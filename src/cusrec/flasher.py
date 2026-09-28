import os
import sys
import subprocess
from pathlib import Path

os.system("")

RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"

BASE_DIR = Path(__file__).resolve().parent
AOSP_ROOT = BASE_DIR / "AospBOOT_ROOT.img"
TWRP_ROOT = BASE_DIR / "TwrpBOOT_ROOT.img"
AOSP_NOROOT = BASE_DIR / "AospBOOT_noROOT.img"
TWRP_NOROOT = BASE_DIR / "TwrpBOOT_noROOT.img"


def c(text, color):
    return f"{color}{text}{RESET}"


def fail_simple():
    print(c("\nSomething went wrong. Check the USB cable,", RED))
    print(c("make sure the phone is in fastboot mode, and try again.", RED))
    input("Press Enter to close...")
    sys.exit(1)


def run_quiet(*args):
    try:
        r = subprocess.run(
            args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            text=True, errors="replace",
        )
    except FileNotFoundError:
        fail_simple()
    if r.returncode != 0:
        fail_simple()
    return r.stdout


def set_active(slot):
    r = subprocess.run(
        ["fastboot", f"--set-active={slot}"],
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        text=True, errors="replace",
    )
    if r.returncode != 0:
        run_quiet("fastboot", "set_active", slot)


def ask(question, hint=None, warn=None):
    print(c(f"\n{question}", BOLD + YELLOW))
    if hint:
        print(c(hint, GREEN))
    if warn:
        print(c(warn, RED))
    while True:
        a = input("Answer [y/n]: ").strip().lower()
        if a in ("y", "yes"):
            return True
        if a in ("n", "no"):
            return False
        print("Please type y or n.")


def main():
    print(c("PHONE FLASHER", BOLD + CYAN))
    print("Connect the phone in fastboot mode with a USB cable.\n")
    try:
        want_root = ask(
            "1/4 - Want root?",
            hint="Yes = full control.  No = normal, best for banking apps.",
        )
        ROM_IMG = AOSP_ROOT if want_root else AOSP_NOROOT
        REC_IMG = TWRP_ROOT if want_root else TWRP_NOROOT

        if not ROM_IMG.is_file() or not REC_IMG.is_file():
            print(c("\nFiles missing. Put the .img files next to flasher.py.", RED))
            input("Press Enter to close...")
            sys.exit(1)

        out = run_quiet("fastboot", "getvar", "slot-successful:a")
        lo = out.lower()
        if "slot-successful:a: yes" in lo:
            rom, rec = "a", "b"
        elif "slot-successful:a: no" in lo:
            rom, rec = "b", "a"
        else:
            fail_simple()

        want_wipe = ask(
            "2/4 - Erase everything?",
            hint="Yes = fresh start.  No = keep photos and apps.",
            warn="Yes deletes everything!",
        )

        print(c("\nInstalling... please wait, do not unplug.", CYAN))
        run_quiet("fastboot", "flash", f"boot_{rom}", str(ROM_IMG))
        run_quiet("fastboot", "flash", f"boot_{rec}", str(REC_IMG))
        if want_wipe:
            run_quiet("fastboot", "erase", "userdata")

        # Clear /misc to erase stale boot-recovery flags and reset BCAB state
        run_quiet("fastboot", "erase", "misc")

        want_rec = ask(
            "3/4 - Open recovery after install?",
            hint="No = start phone normally.  Yes = open AOSP recovery or TWRP recovery.",
        )
        if want_rec:
            print(c("\n4/4 - Which one?", BOLD + YELLOW))
            print(c("1 = AOSP recovery.  2 = TWRP recovery.", GREEN))
            while True:
                p = input("Answer [1/2]: ").strip()
                if p in ("1", "2"):
                    break
                print("Please type 1 or 2.")
            target = rom if p == "1" else rec
            target_name = "AOSP recovery" if p == "1" else "TWRP recovery"
            set_active(target)
            # In MT6833 dual-slot architecture, TWRP is resident directly in boot_{rec}.
            # Standard 'fastboot reboot' boots the selected active slot cleanly without
            # triggering the MTK boot-recovery fallback or bootloader panics.
            run_quiet("fastboot", "reboot")
            print(c(f"\nDone! Opening {target_name}.", BOLD + GREEN))
        else:
            set_active(rom)
            run_quiet("fastboot", "reboot")
            print(c("\nDone! Phone is restarting.", BOLD + GREEN))

        print("You can unplug now.")
        input("Press Enter to close...")
    except KeyboardInterrupt:
        print("\nCancelled.")
        sys.exit(1)


if __name__ == "__main__":
    main()
