#!/usr/bin/env python3
"""brompull.py - zero-boot evidence pull via mtkclient (BROM mode).

Reads expdb (persistent flash) and the live ramoops DRAM region without
booting any kernel/LK, so loop evidence can't be overwritten by a restore
boot. The user puts the device into BROM mode (power off, hold Vol keys,
plug USB), then runs this ONE command from the repo root:

    python src/scripts/brompull.py --label test57

Output lands in build/output/Brom/ (auto-created): expdb-<label>.bin (40MB) and
ramoops-<label>.bin (320KB, best-effort: DRAM may not survive BROM entry).

Requires the mtkclient tree at src/modules/Mediatek/mtk-client and the
evergo firmware set at build/output/Firmwares/evergo_in_images_OS1.0.1.0.TGBINXM_13.0
(preloader + DA). If this SoC needs extra connection flags you already use
(auth/crash/etc.), append them after `--` and they are passed through.
Standalone host use (HOST/Downloads/Brom): same script next to Mediatek/
and firmware/ (preloader_evergo.bin + MTK_AllInOne_DA.bin); paths fall
back automatically, output goes to Brom/out/Brom/.
"""
import sys
import hashlib
import argparse
import subprocess
from pathlib import Path
def pick(*ps):
    for p in ps:
        if Path(p).is_file(): return Path(p)
    return Path(ps[0])
HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
FWSET = REPO / "build" / "output" / "Firmwares" / "evergo_in_images_OS1.0.1.0.TGBINXM_13.0"
MTKCLIENT = pick(REPO / "src" / "modules" / "Mediatek" / "mtk-client" / "mtk", HERE / "Mediatek" / "mtk-client" / "mtk")
PRELOADER = pick(FWSET / "images" / "preloader_evergo.bin", HERE / "firmware" / "preloader_evergo.bin")
DA = pick(FWSET / "MTK_AllInOne_DA.bin", HERE / "firmware" / "MTK_AllInOne_DA.bin")
OUTDIR = (REPO if (REPO / "src" / "scripts").is_dir() else HERE) / "build" / "output" / "Brom"
EXPDB_SIZE = 0x2800000
RAMOOPS_SIZE = 0x50000
RAMOOPS_LEN = "0x50000"
RAMOOPS_ADDR = "0x48090000"
def run(cmd):
    print("+", " ".join(str(c) for c in cmd), flush=True)
    proc = subprocess.run(cmd, capture_output=True, text=True, errors="replace")
    tail = (proc.stdout + proc.stderr).strip().splitlines()[-6:]
    print("\n".join(tail), flush=True)
    return proc.returncode
def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4 << 20), b""):
            h.update(chunk)
    return h.hexdigest()
def main():
    ap = argparse.ArgumentParser(description="Pull expdb+ramoops via BROM, zero boots.")
    ap.add_argument("--label", default=None, help="Tag for output files (default: UTC timestamp).")
    ap.add_argument("--preloader", default=str(PRELOADER))
    ap.add_argument("--loader", default=str(DA))
    ap.add_argument("extra", nargs=argparse.REMAINDER, help="Extra flags appended to every mtk call (after '--').")
    args = ap.parse_args()
    extra = [a for a in args.extra if a != "--"]
    for p, what in [(MTKCLIENT, "mtkclient script"), (args.preloader, "preloader"), (args.loader, "DA loader")]:
        if not Path(p).is_file(): sys.exit(f"missing {what}: {p}")
    from datetime import datetime, timezone
    label = args.label or datetime.now(timezone.utc).strftime("%Y%m%d-%H%M")
    OUTDIR.mkdir(parents=True, exist_ok=True)
    expdb_out = OUTDIR / f"expdb-{label}.bin"
    ramoops_out = OUTDIR / f"ramoops-{label}.bin"
    base = [sys.executable, str(MTKCLIENT), "--preloader", args.preloader, "--loader", args.loader] + extra
    print("device must already be in BROM mode (no kernel/LK boot after the loops).")
    rc = run(base + ["r", "expdb", str(expdb_out)])
    ok_expdb = rc == 0 and expdb_out.is_file()
    if ok_expdb:
        size_ok = expdb_out.stat().st_size == EXPDB_SIZE
        print(f"expdb: {expdb_out.stat().st_size} bytes " f"({'OK' if size_ok else 'SIZE MISMATCH, expected 41943040'})")
        print(f"sha256: {sha256(expdb_out)}")
    rc2 = run(base + ["peek", RAMOOPS_ADDR, RAMOOPS_LEN, "--filename", str(ramoops_out)])
    ok_ram = rc2 == 0 and ramoops_out.is_file()
    if ok_ram:
        print(f"ramoops: {ramoops_out.stat().st_size} bytes " f"(expected ~{RAMOOPS_SIZE}; short read is fine, DRAM may reset)")
    print(f"done. files in {OUTDIR} (send both for analysis).")
    return 0 if ok_expdb else 1
if __name__ == "__main__":
    sys.exit(main())
