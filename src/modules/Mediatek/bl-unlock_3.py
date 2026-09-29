#!/usr/bin/env python3
import sys
import subprocess
from pathlib import Path
ROOT_DIR = Path(__file__).resolve().parent
UNLOCK_DIR = ROOT_DIR / "lk-unlocker"
if not UNLOCK_DIR.is_dir() and (ROOT_DIR / "UnlockLK").is_dir():
    UNLOCK_DIR = ROOT_DIR / "UnlockLK"
def pause() -> None:
    try:
        if sys.stdin.isatty():
            input("Press Enter to exit...")
    except (EOFError, KeyboardInterrupt):
        pass
def main() -> int:
    unlock_script = UNLOCK_DIR / "lk-unlock.py"
    private_pem = UNLOCK_DIR / "private.pem"
    if not private_pem.is_file():
        print(f"[-] private.pem not found in {UNLOCK_DIR}", file=sys.stderr)
        print(f'    From that dir run: {sys.executable} lk-unlock.py patch <lk.img> -o lk_patched_evergo.img',
              file=sys.stderr)
        pause()
        return 1
    if not unlock_script.is_file():
        print(f"[-] lk-unlock.py not found in {UNLOCK_DIR}", file=sys.stderr)
        pause()
        return 1
    print("[*] Stage 3/3: fastboot unlock (phone must show up in fastboot devices)")
    rc = subprocess.run(
        [sys.executable, str(unlock_script), "unlock"],
        cwd=str(UNLOCK_DIR),
    ).returncode
    pause()
    return rc
if __name__ == "__main__":
    raise SystemExit(main())
