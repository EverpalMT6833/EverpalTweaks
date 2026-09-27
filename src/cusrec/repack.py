#!/usr/bin/env python3
import os
import sys
import shutil
import hashlib
import argparse
import subprocess
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TOOLS_DIR = os.path.join(SCRIPT_DIR, "tools")
AVBTOOL = os.path.join(TOOLS_DIR, "avbtool")
MKBOOTIMG = os.path.join(TOOLS_DIR, "mkbootimg.py")
RAMDISKS_DIR = os.path.join(SCRIPT_DIR, "ramdisks")
UNPACK_BOOTIMG = os.path.join(TOOLS_DIR, "unpack_bootimg.py")
OFOX_RAMDISK = os.path.join(RAMDISKS_DIR, "ofox_ramdisk.cpio.gz")
TWRP_RAMDISK = os.path.join(RAMDISKS_DIR, "twrp_ramdisk.cpio.gz")
BOOT_PARTITION_SIZE = 134217728
BOLD = "\033[1m"
RESET = "\033[0m"
RED = "\033[1;31m"
CYAN = "\033[1;36m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()
def check_magic(path: str) -> bool:
    with open(path, "rb") as f:
        magic = f.read(8)
    return magic == b"ANDROID!"
def parse_unpack_info(info_path: str) -> dict:
    params = {}
    if not os.path.exists(info_path):
        return params
    with open(info_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line or ":" not in line:
                continue
            k, v = line.split(":", 1)
            params[k.strip()] = v.strip()
    return params
def main():
    parser = argparse.ArgumentParser(description="Repack an AOSP boot image into an OrangeFox / TWRP recovery boot image for everpal (MT6833).")
    parser.add_argument("aosp_image", help="Path to input AOSP / ROM boot image (e.g. aosp.img)")
    parser.add_argument("--recovery", "-r",choices=["ofox", "twrp"],default="ofox",help="Recovery engine to package (default: ofox)")
    parser.add_argument("-o", "--output",default=None,help="Custom output image path (default: ofox_<aospname>.img or twrp_<aospname>.img)")
    parser.add_argument("-k", "--kernel",default=None,help="Optional custom kernel override (e.g. Image.gz / Aqua #3 kernel)")
    parser.add_argument("--keep-workdir",action="store_true",help="Do not delete temporary extraction work directory")
    args = parser.parse_args()
    input_path = os.path.abspath(args.aosp_image)
    if not os.path.exists(input_path):
        print(f"{RED}[!] Error: Input image '{input_path}' not found!{RESET}")
        sys.exit(1)
    if not check_magic(input_path):
        print(f"{RED}[!] Error: '{input_path}' does not have a valid Android boot header (magic != ANDROID!){RESET}")
        sys.exit(1)
    if args.recovery == "ofox":
        rec_ramdisk = OFOX_RAMDISK
        rec_prefix = "ofox"
        rec_name = "OrangeFox R12.1 (Aqua A16)"
    else:
        rec_ramdisk = TWRP_RAMDISK
        rec_prefix = "twrp"
        rec_name = "TWRP 3.7.1 (Aqua A16)"
    if not os.path.exists(rec_ramdisk):
        print(f"{RED}[!] Error: Recovery ramdisk '{rec_ramdisk}' not found!{RESET}")
        sys.exit(1)
    base_name = os.path.splitext(os.path.basename(input_path))[0]
    out_dir = os.path.dirname(input_path) or os.getcwd()
    if args.output: out_img = os.path.abspath(args.output)
    else: out_img = os.path.join(out_dir, f"{rec_prefix}_{base_name}.img")
    print(f"\n{CYAN}{BOLD}=================================================================={RESET}")
    print(f"{CYAN}{BOLD}       EverpalTweaks Recovery Repacker for Android 16 (MT6833)     {RESET}")
    print(f"{CYAN}{BOLD}=================================================================={RESET}")
    print(f" {BOLD}Target Device:{RESET}   Xiaomi POCO M4 Pro 5G / Redmi Note 11S 5G (everpal / evergo)")
    print(f" {BOLD}Recovery Type:{RESET}   {GREEN}{rec_name}{RESET}")
    print(f" {BOLD}Input AOSP:{RESET}      {input_path} ({os.path.getsize(input_path)} bytes)")
    print(f" {BOLD}Output Target:{RESET}   {out_img}\n")
    work_dir = os.path.join(out_dir, f".repack_tmp_{base_name}")
    if os.path.exists(work_dir): shutil.rmtree(work_dir)
    os.makedirs(work_dir, exist_ok=True)
    try:
        print(f"{YELLOW}[*] Step 1: Unpacking AOSP boot image...{RESET}")
        cmd_unpack = [sys.executable, UNPACK_BOOTIMG,"--boot_img", input_path,"--out", work_dir]
        res = subprocess.run(cmd_unpack, capture_output=True, text=True)
        if res.returncode != 0:
            print(f"{RED}[!] Unpack failed:\n{res.stderr}{RESET}")
            sys.exit(1)

        extracted_kernel = os.path.join(work_dir, "kernel")
        extracted_dtb = os.path.join(work_dir, "dtb")

        # Step 2: Select Kernel & DTB
        kernel_to_use = args.kernel if args.kernel else extracted_kernel
        if not os.path.exists(kernel_to_use):
            print(f"{RED}[!] Error: Kernel binary not found at '{kernel_to_use}'!{RESET}")
            sys.exit(1)

        print(f"  {GREEN}[+] Extracted Kernel:{RESET} {kernel_to_use} ({os.path.getsize(kernel_to_use)} bytes)")
        if os.path.exists(extracted_dtb):
            print(f"  {GREEN}[+] Extracted DTB:{RESET}    {extracted_dtb} ({os.path.getsize(extracted_dtb)} bytes)")
        print(f"  {GREEN}[+] Injected Ramdisk:{RESET} {rec_ramdisk} ({os.path.getsize(rec_ramdisk)} bytes)")

        # Step 3: Parse Header & cmdline
        cmdline = "bootopt=64S3,32N2,64N2 androidboot.selinux=permissive androidboot.hardware=mt6833 buildvariant=eng"

        # Step 4: Build new boot.img with mkbootimg
        print(f"{YELLOW}[*] Step 2: Repacking with {rec_name}...{RESET}")
        mkboot_cmd = [
            sys.executable, MKBOOTIMG,
            "--kernel", kernel_to_use,
            "--ramdisk", rec_ramdisk,
            "--base", "0x40000000",
            "--kernel_offset", "0x00080000",
            "--ramdisk_offset", "0x11100000",
            "--tags_offset", "0x07c80000",
            "--dtb_offset", "0x07c80000",
            "--os_version", "16.0.0",
            "--os_patch_level", "2026-05",
            "--header_version", "2",
            "--pagesize", "2048",
            "--cmdline", cmdline,
            "-o", out_img
        ]
        if os.path.exists(extracted_dtb):
            mkboot_cmd.extend(["--dtb", extracted_dtb])

        res = subprocess.run(mkboot_cmd, capture_output=True, text=True)
        if res.returncode != 0:
            print(f"{RED}[!] mkbootimg failed:\n{res.stderr}{RESET}")
            sys.exit(1)

        # Step 5: Sign / AVB Hash Footer
        print(f"{YELLOW}[*] Step 3: Signing with AVB 2.0 footer for partition size 128 MB...{RESET}")
        key_path = os.path.join(TOOLS_DIR, "testkey_rsa2048.pem")
        avb_cmd = [
            AVBTOOL, "add_hash_footer",
            "--image", out_img,
            "--partition_size", str(BOOT_PARTITION_SIZE),
            "--partition_name", "boot",
            "--algorithm", "SHA256_RSA2048",
            "--key", key_path,
        ]
        if not os.path.exists(key_path):
            avb_cmd = [
                AVBTOOL, "add_hash_footer",
                "--image", out_img,
                "--partition_size", str(BOOT_PARTITION_SIZE),
                "--partition_name", "boot"
            ]

        res = subprocess.run(avb_cmd, capture_output=True, text=True)
        if res.returncode != 0:
            print(f"{YELLOW}[!] AVB signing notice: {res.stderr.strip()}{RESET}")
            # Pad file to 128MB manually if avbtool didn't expand to full partition
            cur_size = os.path.getsize(out_img)
            if cur_size < BOOT_PARTITION_SIZE:
                with open(out_img, "ab") as f:
                    f.write(b"\x00" * (BOOT_PARTITION_SIZE - cur_size))

        final_size = os.path.getsize(out_img)
        final_sha256 = sha256_file(out_img)

        print(f"\n{GREEN}{BOLD}[SUCCESS] Generated Recovery Boot Image!{RESET}")
        print(f" {BOLD}Output File:{RESET}   {out_img}")
        print(f" {BOLD}File Size:{RESET}     {final_size:,} bytes ({final_size // (1024*1024)} MB)")
        print(f" {BOLD}SHA-256:{RESET}       {final_sha256}")

        print(f"\n{CYAN}{BOLD}=== Fastboot Flashing Instructions ==={RESET}")
        print(f"To flash this recovery to your phone in Fastboot mode:")
        out_filename = os.path.basename(out_img)
        print(f"{YELLOW}  fastboot flash boot_a {out_filename}; fastboot flash boot_b {out_filename}; fastboot erase misc; fastboot reboot recovery;{RESET}\n")

    finally:
        if not args.keep_workdir and os.path.exists(work_dir):
            shutil.rmtree(work_dir)


if __name__ == "__main__":
    main()
