#!/usr/bin/env python3
"""Flash lk_a + lk_b via mtk-client (BROM mode).

Recovery helper: restores the STOCK lk image after a bad kaeru test flash.
Defaults to the stock evergo lk.img, both slots:

    python lkFLASH.py
    python lkFLASH.py path/to/custom-lk.bin
    python lkFLASH.py a.bin,b.bin
    python lkFLASH.py --slot a path/to/lk.bin

Phone must be in BROM mode: power off, hold Vol+ AND Vol-, plug USB.
"""
import sys
import argparse
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
MTK_DIR = HERE / "mtk-client"
if not MTK_DIR.is_dir():
    for legacy in ("mtk-client", "lk-unlocker"):
        if (HERE / legacy).is_dir():
            MTK_DIR = HERE / legacy
            break
REPO = HERE
for parent in HERE.parents:
    if (parent / "src" / "scripts").is_dir():
        REPO = parent
        break
FWSET = REPO / "build" / "Firmwares" / "evergo_in_images_OS1.0.1.0.TGBINXM_13.0"


def pick(*paths):
    for p in paths:
        if p and Path(p).is_file():
            return str(Path(p))
    return None


DEFAULT_STOCK_LK = pick(
    FWSET / "images" / "lk.img",
    HERE / "firmware" / "lk.img",
    HERE / "dldr-files" / "devices" / "evergo" / "lk.img",
)
DEFAULT_PRELOADER = pick(
    FWSET / "images" / "preloader_evergo.bin",
    HERE / "firmware" / "preloader_evergo.bin",
    HERE / "dldr-files" / "devices" / "evergo" / "preloader_evergo.bin",
)
DEFAULT_LOADER = pick(
    FWSET / "MTK_AllInOne_DA.bin",
    HERE / "firmware" / "MTK_AllInOne_DA.bin",
    HERE / "dldr-files" / "devices" / "evergo" / "MTK_AllInOne_DA.bin",
)


def resolve_mtk_entry():
    for name in ("mtk", "mtk.py"):
        candidate = MTK_DIR / name
        if candidate.is_file():
            return candidate
    sys.exit(f"[-] mtk entry not found in {MTK_DIR} (expected mtk-client/mtk)")


def run(cmd):
    print("+", " ".join(str(c) for c in cmd), flush=True)
    return subprocess.run([str(c) for c in cmd], cwd=str(MTK_DIR)).returncode


def pause():
    try:
        if sys.stdin.isatty():
            input("Press Enter to exit...")
    except (EOFError, KeyboardInterrupt):
        pass


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="Flash lk_a + lk_b via mtk-client (BROM mode). "
                    f"Defaults to stock lk: {DEFAULT_STOCK_LK}"
    )
    ap.add_argument(
        "images", nargs="*",
        help="lk image(s): '<a.bin>,<b.bin>' or '<a.bin> <b.bin>' or single "
             "'<lk.bin>' for both slots (default: stock lk.img)",
    )
    ap.add_argument(
        "--slot", choices=("a", "b", "both"), default="both",
        help="which slot to flash (default: both)",
    )
    ap.add_argument("--preloader", default=DEFAULT_PRELOADER,
                    help=f"preloader for DRAM config (default: {DEFAULT_PRELOADER})")
    ap.add_argument("--loader", default=DEFAULT_LOADER,
                    help=f"DA loader (default: {DEFAULT_LOADER})")
    ap.add_argument("--no-reset", action="store_true", help="skip reset at the end")
    ap.add_argument("extra", nargs=argparse.REMAINDER,
                    help="extra mtk flags appended to write (after '--')")
    args = ap.parse_args(argv)

    parts = []
    for chunk in args.images:
        parts.extend(p for p in chunk.split(",") if p)
    if len(parts) == 0:
        if not DEFAULT_STOCK_LK:
            print("[-] stock lk.img not found, pass an image explicitly",
                  file=sys.stderr)
            return 1
        print(f"[*] no image given, using stock: {DEFAULT_STOCK_LK}")
        img_a, img_b = DEFAULT_STOCK_LK, DEFAULT_STOCK_LK
    elif len(parts) == 1:
        img_a, img_b = parts[0], parts[0]
    elif len(parts) == 2:
        img_a, img_b = parts
    else:
        ap.error("give 0-2 images: '[<lk.bin>]' or '<a.bin>,<b.bin>'")
        return 2

    if args.slot == "a":
        targets, files = "lk_a", img_a
    elif args.slot == "b":
        targets, files = "lk_b", img_b
    else:
        targets, files = "lk_a,lk_b", f"{img_a},{img_b}"
    for img in (files.split(",") if "," in files else [files]):
        if not Path(img).is_file():
            print(f"[-] image not found: {img}", file=sys.stderr)
            return 1

    conn = []
    if args.preloader:
        if not Path(args.preloader).is_file():
            print(f"[-] preloader not found: {args.preloader}", file=sys.stderr)
            return 1
        conn += ["--preloader", args.preloader]
    if args.loader:
        if not Path(args.loader).is_file():
            print(f"[-] loader not found: {args.loader}", file=sys.stderr)
            return 1
        conn += ["--loader", args.loader]
    extra = [a for a in args.extra if a != "--"]
    mtk_entry = resolve_mtk_entry()
    print("[*] lk_a/b flash — phone must be in BROM mode "
          "(power off, hold Vol+ and Vol-, plug USB)")
    rc = run([sys.executable, str(mtk_entry), "w", targets, files] + conn + extra)
    if rc != 0:
        print(f"[-] {targets} flash failed", file=sys.stderr)
        pause()
        return 1
    if not args.no_reset:
        rc = run([sys.executable, str(mtk_entry), "reset"])
        if rc != 0:
            print("[!] auto-reset failed, reboot manually: Power + Vol Down")
    print(f"[+] done: {targets} <- {files}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
