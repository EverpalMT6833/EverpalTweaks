# Everpal Leica Camera Port Master Blueprint

> **Prepared By:** Shovit Dutta
> **Author / Tuning:** FrontlXOX x himanshuksr0007 (Goku)
> **Target Device:** Xiaomi POCO M4 Pro 5G / Redmi Note 11S 5G (`everpal`)
> **Hardware:** MediaTek Dimensity 810 (MT6833P / MT6833 family, 2x A76 @ 2.4 GHz + 6x A55 @ 2.0 GHz, Mali-G57 MC2)
> **Kernel & OS:** Linux `4.14.357-Aqua #3` | Android 16 (Project Infinity - `BP4A.251205.006`)
> **Target Repository:** [vendor_xiaomi_camera-everpal](https://github.com/FrontlXOX/vendor_xiaomi_camera-everpal)
> **Flashable Module:** `package/LeicaCamera/package/LeicaCamera.zip`

---

## 📱 Device & Operating System Specifications

| Specification          | Hardware & Software Configuration                                             |
| :--------------------- | :---------------------------------------------------------------------------- |
| **Commercial Device**  | Xiaomi POCO M4 Pro 5G / Redmi Note 11S 5G (`everpal`)                          |
| **Model Identifier**   | `Xiaomi 22031116AI` (Motherboard: `everpal`, Board ID: `S98016LA1`)           |
| **Operating System**   | **Android 16** (Project Infinity - LineageOS 23.0 Base)                       |
| **Android Build ID**   | `BP4A.251205.006 release-keys` (`eng.androi.20260917.074937`)                 |
| **Security Patch**     | September 1, 2026                                                             |
| **Kernel Version**     | Linux `4.14.357-Aqua #3 SMP PREEMPT` (AArch64, Android Clang 18)              |
| **SoC / Platform**     | MediaTek Dimensity 810 5G (MT6833P / MT6833 family, 6nm TSMC Process)         |
| **CPU Architecture**   | Octa-core: 2x Cortex-A76 @ 2.40 GHz (Big) + 6x Cortex-A55 @ 2.00 GHz (LITTLE) |
| **GPU Architecture**   | ARM Mali-G57 MC2 @ 950 MHz - 1068 MHz (Valhall v1, 2 Shader Cores)           |
| **Camera Sensor**      | OmniVision OV50C / Samsung S5KJN1 50MP + 8MP Ultra-Wide                       |
| **Root Environment**   | KernelSU (`ksud 4.2.0-rc1` / v1.0.5) + Zygisk / SELinux Enforcing             |

---

## 📁 Repository Layout & File Catalog

```text
src/package/LeicaCamera/
├── README.md                      # Comprehensive master technical manual & architecture guide
├── patch.patch                    # Unified git patch for vendor_xiaomi_camera-everpal
│
├── package/                       # Production flashable KernelSU / Magisk module
│   └── LeicaCamera.zip            # Root flashable module (Author: FrontlXOX)
│
└── docs/                          # Architectural blueprint & integration guide
    └── leica-camera.txt           # Master blueprint (JNI mapping, ABI fixes, permissions)
```

---

## ⚡ Technical Deep Dive: Packaging Bugs & Fixes

### 1. The Fatal ABI Path Packaging Bug (`lib/arm64/` vs `lib/arm64-v8a/`)
In stock and raw modified camera APKs, the algorithm stub library `libcamera_algoup_jni.xiaomi.so` was packaged inside `lib/arm64/`.
- Android Package Manager strictly scans for standard ABI directories: `lib/arm64-v8a/`, `lib/armeabi-v7a/`, `lib/x86_64/`.
- Any library under `lib/arm64/` is silently ignored and never extracted by Android's package installer.
- When `com.android.camera` launched, `MiCamAlgoInterfaceJNI` attempted `System.loadLibrary("camera_algoup_jni.xiaomi")`, crashing immediately with:
  ```txt
  java.lang.UnsatisfiedLinkError: dlopen failed: library "libcamera_algoup_jni.xiaomi.so" not found
  ```
- **Solution:** Extracted, sanitized, and relocated `libcamera_algoup_jni.xiaomi.so` into `lib/arm64-v8a/` alongside all native engine binaries.

### 2. Stub Signature Stripping & Full Scheme Re-signing
- The donor APK contained a mock test certificate (`CN=Weather Stub`) signed with v3 only.
- Trying to install or update over existing `com.android.camera` packages caused `INSTALL_FAILED_UPDATE_INCOMPATIBLE`.
- **Solution:** Stripped all `META-INF/STUB.*` signatures, 4-byte/16KB aligned all uncompressed entries with `zipalign -p -f 4`, and signed the package with a dedicated `CN=MiuiCamera, OU=Everpal, O=Everpal` key using v1, v2, and v3 schemes.

### 3. MediaTek MT6833 Algorithm Stubbing
- Stock HyperOS camera expects Xiaomi's proprietary background daemon (`mivi` / `misys`) and hardware HAL callbacks.
- The bundled `libcamera_algoup_jni.xiaomi.so` provides full no-op stubs for:
  - `init`, `deInit`, `getVersionCode`
  - `createSessionWithSurfaces`, `createSessionByOutputConfigurations`
  - `processFrame`, `processFrameWithSync`, `preProcess`, `quickFinish`
  - `flush`, `destroySession`, `dumpGcov`, `setMiViInfo`
- This allows the camera UI, viewfinder, and capture pipeline to function cleanly on pure AOSP.

---

## 🛠️ Standalone Flashable Module (`package/LeicaCamera.zip`)

The flashable module is built via `scripts/builder.py --camera` (or `--all`) and can be flashed directly in **KernelSU Manager**, **Magisk**, or **APatch**:

- **Module ID:** `leica-camera-everpal`
- **Module Name:** `Leica Camera HyperOS v6 (Everpal)`
- **Version:** `v6.0.001240.1 (600001)`
- **Author:** `FrontlXOX x himanshuksr0007 (Goku)`

### Flash via ADB:
```bash
adb push src/package/LeicaCamera/package/LeicaCamera.zip /sdcard/Download/
adb shell "su -c 'ksud module install /sdcard/Download/LeicaCamera.zip'"
adb reboot
```
