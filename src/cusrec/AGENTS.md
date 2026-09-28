# AGENTS.md — cusrec Universal Recovery & Dual-Slot Engine

> **Master AI Agent Operational Specification & Hardware Architecture Manual**  
> Subsystem: **`src/cusrec/` — Custom Recovery Repacker & Dual-Slot Boot Engine**  
> Target Device Family: **Xiaomi POCO M4 Pro 5G / Redmi Note 11S 5G (`everpal`, `evergo`, `evergreen`, `opal`)**  
> Target SoC: **MediaTek Dimensity 810 5G (MT6833P / MT6833 family)**  
> Target OS: **Android 16** (AlphaDroid 3.4, Project Infinity, LineageOS 23.0 base)  
> Target Kernel: **Linux 4.14.357-Aqua #3 SMP PREEMPT**  
> Maintainer / Author: **Shovit Dutta (`FrontlXOX`)**  
> Upstream / Device Collaborators: **himanshuksr0007 (Goku / Sudoku)**, **Addster09**

---

## 1. System Identity & Mission

`cusrec` is an automated, hardware-verified custom recovery repacker, dual-slot boot engine, and Android 16 UI optimization suite engineered specifically for the MediaTek Dimensity 810 (`MT6833`) platform.

On modern MediaTek A/B architectures lacking a dedicated hardware `recovery` partition, recovery environments reside directly within the `boot` image (`boot_a` / `boot_b`). `cusrec` resolves the critical challenges inherent to this architecture:
1. **Dynamic Multi-SKU Adaptation:** Dynamically reads bootloader hardware board IDs to configure universal device assertions across all 5 regional commercial variants.
2. **MediaTek BCAB Dual-Slot Engine:** Manipulates the proprietary MediaTek `BCAB` partition table at byte offset 2048 in `/dev/block/by-name/misc`, decoupling slot switching from broken Android 16 user-space HAL commands and eliminating bootloops.
3. **Android 16 FBE v2 Decryption:** Provides interactive PIN/Pattern/Password decryption for File-Based Encryption (FBE v2) and handles metadata key stretching across wiped or newly initialized partitions.
4. **Hardware-Accelerated UI & Squircle Modernization:** Modernizes legacy TWRP UI elements into rounded squircles (Material You design) using thresholded alpha bounding-box algorithms, while avoiding CPU-bound FreeType rendering stalls.

---

## 2. Multi-SKU Universal Hardware Matrix

MediaTek Dimensity 810 hardware is distributed across five distinct commercial models. Different variants feature slight variations in camera sensor buses and display panel timings (KTZ8863A vs Novatek).

`cusrec` achieves **100% universal compatibility** by reading `ro.boot.board_id` directly from the MediaTek Little Kernel (LK) bootloader at runtime via `twres/unified-script.sh`:

| Board ID | Platform Codename | Commercial Branding | Model Number | Primary Market |
| :--- | :--- | :--- | :--- | :--- |
| **`S98016LA1`** | **`everpal`** / `evergo` | **POCO M4 Pro 5G** | `22031116AI` | India |
| **`S98017AA1`** | **`evergreen`** / `everpal` | **POCO M4 Pro 5G** | `21091116AG` | Global |
| **`S98018AA1`** | **`opal`** / `everpal` | **Redmi Note 11S 5G** | `22031116BG` | Global |
| **`S98016AA1`** | **`evergo`** | **Redmi Note 11 5G** | `21091116AC` | China |
| **`S98016BA1`** | **`evergo`** | **Redmi Note 11T 5G** | `21091116AI` | India |

> [!NOTE]
> If an unrecognized or engineering board ID is encountered, `unified-script.sh` automatically falls back to `load_evergreen_g` (the universal global SKU definition). This ensures assertions never fail during zip installations.

---

## 3. Repacker Pipeline & AVB 2.0 Signing (`repack.py`)

The primary CLI orchestrator is `src/cusrec/repack.py`. It guarantees bit-exact hardware synchronization by extracting the native kernel and Device Tree Blob (DTB) from the user's existing AOSP boot image before repacking.

```
                    [ Input AOSP boot.img ]
                               │
                      unpack_bootimg.py
                               │
               ┌───────────────┴───────────────┐
               ▼                               ▼
       [ Kernel Binary ]               [ Device Tree Blob (DTB) ]
       (Image.gz / Aqua)               (Panel / Regulator configs)
               │                               │
               └───────────────┬───────────────┘
                               │
                  + [ Recovery Ramdisk ]
                  (twrp_ramdisk / ofox_ramdisk)
                               │
                          mkbootimg.py
              (Header v2, Page 2048, Base 0x40000000)
                               │
                               ▼
                    [ Repacked boot.img ]
                               │
                            avbtool
             (add_hash_footer: 128 MB Partition Boundary)
             (Algorithm: SHA256_RSA2048 via testkey.pem)
                               │
                               ▼
               [ TwrpBOOT_ResukiSU.img / 128 MB ]
```

### Critical Boot Parameters & Offsets

Repacking strictly enforces MediaTek A/B boot header version 2 parameters:

```python
--base            0x40000000
--kernel_offset   0x00080000
--ramdisk_offset  0x11100000
--tags_offset     0x07c80000
--dtb_offset      0x07c80000
--os_version      16.0.0
--os_patch_level  2026-05
--header_version  2
--pagesize        2048
--cmdline         "bootopt=64S3,32N2,64N2 androidboot.selinux=permissive androidboot.hardware=mt6833 buildvariant=eng"
```

### Cryptographic Signing & Partition Padding
Android 16 bootloaders verify the partition footer against AVB 2.0 (Android Verified Boot). `repack.py` invokes `tools/avbtool add_hash_footer`:
- **Partition Size:** Exactly `134,217,728` bytes (128 MB).
- **Algorithm:** `SHA256_RSA2048` utilizing `tools/testkey_rsa2048.pem`.
- **Zero-Padding Guard:** If `avbtool` output falls short of 128 MB, `repack.py` automatically pads the image with null bytes (`\x00`) to match physical flash block boundaries.

---

## 4. MediaTek MT6833 Dual-Slot Engine & Hardware Traps

### The `/misc` Partition Architecture

Unlike Qualcomm devices that rely on standard AOSP boot control HAL metadata in GPT headers, MediaTek MT6833 utilizes a segmented `/dev/block/by-name/misc` structure:

```
Byte 0                               Byte 2048                              Byte 4096
┌──────────────────────────────────────┬──────────────────────────────────────┬───
│ Standard Android BCB                 │ MediaTek Proprietary BCAB Struct     │ ...
│ (bootloader_message: command[32],    │ (A/B Slot Selection, Priority,       │
│  status[32], recovery[1024])         │  Retry Counts, Boot Flags)           │
└──────────────────────────────────────┴──────────────────────────────────────┴───
```

### The MediaTek BCAB Structure (Offset 2048)

The active boot slot is governed by a 16-byte binary payload located at byte offset **2048**:

| Byte Offset | Size | Purpose | Verified Slot A Payload | Verified Slot B Payload |
| :--- | :--- | :--- | :--- | :--- |
| `2048` | 4 B | Slot Suffix ASCII | `_a\x00\x00` (`0x5F 0x61 0x00 0x00`) | `_b\x00\x00` (`0x5F 0x62 0x00 0x00`) |
| `2052` | 4 B | Magic Header | `BCAB` (`0x42 0x43 0x41 0x42`) | `BCAB` (`0x42 0x43 0x41 0x42`) |
| `2056` | 4 B | Version & Flags | `\x01\x02\x00\x00` | `\x01\x02\x00\x00` |
| `2060` | 2 B | Slot A Priority/State | `\xef\x00` (Active: 239) | `\xee\x00` (Inactive: 238) |
| `2062` | 2 B | Slot B Priority/State | `\x2e\x00` (Inactive: 46) | `\xef\x00` (Active: 239) |

---

### Critical Hardware Traps Discovered & Neutralized

#### 🛑 TRAP 1: The `boot-recovery` Conflict & POCO Bootloop
- **Symptom:** Selecting "Recovery (SLOT B)" triggers an infinite bootloop at the initial POCO splash logo.
- **Root Cause:** When the standard Android recovery flag (`boot-recovery`) is written to byte offset 0, the MT6833 bootloader interprets this as an emergency rescue command and forces an internal fallback path hardcoded to **Slot A**. However, byte offset 2048 simultaneously instructs the bootloader to boot **Slot B**. The bootloader encounters mutually conflicting hardware directives, panics, and crashes before executing the kernel.
- **Neutralization:** On A/B devices where TWRP resides directly in the `boot` partition, **NEVER write `boot-recovery` to offset 0**. All reboot operations unconditionally zero out byte offset 0 (`bs=2048 count=1`), relying exclusively on the BCAB struct at offset 2048 to designate the boot target.

#### 🛑 TRAP 2: TWRP C++ Reboot Hook Tampering
- **Symptom:** Manual modifications to `/dev/block/by-name/misc` are reverted on device reboot, booting back into AOSP (Slot A).
- **Root Cause:** During a graceful shutdown, TWRP's internal C++ recovery process calls `set_bootloader_message()` immediately prior to invoking the `reboot()` syscall, overwriting offset 0 with `boot-recovery`.
- **Neutralization:** Reboot scripts execute a kernel-level hardware restart via the Magic SysRq trigger:
  ```bash
  sync
  echo 1 > /proc/sys/kernel/sysrq
  echo b > /proc/sysrq-trigger
  ```
  This immediately halts user-space execution and reboots the SoC at the kernel level, completely bypassing TWRP's shutdown hooks.

#### 🛑 TRAP 3: Missing XML `<placement>` Tag (Empty Reboot Menu)
- **Symptom:** The Reboot menu in TWRP renders completely blank/empty.
- **Root Cause:** In TWRP's GUI XML parser (`portrait.xml`), `<listbox style="advanced_listbox">` requires an explicit child `<placement>` element. If omitted during XML refactoring, the listbox evaluates to `0x0` dimensions, rendering all menu items invisible.
- **Neutralization:** Ensure `<placement x="%indent%" y="%row2a_y%" w="%content_width%" h="%listbox_advanced_height%"/>` is strictly preserved inside the listbox definition.

---

## 5. Dual-Slot Boot Enforcement & Clean Standard GUI

To prevent users from becoming trapped in a recovery loop or booting an uninitialized slot, TWRP implements an **Enforced AOSP Boot Strategy**:

1. **Clean Standard GUI:** The custom split buttons have been eliminated in favor of TWRP's standard, uncluttered Reboot menu (`System`, `Power Off`, `Recovery`, `Bootloader`, `Fastboot`).
2. **Default AOSP Target:** Every standard reboot action (`Reboot System` and `Reboot Recovery`) as well as unexpected reboots/crashes automatically route to **Slot A (AOSP)**.
3. **Manual Override via Slot Switcher:** Users only boot or reboot into Slot B (TWRP) if they navigate to the Reboot menu and explicitly tap the **`Slot B`** button.

### Automatic AOSP Enforcement on Startup (`system/bin/unified-script.sh`)

On every TWRP boot, `unified-script.sh` automatically arms MediaTek `/misc` offset 2048 to point to Slot A:

```bash
# Auto-clear BCB in misc to guarantee zero boot-recovery loops
dd if=/dev/zero of=/dev/block/by-name/misc bs=2048 count=1 2>/dev/null
dd if=/dev/zero of=/dev/block/platform/bootdevice/by-name/misc bs=2048 count=1 2>/dev/null

# Always arm Slot A (AOSP) by default on TWRP boot
printf "_a\0\0BCAB\x01\x02\0\0\xef\0\x2e\0" | dd of=/dev/block/by-name/misc bs=1 seek=2048 count=16 conv=notrunc 2>/dev/null
rm -f /tmp/manual_slot_selected 2>/dev/null
```

### Manual Slot Override Hook (`system/bin/setslot.sh`)

When the user taps `Slot A` or `Slot B` in the TWRP Reboot menu, `portrait.xml` executes `/system/bin/setslot.sh [A|B]`:

```bash
#!/system/bin/sh
TARGET=$1
if [ "$TARGET" = "B" ] || [ "$TARGET" = "b" ]; then
    echo "B" > /tmp/manual_slot_selected
    dd if=/dev/zero of=/dev/block/by-name/misc bs=2048 count=1 conv=notrunc 2>/dev/null
    dd if=/dev/zero of=/dev/block/platform/bootdevice/by-name/misc bs=2048 count=1 conv=notrunc 2>/dev/null
    printf "_b\0\0BCAB\x01\x02\0\0\xee\0\xef\0" | dd of=/dev/block/by-name/misc bs=1 seek=2048 count=16 conv=notrunc 2>/dev/null
else
    echo "A" > /tmp/manual_slot_selected
    dd if=/dev/zero of=/dev/block/by-name/misc bs=2048 count=1 conv=notrunc 2>/dev/null
    dd if=/dev/zero of=/dev/block/platform/bootdevice/by-name/misc bs=2048 count=1 conv=notrunc 2>/dev/null
    printf "_a\0\0BCAB\x01\x02\0\0\xef\0\x2e\0" | dd of=/dev/block/by-name/misc bs=1 seek=2048 count=16 conv=notrunc 2>/dev/null
fi
sync
exit 0
```

### Pre-Reboot Enforcer Hooks (`system/bin/rebootsystem.sh` & `rebootrecovery.sh`)

When the user executes a reboot in TWRP, the pre-reboot hooks inspect `/tmp/manual_slot_selected`. Unless the user explicitly intervened and tapped `Slot B`, the device unconditionally boots Slot A (AOSP):

```bash
#!/system/bin/sh
MANUAL=$(cat /tmp/manual_slot_selected 2>/dev/null)
if [ "$MANUAL" = "B" ]; then
    # User explicitly selected Slot B
    printf "_b\0\0BCAB\x01\x02\0\0\xee\0\xef\0" | dd of=/dev/block/by-name/misc bs=1 seek=2048 count=16 conv=notrunc 2>/dev/null
else
    # Default: Unconditionally enforce Slot A (AOSP)
    printf "_a\0\0BCAB\x01\x02\0\0\xef\0\x2e\0" | dd of=/dev/block/by-name/misc bs=1 seek=2048 count=16 conv=notrunc 2>/dev/null
fi

dd if=/dev/zero of=/dev/block/by-name/misc bs=2048 count=1 conv=notrunc 2>/dev/null
dd if=/dev/zero of=/dev/block/platform/bootdevice/by-name/misc bs=2048 count=1 conv=notrunc 2>/dev/null

sync
echo 1 > /proc/sys/kernel/sysrq 2>/dev/null
echo b > /proc/sysrq-trigger 2>/dev/null
reboot -f 2>/dev/null
exit 0
```

---

## 6. UI Theming, Rendering Performance & Squircles

### The FreeType CPU Software Rendering Bottleneck
TWRP does not utilize GPU acceleration; all glyphs are rasterized on the CPU via FreeType.
- **The Bug:** Applying heavy fonts (e.g. `IosevkaTermSlabNerdFont-Bold.ttf`, ~14.6 MB) globally across `twres/languages/*.xml` caused catastrophic rendering lag, dropping UI framerates below 5 FPS during scrolling.
- **The Solution:** Lightweight `RobotoCondensed-Regular.ttf` is strictly enforced for dense UI lists, menus, and consoles. Iosevka Nerd Font is reserved exclusively for the static Splash Screen where single-frame rendering occurs.

### Palette Migration (`#006200`)
The entire TWRP visual theme is aligned with the Everpal Emerald Green design language:
- `twres/ui.xml` & `portrait.xml` base color values mapped to `%accent_color% = #006200`.
- All standard OrangeFox/TWRP orange PNG assets hue-shifted to 120° (Green) via `src/cusrec/shift_to_green.py`.
- Splash screen top header color block removed to produce a continuous, seamless dark background.

### Bounding-Box Squircle Masking Algorithm
Original TWRP buttons are rectangular PNGs containing up to 40 pixels of transparent margin padding. A naive corner crop will only mask invisible pixels, leaving the visual button untouched.

The production squircle engine evaluates the **strict alpha bounding box** (`get_solid_bbox(img, threshold=200)`), applies a mathematically anti-aliased squircle mask to the visible pixels, and preserves the outer dimensions:

```python
def get_solid_bbox(img, threshold=200):
    w, h = img.size
    left, top, right, bottom = w, h, 0, 0
    found = False
    for y in range(h):
        for x in range(w):
            if img.getpixel((x, y))[3] > threshold:
                found = True
                if x < left: left = x
                if x > right: right = x
                if y < top: top = y
                if y > bottom: bottom = y
    return (left, top, right + 1, bottom + 1) if found else None

def apply_squircle(img_path):
    img = Image.open(img_path).convert("RGBA")
    bbox = get_solid_bbox(img, threshold=200) or img.getbbox()
    if not bbox: return
    
    left, top, right, bottom = bbox
    bh = bottom - top
    radius = min(48, bh // 3)  # Adaptive corner radius
    
    mask = Image.new("L", img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle((left, top, right - 1, bottom - 1), radius, fill=255)
    
    rounded = Image.new("RGBA", img.size, (0, 0, 0, 0))
    rounded.paste(img, (0, 0), mask)
    rounded.save(img_path)
```

**Assets Squircled:**
- `main_button.png`, `main_button_half_height.png`, `main_button_half_height_full_width.png`
- `slider.png`, `slider_touch.png`, `slider_used.png`
- `tab_*.png` (General, Display, Language, Vibration)
- `kb_*.png` (Full on-screen terminal and search keyboard)
- `checkbox_true.png`, `checkbox_false.png`
- `progress_fill.png`, `progress_empty.png`

---

## 7. Android 16 FBE Decryption & Storage Triage

### Metadata Partition Wipe Edge-Case (`fastboot erase metadata`)
If `/metadata` is formatted or erased via fastboot (`fastboot erase metadata`), the block is physically zeroed:
- TWRP's `blkid` probe fails (`Can't probe device /dev/block/by-name/metadata`).
- Mounting `/metadata` aborts with `Invalid argument` (missing filesystem superblock).
- Decryption aborts because key stretching directories (`/metadata/vold/metadata_encryption`) do not exist.

> [!IMPORTANT]
> Decryption is physically impossible when `/metadata` is unformatted. The user MUST boot the AOSP ROM once to allow Android's `vold` to initialize the ext4 filesystem and write cryptographic headers before TWRP can mount it.

### Kernel Module Mount Masking
TWRP dynamically mounts a `tmpfs` over `/vendor/lib/modules` during startup. Kernel log warnings stating `Unable to open module directory: /vendor/lib/modules` are cosmetic and do not impact storage, touch, or decryption subsystems.

---

## 8. Directory Catalog & Tooling Reference

All scripts and packaging assets reside in `src/cusrec/`:

```text
src/cusrec/
├── AGENTS.md                  # Master technical specification (This file)
├── README.md                  # Public overview and flashing instructions
├── repack.py                  # Primary AOSP-to-Recovery packaging CLI
├── shift_to_green.py          # HSV color-space hue shifter (Orange -> #006200)
├── modernize_ui.py            # XML styling and font configuration patcher
├── generate_buttons.py        # Programmatic squircle button generator
├── generate_sliders.py        # Programmatic squircle slider generator
├── generate_checkboxes.py     # Programmatic squircle checkbox generator
├── generate_progress.py       # Programmatic squircle progress bar generator
├── apply_ofox_theme.py        # OrangeFox R12.1 theme applicator
├── ramdisks/
│   ├── twrp_ramdisk.cpio.gz   # Production TWRP 3.7.1 Aqua A16 ramdisk
│   └── ofox_ramdisk.cpio.gz   # Production OrangeFox R12.1 Aqua A16 ramdisk
└── tools/
    ├── avbtool                # Android Verified Boot 2.0 utility
    ├── mkbootimg.py           # Android boot image assembler
    ├── unpack_bootimg.py      # Android boot image disassembler
    └── testkey_rsa2048.pem    # AVB 2.0 RSA-2048 cryptographic signing key
```

---

## 9. Developer & Agent Operational Workflows

### Repacking TWRP with a Custom Kernel
```bash
python3 src/cusrec/repack.py out/AlphaDroid_3.4_ResukiSU.img \
    --recovery twrp \
    -k out/ImageResukiSU.gz \
    -o /mnt/c/Users/psycosis/Downloads/TwrpBOOT_ResukiSU.img
```

### Inspecting Ramdisk Internals
```bash
mkdir -p /tmp/twrp_inspect && cd /tmp/twrp_inspect
gzip -dc /root/Everpal/src/cusrec/ramdisks/twrp_ramdisk.cpio.gz | cpio -idm
```

### Re-compressing Ramdisk After Edits
```bash
cd /tmp/twrp_inspect
find . | cpio -o -H newc | gzip > /root/Everpal/src/cusrec/ramdisks/twrp_ramdisk.cpio.gz
```

### Flashing via Fastboot (Dual-Slot Flashing)
```powershell
fastboot flash boot_a TwrpBOOT_ResukiSU.img; fastboot flash boot_b TwrpBOOT_ResukiSU.img; fastboot erase misc; fastboot reboot recovery;
```
