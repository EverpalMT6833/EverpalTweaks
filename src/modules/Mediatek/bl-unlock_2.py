#!/usr/bin/env python3
import sys
import subprocess
from pathlib import Path
ROOT_DIR = Path(__file__).resolve().parent
MTK_DIR = ROOT_DIR / "mtk-client"
UNLOCK_DIR = ROOT_DIR / "lk-unlocker"
if not MTK_DIR.is_dir() and (ROOT_DIR / "mtkclient").is_dir():
    MTK_DIR = ROOT_DIR / "mtkclient"
if not UNLOCK_DIR.is_dir() and (ROOT_DIR / "lk-unlock").is_dir():
    UNLOCK_DIR = ROOT_DIR / "lk-unlock"
if not UNLOCK_DIR.is_dir() and (ROOT_DIR / "UnlockLK").is_dir():
    UNLOCK_DIR = ROOT_DIR / "UnlockLK"
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
def main(argv: list) -> int:
    mtk_entry = resolve_mtk_entry()
    if len(argv) > 1:
        patched_lk = Path(argv[1])
    else:
        candidates = [
            UNLOCK_DIR / "lk_patched_evergo.img",
            UNLOCK_DIR / "lk_patched.img",
        ]
        patched_lk = next((c for c in candidates if c.is_file()), candidates[0])

    if not patched_lk.is_file():
        print(f"[-] Patched LK not found in {UNLOCK_DIR}", file=sys.stderr)
        print(f"    Expected: {patched_lk.name}", file=sys.stderr)
        print(f'    From the lk-unlocker dir run: {sys.executable} lk-unlock.py patch <lk.img> -o lk_patched_evergo.img',
              file=sys.stderr)
        pause()
        return 1

    print("[*] Stage 2/3: flash patched LK to lk_a + lk_b (phone must be in BROM mode)")
    print(f"[*] Flashing image: {patched_lk}")
    rc = subprocess.run(
        [sys.executable, str(mtk_entry), "w", "lk_a,lk_b", f"{patched_lk},{patched_lk}"],
        cwd=str(MTK_DIR),
    ).returncode

    state_file = MTK_DIR / ".state"
    if state_file.is_file():
        try:
            state_file.unlink()
        except OSError:
            pass

    if rc != 0:
        print("[-] LK flash failed", file=sys.stderr)
        pause()
        return 1

    print("[+] Stage 2 done: patched LK flashed to lk_a and lk_b.")
    print("    Next: disconnect USB, boot to fastboot (Power + Vol Down), then run:")
    print("      python bl-unlock_3.py")
    pause()
    return 0
if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
