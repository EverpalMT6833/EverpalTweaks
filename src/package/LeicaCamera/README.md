# Everpal Leica Camera Port Master Blueprint

> **Prepared By:** Shovit Dutta
> **Author / Tuning:** FrontlXOX
> **Target Device:** Xiaomi POCO M4 Pro 5G / Redmi Note 11S 5G (`everpal`)
> **Hardware:** MediaTek Dimensity 810 (MT6833P / MT6833 family, 2x A76 @ 2.4 GHz + 6x A55 @ 2.0 GHz, Mali-G57 MC2)
> **Kernel & OS:** Linux `4.14.357-Aqua #3` | Android 16 (Project Infinity - `BP4A.251205.006`)
> **Target Repository:** [vendor_xiaomi_camera-everpal](https://github.com/EverpalMT6833/vendor_xiaomi_camera-everpal)
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

### 4. Elimination of 5-Second Mode Changing Delay (`replaceSessionClose()V`)
- In stock HyperOS/MIUI frameworks, Xiaomi added a proprietary non-standard method `replaceSessionClose()V` to `CameraCaptureSessionImpl`. Standard Android 16 AOSP lacks this method.
- When switching camera modes (e.g. Photo to Video or Portrait), the mode switch worker invoked `replaceSessionClose()V`, throwing `java.lang.NoSuchMethodError` inside handler thread `ch.b`.
- The camera device was left in a hanging state until Android CameraService's **5,000ms session abort timeout** elapsed, forcing a 5-second UI freeze.
- **Solution:** Patched `dh/e.smali` and `MockCameraImageReceiver.smali` to invoke standard null-safe `CameraCaptureSession.close()V`. Mode transitions now occur **instantaneously (< 200ms)**.

### 5. Photo Capture Crash & Dalvik Register Verification Fix
- HyperOS v6 relies on proprietary Xiaomi vendor tags embedded in `ICustomCaptureResult`. On pure AOSP, standard capture results lack these vendor extensions.
- In `xf/a.smali`, reflection on `CaptureRequest.getNativeCopy()` failed and returned `null`, while `ba/p1.smali` had an inverted branch condition causing `NullPointerException` on `ICustomCaptureResult.getTimeStamp()`.
- Furthermore, smali local registers clobbered parameter register `p0`, triggering an ART `VerifyError: Verifier rejected class xf.a`.
- **Solution:** Re-implemented `xf.a.a` and `xf.a.b` with strict register allocation (`.locals 8`), fallback to `getNativeMetadata()`, and null-safe branching in `ba.p1` and `o$b`.

### 6. MT6833 Snapshot Burst Memory Protection & LMKD Shielding
- During high-resolution snapshot allocations (4080x3072 = 12.5 MP YUV420 buffers), MediaTek `initMfnrCore` multi-frame noise reduction allocates ~113 MB of contiguous physical memory.
- On MT6833 4GB variants, `Zone Normal` (~374 MB managed) breaches watermarks, causing Android 16 LMKD to escalate kill cycles (`reason: min watermark is breached even after kill`).
- By default, LMKD `ro.lmk.pressure_after_kill_min_score` defaults to 0, which slaughtered the foreground camera app.
- Additionally, kernel `vm.lowmem_reserve_ratio` defaulted to `256 32`, locking 4,626 pages (18.5 MB) out of Zone Normal.
- **Solution:** Configured `ro.lmk.pressure_after_kill_min_score=201` and `ro.lmk.lowmem_min_oom_score=201` to protect foreground camera tasks, and tuned `vm.lowmem_reserve_ratio="256 256"` (freeing 4,048 pages / 16.2 MB for Zone Normal). Zero capture crashes or frame drops.

### 7. MediaTek CPU Auto-Exposure (AE) Fallback (`vendor.debug.ae.stat.type=2`)
- On MediaTek MT6833 / Dimensity 810 under custom AOSP ROMs, the vendor camera HAL default AE statistics path attempted to query missing Xiaomi CCU hardware coprocessor firmware.
- This resulted in uncalibrated, near-zero exposure gains, causing an extremely dark viewfinder preview across all camera modes (Photo, Night, Portrait, Pro).
- **Solution:** Deployed `vendor.debug.ae.stat.type=2` in `system.prop` and `post-fs-data.sh`. This instructs MediaTek's `lib3a.ae.stat.so` 3A engine to bypass the absent CCU coprocessor and compute exposure statistics directly on the CPU. Viewfinder brightness, dynamic range, and ambient exposure calibration are 100% restored.

### 8. Night Mode Surface Target & Shutter Capture Pipeline
- Porting Night Mode (`MODULE_NIGHT` / index `0xad`) previously caused:
  1. `IllegalArgumentException: Each request must have at least one Surface target` (error `0x101` / "Can't connect to camera") when the shutter was pressed, due to Qualcomm raw super night surface requirements and disabled parallel session surface maps.
  2. Stalled capture flow waiting for absent proprietary Xiaomi AlgoUp / Joyose multi-frame DSP blending daemons.
- **Solution:**
  - Patched `NightModule.smali`: diverted `getRawCallbackType()` to return `0` (bypassing Qualcomm RAW callback) and `isParallelSessionEnable()` to return `1` (ensuring 4080x3072 YUV surface is added to session).
  - Patched `Camera2Module.smali`: eliminated the `instance-of NightModule` and `supportFrontOrBackSuperNightAlgoUp` (`g1/w1.F()`) bypasses in `onCaptureStart` and `onShutter`. Both Photo Mode and Night Mode now directly execute the `AnchorPreviewCallbackImpl` -> `saveJpegOrBitmapAsThumbnail` -> `PreviewSaveRequest` -> `Storage.addImage` pipeline.
  - Enabled `NightModuleEntry.support()` returning `1` for clean mode carousel registration.
  - Photos in Night mode now capture instantaneously (~1,000ms end-to-end), encoding crisp 1080x1440 JPEGs with complete EXIF data (`NightScene=1`, `Make=Xiaomi`, `Model=22031116AI`) persisted to `/sdcard/DCIM/Camera/IMG_*.jpg`.

---

## 🛠️ Standalone Flashable Module (`package/LeicaCamera.zip`)

The flashable module is built via `scripts/builder.py --camera` (or `--all`) and can be flashed directly in **KernelSU Manager**, **Magisk**, or **APatch**:

- **Module ID:** `leica-camera-everpal`
- **Module Name:** `Leica Camera HyperOS v6 (Everpal)`
- **Version:** `v6.0.001240.1 (600001)`
- **Author:** `FrontlXOX`

### Flash via ADB:
```bash
adb push src/package/LeicaCamera/package/LeicaCamera.zip /sdcard/Download/
adb shell "su -c 'ksud module install /sdcard/Download/LeicaCamera.zip'"
adb reboot
```
