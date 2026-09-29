#!/usr/bin/env python3
import sys
import subprocess
from pathlib import Path
ROOT_DIR = Path(__file__).resolve().parent
MTK_DIR = ROOT_DIR / "mtk-client"
if not MTK_DIR.is_dir():
    legacy = ROOT_DIR / "mtkclient"
    if legacy.is_dir():
        MTK_DIR = legacy
def resolve_mtk_entry() -> Path:
    for name in ("mtk", "mtk.py"):
        candidate = MTK_DIR / name
        if candidate.is_file():
            return candidate
    print(f"[-] mtk entry not found in {MTK_DIR}", file=sys.stderr)
    print("    Expected: mtk-client/mtk", file=sys.stderr)
    sys.exit(1)
def pause() -> None:
    try:
        if sys.stdin.isatty():
            input("Press Enter to exit...")
    except (EOFError, KeyboardInterrupt):
        pass
def main() -> int:
    mtk_entry = resolve_mtk_entry()
    print("[*] Stage 1/3: erase metadata + userdata (phone must be in BROM mode)")
    rc = subprocess.run(
        [sys.executable, str(mtk_entry), "e", "metadata,userdata"],
        cwd=str(MTK_DIR),
    ).returncode
    if rc != 0:
        print("[-] erase failed", file=sys.stderr)
        pause()
        return 1
    print("[+] Stage 1 done. The phone has disconnected.")
    print("    Next: put the phone back into BROM mode, then run:")
    print("      python unlockEVERGO_2_flash_lk.py")
    pause()
    return 0
if __name__ == "__main__":
    raise SystemExit(main())
