#!/usr/bin/env python3
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
FWSET = REPO / "out" / "Firmwares" / "evergo_in_images_OS1.0.1.0.TGBINXM_13.0"
def pick(*paths):
    for p in paths:
        if p and Path(p).is_file():
            return str(Path(p))
    return None
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
    ap = argparse.ArgumentParser(description="Flash boot_a + boot_b via mtk-client (erases misc first).")
    ap.add_argument("images", nargs="+",help="boot image(s): '<a.img>,<b.img>' or '<a.img> <b.img>' or single '<boot.img>' for both slots")
    ap.add_argument("--preloader", default=DEFAULT_PRELOADER,help=f"preloader for DRAM config (default: {DEFAULT_PRELOADER})")
    ap.add_argument("--loader", default=DEFAULT_LOADER,help=f"DA loader (default: {DEFAULT_LOADER})")
    ap.add_argument("--skip-misc", action="store_true", help="skip misc erase")
    ap.add_argument("--no-reset", action="store_true", help="skip reset at the end")
    ap.add_argument("extra", nargs=argparse.REMAINDER,help="extra mtk flags appended to erase/write (after '--')")
    args = ap.parse_args(argv)
    parts = []
    for chunk in args.images:
        parts.extend(p for p in chunk.split(",") if p)
    if len(parts) == 1:
        img_a, img_b = parts[0], parts[0]
    elif len(parts) == 2:
        img_a, img_b = parts
    else:
        ap.error("give 1 image (both slots) or 2 images 'a.img,b.img'")
        return 2
    for img in (img_a, img_b):
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
    print("[*] boot_a/b flash (phone must be in BROM mode)")
    if not args.skip_misc:
        rc = run([sys.executable, str(mtk_entry), "e", "misc"] + conn + extra)
        if rc != 0:
            print("[-] misc erase failed", file=sys.stderr)
            pause()
            return 1
    rc = run([sys.executable, str(mtk_entry), "w", "boot_a,boot_b", f"{img_a},{img_b}"] + conn + extra)
    if rc != 0:
        print("[-] boot_a/boot_b flash failed", file=sys.stderr)
        pause()
        return 1
    if not args.no_reset:
        rc = run([sys.executable, str(mtk_entry), "reset"])
        if rc != 0:
            print("[!] auto-reset failed, reboot manually: Power + Vol Down")
    print(f"[+] done: misc wiped, boot_a={img_a} boot_b={img_b}")
    return 0
if __name__ == "__main__":
    raise SystemExit(main())
