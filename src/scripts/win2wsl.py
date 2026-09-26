#!/usr/bin/env python3
import re, sys, time, base64, shutil, argparse, subprocess

def powershell(script, check=True):
    encoded = base64.b64encode(script.encode("utf-16le")).decode("ascii")
    result = subprocess.run(["powershell.exe","-NoProfile","-NonInteractive","-ExecutionPolicy", "Bypass","-EncodedCommand", encoded,],text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,)
    output = result.stdout.replace("\r\n", "\n").strip()
    if output:
        print(output)
    if check and result.returncode != 0:
        raise RuntimeError(f"PowerShell failed (exit {result.returncode})")
    return result.returncode
def list_devices():
    print("\n=== Windows USB devices ===\n")
    script = r"""
$ErrorActionPreference = 'Stop'
usbipd list
"""
    encoded = base64.b64encode(script.encode("utf-16le")).decode("ascii")
    result = subprocess.run(["powershell.exe", "-NoProfile","-ExecutionPolicy", "Bypass","-EncodedCommand", encoded,],text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,)
    output = result.stdout.replace("\r\n", "\n")
    print(output)
    if result.returncode != 0:
        raise RuntimeError("Could not run usbipd. Is usbipd-win installed?")
    return output
def bind_device(busid):
    print(f"\nSharing USB device {busid}...")
    print("Approve the Windows UAC prompt if requested.")
    script = f"""
$ErrorActionPreference = 'Stop'
$arg = '-NoProfile -Command "usbipd bind --busid {busid}"'
$p = Start-Process powershell.exe -Verb RunAs `
    -ArgumentList $arg -Wait -PassThru
exit $p.ExitCode
"""
    return powershell(script, check=False)
def attach_device(busid):
    print(f"\nAttaching {busid} to WSL...")
    script = f"""
$ErrorActionPreference = 'Stop'
usbipd attach --wsl --busid {busid}
exit $LASTEXITCODE
"""
    return powershell(script, check=False)
def tunnel():
    if shutil.which("powershell.exe") is None:
        sys.exit("ERROR: powershell.exe not found. ""Run this script inside WSL with Windows interop enabled.")
    print("=== Windows -> WSL USB tunnel ===")
    print("ADB and fastboot will run inside WSL.")
    print("Windows tools will not access an attached device.")
    while True:
        try:
            output = list_devices()
        except RuntimeError as exc:
            print(f"\nERROR: {exc}")
            return 1
        busids = re.findall(r"(?m)^\s*(\d+-\d+(?:\.\d+)*)\s+",output,)
        if not busids:
            print("No USB devices found.")
            input("Connect your phone, then press Enter...")
            continue
        busid = input("\nEnter phone BUSID (or q to quit): ").strip()
        if busid.lower() in ("q", "quit", "exit"):
            break
        if busid not in busids:
            print("Invalid BUSID. Select one from the list.")
            continue
        rc = attach_device(busid)
        if rc != 0:
            print("\nAttach failed. Attempting to share the device...")
            rc = bind_device(busid)
            if rc == 0:
                rc = attach_device(busid)
        if rc == 0:
            print(f"\nUSB device {busid} attached.")
            print("Check inside WSL:")
            print("  lsusb")
            print("  adb devices")
            print("  fastboot devices")
        else:
            print("\nAttach failed. Check the UAC prompt, ""usbipd service, and device state.")
        print("\nIf the phone changes USB mode, ""select its new BUSID.")
        answer = input("\nReconnect/select another device? [Y/n]: ").strip().lower()
        if answer in ("n", "no"):
            break
        time.sleep(1)
    print("\nExited.")
    return 0
def main():
    parser = argparse.ArgumentParser(description="Forward Windows USB devices into WSL 2")
    parser.add_argument("--tunnel",action="store_true",help="Start interactive USB passthrough",)
    args = parser.parse_args()
    if args.tunnel:
        return tunnel()
    parser.print_help()
    return 0
if __name__ == "__main__":
    sys.exit(main())
