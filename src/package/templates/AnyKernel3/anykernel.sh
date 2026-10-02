### AnyKernel3 Ramdisk Mod Script
## FronxKernel Project by FrontlXOX
## Root-Only Architecture: ReSukiSU v4.2.0-rc3 + SuSFS v2.3.0

properties() { '
kernel.string=Fronx Kernel for Xiaomi POCO M4 Pro 5G / Redmi Note 11S 5G
do.devicecheck=0
do.modules=0
do.systemless=1
do.cleanup=1
do.cleanuponabort=1
device.name1=everpal
device.name2=evergo
'; }

# boot shell variables
block=boot;
is_slot_device=auto;
ramdisk_compression=auto;
patch_vbmeta_flag=auto;
no_block_display=1;

# import functions/variables and setup patching - see for reference (DO NOT REMOVE)
. tools/ak3-core.sh;

ui_print " "
ui_print "================================================"
ui_print "   F R O N X   K E R N E L   R O O T"
ui_print "================================================"
ui_print " • Target:    Xiaomi POCO M4 Pro 5G (everpal)"
ui_print " • Platform:  MediaTek Dimensity 810 (MT6833P)"
ui_print " • Kernel:    Linux 4.14.357-Fronx PREEMPT SMP"
ui_print " • Variant:   Root Edition (ReSukiSU + SuSFS)"
ui_print " • Author:    FrontlXOX"
ui_print " • Toolchain: ZyC Clang 22.0.0 (LLVM + ThinLTO)"
ui_print " • Date:      @BUILD_DATE@"
ui_print "------------------------------------------------"

# Pre-flight environment diagnostics
ui_print " [i] Pre-flight Environment Inspection..."
SLOT=$(find_slot 2>/dev/null)
if [ -n "$SLOT" ]; then
  ui_print "     -> Active Slot:        $SLOT"
else
  ui_print "     -> Active Slot:        A-only / Single"
fi

DEVICE=$(getprop ro.product.device 2>/dev/null || getprop ro.build.product 2>/dev/null)
[ -n "$DEVICE" ] && ui_print "     -> Target Device:      $DEVICE"

SDK=$(getprop ro.build.version.sdk 2>/dev/null)
REL=$(getprop ro.build.version.release 2>/dev/null)
if [ -n "$REL" ]; then
  ui_print "     -> Android OS:         Android $REL (API $SDK)"
fi

ui_print " "
ui_print " [+] Dumping & splitting boot partition..."
split_boot;

ui_print " [+] Injecting Fronx Kernel (Image.gz)..."
flash_boot;

if [ -f dtb.img ] || [ -f dtbo.img ]; then
  ui_print " [+] Flashing Device Tree overlays..."
  flash_dtbo;
fi

ui_print " "
ui_print "================================================"
ui_print "  [✓] FRONXKERNEL FLASH COMPLETED SUCCESSFULLY!"
ui_print "================================================"
ui_print " Subsystems Status:"
ui_print " • Root Solution:    ReSukiSU v4.2.0-rc3 (Active)"
ui_print " • SuSFS Engine:     v2.3.00 Inline Hooks (Active)"
ui_print " • Stealth Spoofing: Path / Mount / Kstat / Map"
ui_print " • Energy Model:     EAS / Schedutil Optimized"
ui_print " • Memory Profile:   Zone Normal Reclaim Ready"
ui_print " • Interconnect:     CoreLink CCI Uncapped"
ui_print "------------------------------------------------"
ui_print " Please reboot your device to boot FronxKernel!"
ui_print "================================================"
ui_print " "
