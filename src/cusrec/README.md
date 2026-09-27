# `cusrec` — Universal Android 16 Recovery Repacker for `evergo` Family

> **Automated Custom Recovery Repacker for MediaTek Dimensity 810 (MT6833 / MT6833P)**  
> Supported Family: **`evergo`, `everpal`, `evergreen`, `opal`**  
> Supported OS: **Android 16** (AlphaDroid, Project Infinity, LineageOS 23.0, AOSP)  
> Author: **FrontlXOX / Shovit Dutta**

---

## 1. Multi-SKU Universal Hardware Support

`cusrec` is engineered to support **all 5 commercial hardware variants** of the Xiaomi MediaTek Dimensity 810 platform. 

The recovery dynamically reads `ro.boot.board_id` directly from the hardware bootloader (`lk`) at runtime via `unified-script.sh` to configure the exact model, market name, and device assertion properties:

| Board ID | Codename | Commercial Name | Model Number | Market Region |
| :--- | :--- | :--- | :--- | :--- |
| **`S98016LA1`** | **`everpal`** / `evergo` | **POCO M4 Pro 5G** | `22031116AI` | India |
| **`S98017AA1`** | **`evergreen`** / `everpal` | **POCO M4 Pro 5G** | `21091116AG` | Global |
| **`S98018AA1`** | **`opal`** / `everpal` | **Redmi Note 11S 5G** | `22031116BG` | Global |
| **`S98016AA1`** | **`evergo`** | **Redmi Note 11 5G** | `21091116AC` | China |
| **`S98016BA1`** | **`evergo`** | **Redmi Note 11T 5G** | `21091116AI` | India |

If an unrecognized board ID is encountered, the script automatically falls back to `load_evergreen_g` (the universal global SKU).

---

## 2. Why `repack.py` is 100% Universal Across All Devices

Different variants and ROMs have slight differences in panel timings (e.g. KTZ8863A vs Novatek panels) and camera sensors. 

`repack.py` solves this automatically:
1. **Preserves Native Kernel & DTB:** It extracts the exact kernel and device tree blob (`dtb`) from the input `boot.img` provided by that device's ROM.
2. **Injects Unified Multi-SKU Ramdisk:** Injects the verified recovery ramdisk with Novatek touchscreen drivers (`novatek_ts_*.bin`) and Awinic haptics (`aw869x_haptic.bin`).
3. **Dynamic Hardware Assertion:** `unified-script.sh` automatically configures props so zip installers for `everpal`, `evergo`, `evergreen`, or `opal` install with zero `assert()` errors.
4. **Android 16 Decryption:** Automatically decrypts metadata encryption (`nopassword` stretching key) and provides the interactive touchscreen PIN/Password prompt for FBE v2 Credential Encryption.

---

## 3. Directory Layout

```text
src/cusrec/
├── repack.py                 # Master repacking CLI
├── README.md                 # Technical documentation & multi-device matrix
├── ramdisks/
│   ├── ofox_ramdisk.cpio.gz  # OrangeFox R12.1 Aqua A16 multi-device ramdisk
│   └── twrp_ramdisk.cpio.gz  # TWRP 3.7.1 Aqua A16 multi-device ramdisk
└── tools/
    ├── avbtool               # Android Verified Boot 2.0 signer
    ├── mkbootimg.py          # Android boot image packager
    ├── testkey_rsa2048.pem   # AVB 2.0 RSA-2048 signing key
    └── unpack_bootimg.py     # Android boot image unpacker
```

---

## 4. Usage

### Basic Usage (OrangeFox Default)

```bash
python3 repack.py aosp.img
```
**Output:** `ofox_aosp.img`

---

### Packaging TWRP 3.7.1 (Verified Decryption & Touch)

```bash
python3 repack.py aosp.img --recovery twrp
```
**Output:** `twrp_aosp.img`

---

### Custom Output Destination

```bash
python3 repack.py /path/to/AlphaDroid_BOOT.img -o /path/to/recovery.img
```

---

### Custom Kernel Override (Optional)

```bash
python3 repack.py aosp.img --kernel /path/to/Image.gz
```

---

## 5. Flashing to Any `evergo` Device

Flash the generated image to your device in **Fastboot Mode**:

```powershell
fastboot flash boot_a ofox_aosp.img; fastboot flash boot_b ofox_aosp.img; fastboot erase misc; fastboot reboot recovery;
```
