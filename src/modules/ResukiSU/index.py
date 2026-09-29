import os
import re
import sys
import gzip
import shutil
import zipfile
import argparse
import tempfile
import subprocess
from pathlib import Path
def _find_kernel_in_zip(z: zipfile.ZipFile) -> str:
    candidates = ['image.gz', 'image', 'image.lz4', 'zimage', 'kernel']
    for name in z.namelist():
        if os.path.basename(name).lower() in candidates:
            return name
    for name in z.namelist():
        if name.endswith('/') or name.startswith('META-INF/') or name.startswith('tools/'):
            continue
        try:
            head = z.read(name)[:64]
            if head.startswith(b'\x1f\x8b') or head.startswith(b'\x04\x22\x4d\x18'):
                return name
            if len(head) >= 60 and head[56:60] == b'ARM\x64':
                return name
        except Exception:
            continue
    raise FileNotFoundError("Could not find a valid kernel binary inside the zip archive.")
def _is_anykernel_zip(p: Path) -> bool:
    try:
        with zipfile.ZipFile(p, 'r') as z:
            names = [n.lower() for n in z.namelist()]
            return any('anykernel' in n or 'image' in n or 'kernel' in n for n in names)
    except Exception:
        return False
def _list_kernelzips(directory: Path):
    zips = [p for p in directory.glob("*.zip") if p.is_file()]
    if not zips:
        raise FileNotFoundError(f"No .zip files found in {directory}")
    def version_key(p: Path):
        return [int(c) if c.isdigit() else c.lower() for c in re.split(r'(\d+)', p.name)]
    kernel_zips = [p for p in zips if _is_anykernel_zip(p)]
    candidates = kernel_zips if kernel_zips else zips
    candidates.sort(key=version_key, reverse=True)
    return candidates
def _auto_detect_kernelzip(directory: Path) -> Path:
    candidates = _list_kernelzips(directory)
    chosen = candidates[0]
    print(f"[+] Auto-detected kernel zip: {chosen.name}")
    return chosen
def _is_kernel_gz(p: Path) -> bool:
    try:
        with open(p, 'rb') as f:
            head = f.read(2)
        if head != b'\x1f\x8b':
            return False
        with gzip.open(p, 'rb') as gf:
            inner = gf.read(64)
        if len(inner) >= 60 and inner[56:60] == b'ARM\x64':
            return True
        if inner.startswith(b'ANDROID!'):
            return False
        return len(inner) > 0
    except Exception:
        return False
def _list_kernel_gz(directory: Path):
    gz_files = [p for p in directory.glob("*.gz") if p.is_file()]
    gz_files = [p for p in gz_files if 'cpio' not in p.name.lower() and 'ramdisk' not in p.name.lower()]
    if not gz_files:
        return []
    def version_key(p: Path):
        return [int(c) if c.isdigit() else c.lower() for c in re.split(r'(\d+)', p.name)]
    kernel_gz = [p for p in gz_files if _is_kernel_gz(p)]
    candidates = kernel_gz if kernel_gz else gz_files
    candidates.sort(key=version_key, reverse=True)
    return candidates
def _auto_detect_kernel_gz(directory: Path) -> Path:
    candidates = _list_kernel_gz(directory)
    if not candidates:
        raise FileNotFoundError(f"No .gz kernel files found in {directory}")
    chosen = candidates[0]
    print(f"[+] Auto-detected kernel gz: {chosen.name}")
    return chosen
def _list_base_imgs(directory: Path):
    skip_suffixes = ('-resukisu.img', '-stock.img')
    search_dirs = []
    aosp_dir = directory / "images" / "aosp"
    if aosp_dir.is_dir():
        search_dirs.append(aosp_dir)
    search_dirs.append(directory)
    candidates = []
    for d in search_dirs:
        for p in d.glob("*.img"):
            if not p.is_file():
                continue
            n = p.name.lower()
            if n.startswith("boot_") or n.endswith(skip_suffixes):
                continue
            candidates.append(p)
    candidates.sort(key=lambda p: p.name.lower())
    return candidates
def _find_fronxkernel_zip(directory: Path) -> Path:
    zips = [p for p in directory.glob("FronxKernel-*.zip") if p.is_file()]
    if not zips:
        raise FileNotFoundError(
            f"No FronxKernel-*.zip in {directory} — copy one from EverpalTweaks out/ "
            "(FronxKernel-1.0-ResukiSU.zip or FronxKernel-1.0.zip)")
    def version_key(p: Path):
        return [int(c) if c.isdigit() else c.lower() for c in re.split(r'(\d+)', p.name)]
    fronx = [p for p in zips if _is_anykernel_zip(p)] or zips
    resukisu = [p for p in fronx if 'resukisu' in p.name.lower()]
    chosen = (resukisu or sorted(fronx, key=version_key, reverse=True))[0]
    print(f"[+] Using FronxKernel zip: {chosen.name}")
    return chosen
def _latest_resukisu_gz(directory: Path) -> Path:
    """Newest vN-resukisu.gz by version sort; falls back to newest kernel .gz."""
    gz_cands = _list_kernel_gz(directory)
    if not gz_cands:
        raise FileNotFoundError(f"No .gz kernel files found in {directory}")
    resukisu = [p for p in gz_cands if 'resukisu' in p.name.lower()]
    chosen = (resukisu or gz_cands)[0]
    print(f"[+] Selected kernel: {chosen.name}")
    return chosen
def _root_output_for(base_img: Path, script_dir: Path) -> Path:
    stem = base_img.name
    if stem.lower().endswith('.img'):
        stem = stem[:-4]
    stem = stem.replace(" ", "_")
    if stem.lower().endswith('-resukisu'):
        stem = stem[:-len('-resukisu')]
    out_dir = script_dir / "images" / "root"
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir / f"{stem}-ResukiSU.img"
def _resolve_kernel_gz_to_workdir(kernel_gz: Path, work_dir: Path) -> Path:
    print(f"[+] Using raw kernel gzip: {kernel_gz.name}")
    try:
        with gzip.open(kernel_gz, 'rb') as gf:
            inner = gf.read(64)
        if inner.startswith(b'ANDROID!'):
            raise ValueError(f"{kernel_gz.name} looks like a gzipped boot.img, not a kernel Image.gz")
        if len(inner) >= 60 and inner[56:60] == b'ARM\x64':
            print("[+] Validated ARM64 Image inside gzip (ARMd @ offset 56)")
        else:
            print("[!] WARNING: no ARMd marker inside gzip - continuing anyway")
    except ValueError:
        raise
    except Exception as err:
        print(f"[!] WARNING: could not validate gzip contents ({err}) - continuing anyway")
    dest = work_dir / "kernel_new"
    shutil.copyfile(kernel_gz, dest)
    return dest
def _auto_detect_bootimg(directory: Path) -> Path:
    candidates = [p for p in directory.glob("*.img") if p.is_file() and not p.name.startswith("boot_") and not p.name.lower().endswith(('-resukisu.img', '-stock.img'))]
    aosp_dir = directory / "images" / "aosp"
    if aosp_dir.is_dir():
        candidates += [p for p in aosp_dir.glob("*.img") if p.is_file() and not p.name.startswith("boot_") and not p.name.lower().endswith(('-resukisu.img', '-stock.img'))]
    if not candidates:
        candidates = [p for p in directory.glob("*.img") if p.is_file()]
    if not candidates:
        raise FileNotFoundError(f"No .img files found in {directory} or {aosp_dir}")
    candidates.sort(key=lambda p: p.stat().st_mtime, reverse=True)
    chosen = candidates[0]
    print(f"[+] Auto-detected base boot image: {chosen.name}")
    return chosen
def _parse_unpack_output(text: str):
    params = {}
    for line in text.splitlines():
        line = line.strip()
        if not line or ':' not in line:
            continue
        key, val = line.split(':', 1)
        params[key.strip()] = val.strip()
    return params
def _parse_avb_info(text: str):
    avb_info = {'has_avb': False,'partition_size': None,'partition_name': 'boot','algorithm': 'SHA256_RSA2048','salt': None,'props': []}
    if 'Footer version:' in text or 'VBMeta offset:' in text:
        avb_info['has_avb'] = True
    for line in text.splitlines():
        line = line.strip()
        if line.startswith('Image size:'):
            match = re.search(r'(\d+)\s+bytes', line)
            if match:
                avb_info['partition_size'] = match.group(1)
        elif line.startswith('Partition Name:'):
            avb_info['partition_name'] = line.split(':', 1)[1].strip()
        elif line.startswith('Algorithm:'):
            avb_info['algorithm'] = line.split(':', 1)[1].strip()
        elif line.startswith('Salt:'):
            avb_info['salt'] = line.split(':', 1)[1].strip()
        elif line.startswith('Prop:'):
            prop_part = line.split('Prop:', 1)[1].strip()
            if '->' in prop_part:
                k, v = prop_part.split('->', 1)
                avb_info['props'].append(f"{k.strip()}:{v.strip().strip('\'\"')}")
    return avb_info
def main(kernelzip: str = "", bootimg: str = "", output: str = ""):
    script_dir = Path(__file__).resolve().parent
    if not kernelzip and not bootimg and not output:
        bases = _list_base_imgs(script_dir)
        if not bases:
            raise FileNotFoundError(f"No base .img files found in {script_dir / 'images' / 'aosp'}")
        try:
            kernel = _find_fronxkernel_zip(script_dir)
        except FileNotFoundError:
            kernel = _latest_resukisu_gz(script_dir)
        print(f"[*] Building {len(bases)} image(s) with {kernel.name} - one per base in images/aosp/")
        results = []
        for b in bases:
            print(f"--- {b.name} ---")
            results.append(_build_single(kernelzip=str(kernel), bootimg=str(b), output=str(_root_output_for(b, script_dir))))
        print(f"[SUCCESS] Built {len(results)} image(s)")
        return results
    return _build_single(kernelzip=kernelzip, bootimg=bootimg, output=output)
def _build_single(kernelzip: str = "", bootimg: str = "", output: str = "") -> str:
    script_dir = Path(__file__).resolve().parent
    python_dir = script_dir / "python"
    avbtool_script = python_dir / "avbtool.py"
    mkbootimg_script = python_dir / "mkbootimg.py"
    unpack_script = python_dir / "unpack_bootimg.py"
    testkey_path = python_dir / "testkey_rsa2048.pem"
    if not kernelzip:
        try:
            kzip_path = _find_fronxkernel_zip(script_dir)
        except FileNotFoundError:
            gz_cands = _list_kernel_gz(script_dir)
            if gz_cands:
                kzip_path = gz_cands[0]
                print(f"[+] Auto-detected kernel gz: {kzip_path.name}")
            else:
                kzip_path = _auto_detect_kernelzip(script_dir)
    else:
        kzip_path = Path(kernelzip).resolve()
        if not kzip_path.is_file() and (script_dir / kernelzip).is_file():
            kzip_path = (script_dir / kernelzip).resolve()
        if not kzip_path.is_file():
            raise FileNotFoundError(f"Kernel source file not found: {kernelzip}")
        if kzip_path.suffix.lower() not in ('.zip', '.gz'):
            print(f"[!] WARNING: unexpected kernel source extension '{kzip_path.suffix}' - continuing anyway")
    if not bootimg:
        paired = None
        cand = script_dir / "AospBOOT.img"
        if cand.is_file():
            paired = cand
        else:
            aosp_cands = sorted((script_dir / "images" / "aosp").glob("*BOOT.img"))
            aosp_cands = [p for p in aosp_cands
                          if not p.name.lower().endswith(('-resukisu.img', '-stock.img'))]
            if aosp_cands:
                paired = aosp_cands[0]
        if paired is not None:
            bimg_path = paired
            print(f"[+] Paired base boot image: {bimg_path.name}")
        else:
            bimg_path = _auto_detect_bootimg(script_dir)
    else:
        bimg_path = Path(bootimg).resolve()
        if not bimg_path.is_file() and (script_dir / bootimg).is_file():
            bimg_path = (script_dir / bootimg).resolve()
        if not bimg_path.is_file():
            raise FileNotFoundError(f"Base boot image file not found: {bootimg}")
    if not output:
        base_name = kzip_path.name
        if base_name.lower().endswith('.gz'):
            base_name = base_name[:-3]
        clean_zip_stem = Path(base_name).stem.replace(" ", "_")
        if clean_zip_stem.lower().endswith('.img'):
            clean_zip_stem = clean_zip_stem[:-4]
        prefix = "" if clean_zip_stem.lower().startswith("boot_") else "boot_"
        output_name = f"{prefix}{clean_zip_stem}.img"
        out_path = script_dir / output_name
    else:
        out_path = Path(output).resolve()
    print("\n--- Repack Configuration ---")
    print(f"[*] Base Boot Image : {bimg_path.name} ({bimg_path.stat().st_size:,} bytes)")
    print(f"[*] Kernel Source   : {kzip_path.name}")
    print(f"[*] Output Target   : {out_path.name}")
    print("----------------------------\n")
    work_dir = Path(tempfile.mkdtemp(prefix="kernel_repack_"))
    try:
        if kzip_path.suffix.lower() == '.gz':
            extracted_kernel = _resolve_kernel_gz_to_workdir(kzip_path, work_dir)
        else:
            with zipfile.ZipFile(kzip_path, 'r') as z:
                k_entry = _find_kernel_in_zip(z)
                print(f"[+] Found kernel binary inside zip: {k_entry}")
                extracted_kernel = work_dir / "kernel_new"
                with open(extracted_kernel, 'wb') as f:
                    f.write(z.read(k_entry))
        unpacked_dir = work_dir / "unpacked"
        unpacked_dir.mkdir()
        unpack_cmd = [
            sys.executable, str(unpack_script),
            "--boot_img", str(bimg_path),
            "--out", str(unpacked_dir)
        ]
        unpack_proc = subprocess.run(unpack_cmd, capture_output=True, text=True, check=True)
        params = _parse_unpack_output(unpack_proc.stdout)
        hdr_ver = params.get('boot image header version', '2')
        page_size = params.get('page size', '2048')
        cmdline = params.get('command line args', '')
        extra_cmdline = params.get('additional command line args', '')
        os_version = params.get('os version', '')
        os_patch_level = params.get('os patch level', '')
        kernel_addr_str = params.get('kernel load address', '0x40080000')
        ramdisk_addr_str = params.get('ramdisk load address', '0x51100000')
        tags_addr_str = params.get('kernel tags load address', '0x47c80000')
        dtb_addr_str = params.get('dtb address', '0x47c80000')
        kernel_addr = int(kernel_addr_str, 16)
        ramdisk_addr = int(ramdisk_addr_str, 16)
        tags_addr = int(tags_addr_str, 16)
        base = kernel_addr & ~0x00FFFFFF
        kernel_offset = kernel_addr - base
        ramdisk_offset = ramdisk_addr - base
        tags_offset = tags_addr - base
        ramdisk_file = unpacked_dir / "ramdisk"
        dtb_file = unpacked_dir / "dtb"
        avb_cmd = [sys.executable, str(avbtool_script), "info_image", "--image", str(bimg_path)]
        avb_proc = subprocess.run(avb_cmd, capture_output=True, text=True)
        avb_info = _parse_avb_info(avb_proc.stdout) if avb_proc.returncode == 0 else {'has_avb': False}
        mkboot_cmd = [
            sys.executable, str(mkbootimg_script),
            "--kernel", str(extracted_kernel),
            "--ramdisk", str(ramdisk_file),
            "--base", hex(base),
            "--kernel_offset", hex(kernel_offset),
            "--ramdisk_offset", hex(ramdisk_offset),
            "--tags_offset", hex(tags_offset),
            "--pagesize", page_size,
            "--header_version", hdr_ver,
            "-o", str(out_path)
        ]
        if dtb_file.is_file() and int(params.get('dtb size', '0')) > 0:
            dtb_addr = int(dtb_addr_str, 16)
            dtb_offset = dtb_addr - base
            mkboot_cmd.extend(["--dtb", str(dtb_file), "--dtb_offset", hex(dtb_offset)])
        recovery_dtbo_file = unpacked_dir / "recovery_dtbo"
        if recovery_dtbo_file.is_file() and int(params.get('recovery dtbo size', '0')) > 0:
            mkboot_cmd.extend(["--recovery_dtbo", str(recovery_dtbo_file)])
        if cmdline:
            mkboot_cmd.extend(["--cmdline", cmdline])
        if extra_cmdline:
            mkboot_cmd.extend(["--extra_cmdline", extra_cmdline])
        if os_version:
            mkboot_cmd.extend(["--os_version", os_version])
        if os_patch_level:
            mkboot_cmd.extend(["--os_patch_level", os_patch_level])
        print("[+] Repacking boot image with mkbootimg...")
        subprocess.run(mkboot_cmd, capture_output=True, text=True, check=True)
        if avb_info.get('has_avb'):
            print("[+] Original image has AVB footer. Adding signed AVB hash footer...")
            part_size = avb_info.get('partition_size') or str(bimg_path.stat().st_size)
            part_name = avb_info.get('partition_name') or 'boot'
            algo = avb_info.get('algorithm') or 'SHA256_RSA2048'
            salt = avb_info.get('salt') or 'ea8468a030d2b72074a1da8937fe69585e5eb96a445aabf43443e65125df5ecb'
            avb_sign_cmd = [
                sys.executable, str(avbtool_script), "add_hash_footer",
                "--image", str(out_path),
                "--partition_size", str(part_size),
                "--partition_name", part_name,
                "--algorithm", algo,
                "--key", str(testkey_path),
                "--salt", salt
            ]
            for prop in avb_info.get('props', []):
                avb_sign_cmd.extend(["--prop", prop])
            subprocess.run(avb_sign_cmd, capture_output=True, text=True, check=True)
            print("[+] AVB footer signed successfully.")
        final_size = out_path.stat().st_size
        print(f"\n[SUCCESS] Flashable image generated: {out_path.name}")
        print(f"          Path: {out_path}")
        print(f"          Size: {final_size:,} bytes ({final_size / (1024*1024):.2f} MB)")
        return str(out_path)
    finally:
        shutil.rmtree(work_dir, ignore_errors=True)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create flashable boot.img(s) from a staged FronxKernel zip (copy from EverpalTweaks out/), falling back to loose .gz/.zip kernel sources, plus base boot.img.")
    parser.add_argument("kernelzip_pos", nargs="?", default="", help="Path to kernel .gz or AnyKernel3 zip (optional)")
    parser.add_argument("bootimg_pos", nargs="?", default="", help="Path to base boot.img (optional)")
    parser.add_argument("-k", "--kernelzip", default="", help="Path to kernel .gz or AnyKernel3 zip")
    parser.add_argument("-b", "--bootimg", default="", help="Path to base boot.img")
    parser.add_argument("-o", "--output", default="", help="Path for output .img file")
    args = parser.parse_args()
    kzip = args.kernelzip or args.kernelzip_pos
    bimg = args.bootimg or args.bootimg_pos
    try:
        main(kernelzip=kzip, bootimg=bimg, output=args.output)
    except Exception as err:
        print(f"\n[ERROR] {err}", file=sys.stderr)
        sys.exit(1)
