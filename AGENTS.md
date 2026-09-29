# AGENTS.md — EverpalTweaks Optimization Suite

> **AI Agent Context & Master Operational Specification for EverpalTweaks**
> Target Device: **Xiaomi POCO M4 Pro 5G / Redmi Note 11S 5G (`everpal`)**
> Target SoC: **MediaTek Dimensity 810 5G (MT6833P / MT6833 family)**
> Target OS: **Android 16** (Project Infinity / LineageOS 23.0 base)
> Target Kernel: **Linux 4.14.357-Aqua #3 SMP PREEMPT**
> Primary Remote: `https://github.com/FrontlXOX/EverpalTweaks`

---

## 1. Project Purpose & System Identity

**EverpalTweaks** is an empirically audited, hardware-verified optimization suite developed to resolve custom ROM performance degradation, thermal throttling, and aggressive background process termination on the Xiaomi POCO M4 Pro 5G / Redmi Note 11S 5G (`everpal`).

This repository maintains four production-grade subsystems:

1. **`MemoryMgmt/`** — Resolves MT6833 `Zone Normal` memory exhaustion, tunes Android 16 LMKD watermarks, and scales ZRAM to 3.58 GB LZ4 for zero direct reclaim stalls and 100% background app retention.
2. **`ThermalMgmt/`** — Decrypts Xiaomi OpenSSL AES-128-CBC thermal profiles, decouples thermal regulation from missing proprietary `joyose`, maps `sconfig 10` (NoLimits profile with 55°C headroom), and uncaps Cortex-A76 Big cores (2.4 GHz) and Mali-G57 GPU clocks.
3. **`Vulkan13/`** — Hybrid decoupled graphics stack deploying HyperOS 3.0 Valhall r49p1 Vulkan 1.3 ICD, companion linker shims (`libgpd1.so`, `libge2.so`), and certified Android 15/16 HAL manifests.
4. **`SpatialAudio/`** — Eliminates wired headset spatial audio routing storms, serializes `immersive_out` mixPort concurrency (`maxOpenCount=1 maxActiveCount=1`), decouples Dolby DAP stream postprocessing, disables speaker spatializer and headtracking loops, and bypasses missing MTK parameter queries.

### Authorship & Collaborator Attribution

- **Author & Maintainer:** Shovit Dutta
- **Special Thanks & Collaborators:**
  - **Android 16 Bringup & Submodule Repos:** himanshuksr0007 (Goku / Sudoku) ([`device_xiaomi_everpal`](https://github.com/himanshuksr0007/device_xiaomi_everpal), [`vendor_xiaomi_everpal`](https://github.com/himanshuksr0007/vendor_xiaomi_everpal), [`android_kernel_xiaomi_mt6833`](https://github.com/himanshuksr0007/android_kernel_xiaomi_mt6833), [`vendor_xiaomi_camera-everpal`](https://github.com/himanshuksr0007/vendor_xiaomi_camera-everpal))
  - **Upstream Device & Kernel Maintainer:** Addster09 ([`device_xiaomi_everpal`](https://github.com/xiaomi-mt6833-dev/device_xiaomi_everpal), [`vendor_xiaomi_everpal`](https://github.com/xiaomi-mt6833-dev/vendor_xiaomi_everpal), [`android_kernel_xiaomi_mt6833`](https://github.com/Addster09/android_kernel_xiaomi_mt6833))
- **Flashable Module Author (`module.prop` metadata):** `FrontlXOX`

---

## 2. Hardware & Operating System Specifications

| Component             | Technical Specification                                                                  |
| :-------------------- | :--------------------------------------------------------------------------------------- |
| **Commercial Device** | Xiaomi POCO M4 Pro 5G / Redmi Note 11S 5G                                                |
| **Model Number**      | `Xiaomi 22031116AI` (Board: `everpal`, Board ID: `S98016LA1`, SKU: `India`)              |
| **Platform / SoC**    | MediaTek Dimensity 810 5G (MT6833P / MT6833 family, TSMC 6nm process)                    |
| **CPU Topology**      | Octa-core: 2x Cortex-A76 @ 2.40 GHz (Big) + 6x Cortex-A55 @ 2.00 GHz (LITTLE)            |
| **GPU Architecture**  | ARM Mali-G57 MC2 @ 950 MHz - 1068 MHz (Valhall v1, 2 Shader Cores)                       |
| **Physical Memory**   | 4.00 GB LPDDR4X (Samsung KM5P9001DM-B424 uMCP, Kernel MemTotal: ~3.53 GB / 3,709,888 kB) |
| **Internal Storage**  | 64 GB UFS 2.2 (Samsung KM5P9001DM-B424 uMCP, ~48 GB User Data Partition)                 |
| **Display Panel**     | 6.6" 90Hz FHD+ IPS LCD (1080 x 2400, 399 PPI, 11-bit PWM brightness 0-2047, KTZ8863A)    |
| **Operating System**  | Android 16 (Project Infinity - LineageOS 23.0 Base)                                      |
| **Android Build ID**  | `BP4A.251205.006 release-keys` (`eng.androi.20260917.074937`)                            |
| **Security Patch**    | September 1, 2026                                                                        |
| **Kernel Version**    | Linux `4.14.357-Aqua #3 SMP PREEMPT` (AArch64, Android Clang 18)                         |
| **Root Environment**  | KernelSU (`ksud 4.2.0-rc1` / v1.0.5) + Zygisk / SELinux Enforcing                        |

---

## 3. Core Subsystems & Technical Deep Dives

### A. Memory Subsystem (`MemoryMgmt/`)

##### The MT6833 Memory Zone Bottleneck

On the 4GB MT6833/MT6833P architecture, physical RAM is segmented into three kernel memory zones:

1. `Zone DMA`: ~2,670 MB managed (683,696 pages, general DMA & bulk user memory)
2. `Zone Normal`: **~374.00 MiB managed** (95,744 pages) | **432.00 MiB spanned** (110,592 pages / 442.37 MB decimal)
3. `Zone Movable` (CMA): ~578 MB managed (148,032 pages reserved for camera/multimedia allocations)
   _Total managed: 927,472 pages (3,709,888 kB / ~3.53 GB Linux MemTotal from 4GB physical LPDDR4X)._

> **Mathematical Distinction:**
>
> - **Spanned Range:** `110,592 pages` = `442,368 KB` = **`432.00 MiB`** (binary) / **`442.37 MB`** (decimal).
> - **Managed Pages:** `95,744 pages` = `382,976 KB` = **`374.00 MiB`** (binary) / **`382.98 MB`** (decimal).
>   Previous diagnostic references cited either the total physical spanned space (~442MB) or post-reservation managed pages (~374MB).

**The Failure Mechanism:** Default AOSP configurations utilize high watermark multipliers (`watermark_scale_factor = 100` to `200`). Because `Zone Normal` is physically restricted to only ~374 MiB managed, inflated watermarks force `Zone Normal` into persistent `low watermark is breached` states under moderate app loading—even when `Zone DMA` has over 850 MB of completely free, unfragmented physical RAM. This triggers Android 16's Low Memory Killer Daemon (`lmkd`) to aggressively kill background launchers, media players, and browser processes.

#### Production Solution & Tunables

Applied via `src/package/MemoryMgmt/patch.patch` (`device_xiaomi_everpal`) and `src/package/MemoryMgmt/package/MemoryMgmt.zip`:

- **Adaptive ZRAM Scaling:** Scaled dynamically to 100% of MemTotal on 4GB variants (**3.58 GB** / `3,758,096,384` bytes) and 75% of MemTotal on 6GB (~4.2 GB) and 8GB (~5.6 GB) variants using single-pass `lz4` compression with dynamic `max_comp_streams = $(nproc)` (8 parallel streams).
- **Watermark Factor:** Scaled down to `vm.watermark_scale_factor = 20` (prevents false-positive direct reclaim storms across all zones).
- **Proportional Atomic Headroom:** `vm.min_free_kbytes` dynamically calibrated by RAM tier: `24,576 KB` (4GB), `32,768 KB` (6GB), or `40,960 KB` (8GB).
- **Adaptive Process Pools:** `bg_apps_limit` scales dynamically: 64 cached (4GB), 96 cached (6GB), 128 cached (8GB).
- **Memory Compaction:** `vm.compact_memory = 1` armed at boot.
- **Kernel VM Swappiness:** `vm.swappiness = 80`, `vm.vfs_cache_pressure = 80`.
- **LMKD Threshold:** `ro.lmk.swap_free_low_percentage = 2` (dynamic 2% emergency reserve floor, preventing premature app murders when swap space is abundant).

---

### B. Thermal Subsystem (`src/package/ThermalMgmt/`)

#### The Xiaomi Joyose Dependency & AES-128-CBC Cipher

Xiaomi MT6833 stock firmware relies on `mi_thermald` interacting with a proprietary MIUI/HyperOS daemon: `com.xiaomi.joyose`. In pure AOSP and custom ROMs, `joyose` is absent. Consequently:

- `mi_thermald` defaults permanently to profile `0` (`thermal-normal.conf`).
- All vendor thermal configurations located in `/vendor/etc/` are encrypted using OpenSSL **AES-128-CBC** with static key and IV defined in `thermalopenssl.h`: **`b"thermalopenssl.h"`** (16 bytes ASCII).
- Reverse engineering of decrypted `thermal-normal.conf` revealed that Xiaomi begins aggressive CPU and GPU throttling at an absurd **36°C** (normal human skin temperature). Cortex-A76 Big cores drop to 1.4 GHz at 44°C, and GPU clocks throttle at 41°C.

#### Production Solution (`sconfig 10` & Hardware Compute Master v2.4)

Applied via `src/package/ThermalMgmt/patch.patch` and `src/package/ThermalMgmt/package/ThermalMgmt.zip`:

- Enforces `sconfig 10` (`thermal-mgame.conf` / `thermal-nolimits.conf`), shifting the thermal throttling ceiling from **36°C to 55°C**.
- Below 55°C, thermal governor applies zero throttling, allowing Cortex-A76 Big Cores to pin at sustained **2.40 GHz** and Cortex-A55 to pin at **2.00 GHz**. The `862000` / `898000` kHz targets in `thermal-nolimits.conf` represent the safety floor _only if_ temperatures breach 55°C.
- Enforces and hardware-locks CoreLink CCI Perf mode at **1.60 GHz** (OPP 0) via `chmod 444`, preventing non-root Android Power HAL (`android.hardware.power-service.mediatek`) from downgrading interconnect and L3 cache bandwidth.
- Hardware-locks ARM Mali-G57 MC2 DVFS evaluation period to **50ms** (via `chmod 444`) with `always_on` power policy and MediaTek GED GPU acceleration up to 1.068 GHz.
- Eliminates CPU Schedutil ramp latency (`up_rate_limit_us = 0`), unlocks both Big cores for foreground (`cpuset 0-7`), configures BORE big task rotation, and preserves natural 8-core DynamIQ task distribution across all 6 Little cores and 2 Big cores.
- Optimizes UFS 2.2 flash storage dispatch via 512 kB read-ahead and zero I/O accounting CPU overhead (`iostats = 0`).
- Hardens network and Wi-Fi ADB connection stability by disabling TCP slow start after idle (`tcp_slow_start_after_idle = 0`) and calibrating 60-second keepalives.

#### Critical Hardware Traps Discovered & Neutralized

1. 🛑 **TRAP 1 (`sconfig 14`):** Profile 14 is the hardcoded YouTube low-power profile. Enforcing profile 14 clamps Big CPU cores to 1.2 GHz and locks refresh rate to 60Hz. Never map profile 14.
2. 🛑 **TRAP 2 (`set_sspm_big_limit_threshold`):** Writing temperature thresholds directly to `/proc/driver/thermal/set_sspm_big_limit_threshold` triggers an unkillable 84% CPU kernel IPI spinloop. Never write to this sysfs node.
3. 🛑 **TRAP 3 (`mtk-cl-backlight`):** Altering or overriding the `mtk-cl-backlight` cooling device in thermal configs forces the display PWM controller to 0, resulting in a black screen upon locking/unlocking the device. Backlight cooling limits MUST remain at state `0` (unrestricted).

---

### C. Graphics & Vulkan Subsystem (`src/package/Vulkan13/`)

#### The Split-Driver Synchronization Problem

ARM Mali GPUs require strict synchronization between the user-space driver (`vulkan.mali.so`, `libGLES_mali.so`) and the kernel device driver (`/dev/mali0` — `mali_kbase`). Directly replacing stock `libGLES_mali.so` with newer DDK binaries crashes SurfaceFlinger due to mismatched IOCTL command structures.

#### Production Solution: Hybrid Decoupling

- **Dual-Stack Decoupling:** Stock `libGLES_mali.so` (r32p1) handles SurfaceFlinger and system GLES rendering, while a standalone **Valhall r49p1 Vulkan 1.3 ICD** (`libVK13_mali.so`) extracted from **Redmi Note 13 5G (`gold`)** on **HyperOS 3.0** (`OS3.0.10.0.VNQCNXM_15.0`) serves Vulkan 1.3 workloads.
- **Linker Hooks & AFBC:** Companion library `libgpd1.so` patched to export missing `GpuAuxBlitAHardwareBuffer` via bit-exact Bionic GnuHash; donor `libged.so` integrated; Arm Generic Timer calibrated to 13 MHz (`PLATFORM_AGT_FREQUENCY_KHZ=13000`); Gralloc AFBC manifests deployed.
- **Mali-G57 Architecture Truth:** Mali-G57 (Valhall v1) uses the **Job Manager (JM)** interface (`BASE_UK_VERSION_MAJOR 11`), **NOT** CSF. Shader and pipeline compilation runs 100% in user-space, delivering full performance on Linux 4.14 without kernel bottlenecks.
- **Kernel Compilation Shims for 4.14:** When backporting 5.10 `mali_kbase`, porters must shim `access_ok(VERIFY_READ, addr, size)` (3 args vs 2 args in 5.0+), retain legacy ION buffer allocator (`mali_kbase_mem_linux.c`), guard modern `dma_fence_set_deadline()`, and port `platform/mt6833/` glue from `mali-r32p1`.

---

### D. Spatial Audio Subsystem (`src/package/SpatialAudio/`)

#### The Routing Storm & HAL Misalignment
On Android 16, connecting wired headsets triggered an aggressive create/releaseAudioPatch loop (~20 round-trips/min) and Downmix_Configure errors. Root causes:
1. `immersive_out` mixPort lacked `maxOpenCount="1" maxActiveCount="1"`, allowing MT6359 accdet debounce chatter to open multiple concurrent spatializer streams.
2. Global Dolby DAP and volume listeners attached to the `AUDIO_OUTPUT_FLAG_SPATIALIZER` thread, which AudioFlinger rejects.
3. Android `SpatializerHelper` attempted to register the mono speaker amp (sia81xx/AW87389) as an HRTF spatial device, spinning a 43-second sensor discovery loop due to missing head-tracking HAL.
4. MediaTek audio HAL crashed trying to calibrate missing ultrasound proximity hardware (`ro.vendor.audio.us.proximity=true`).

#### Production Solution
Applied via `src/package/SpatialAudio/patch.patch` and `src/package/SpatialAudio/package/SpatialAudio.zip`:
- Enforces `maxOpenCount="1" maxActiveCount="1"` on `immersive_out` and adds `5POINT1` / `7POINT1` channel masks.
- Decouples Dolby DAP / DVL into per-session stream postprocessors (`music`, `ring`, `alarm`, `notification`, `voice_call`), keeping the spatializer thread clean.
- Sets `persist.vendor.audio.spatializer.speaker_enabled=false`, `ro.audio.spatializer.headtracking_supported=false`, `ro.audio.monitorRotation=false`, and `ro.vendor.audio.us.proximity=false`.
- Enables `ro.audio.spatializer.use_legacy_param_query=true` to handle MTK spatializer HAL query fallback.
- Injects `allow hal_audio_default vendor_default_prop` SELinux permissions.

---

## 4. Empirical Benchmark Records & Baselines

These verified numbers represent the ground truth performance achievable with this repository:

| Benchmark                     |   Pure Stock AOSP   | Memory Management Alone | EverpalTweaks (Thermal + Memory Management) | Verified Deltas                                   |
| :---------------------------- | :-----------------: | :---------------------: | :----------------------------------------: | :------------------------------------------------ |
| **Geekbench 7 Multi-Core**    |       `1,500`       |         `1,788`         |                **`2,133`**                 | 🚀 **+42.2% (+633 pts — Global MT6833 Record)**   |
| **Geekbench 7 Single-Core**   |        `610`        |          `578`          |                 **`729`**                  | 🚀 **+19.5% (+119 pts — Global MT6833 Record)**   |
| **3DMark Sling Shot Extreme** |       `2,518`       |            —            |                **`2,736`**                 | 🚀 **+8.7% All-Time Global MT6833 Record**        |
| **3DMark Physics (Vulkan)**   |       `3,379`       |            —            |                **`4,053`**                 | 🚀 **+20.0% (+674 pts — World Record Physics)**   |
| **Geekbench 7 GPU (Compute)** |      ~`1,080`       |            —            |                **`1,302`**                 | 🚀 **+20.6% (Mali-G57 MC2 @ 1068 MHz GED Boost)** |
| **Direct Reclaim Stalls**     |      ⚠️ Severe      |         🛡️ None         |       🛡️ **Zero Allocation Stalls**        | `direct_reclaim = 0`                              |
| **App Retention**             | ❌ Aggressive Kills |   ✅ 100% Kept Alive    |           ✅ **100% Kept Alive**           | Retains Chrome tabs, music, launcher in ZRAM      |

- **Official Geekbench 7 Verification (Side-by-Side vs Stock Baseline):** [https://browser.geekbench.com/v7/cpu/compare/400164?baseline=380539](https://browser.geekbench.com/v7/cpu/compare/400164?baseline=380539) | **GPU Compute Compare:** [https://browser.geekbench.com/v7/gpu/compare/183548?baseline=183548](https://browser.geekbench.com/v7/gpu/compare/183548?baseline=183548) (All-Time Record Runs: [400164 — 2133 MC](https://browser.geekbench.com/v7/cpu/400164) / [392815 — 2108 MC](https://browser.geekbench.com/v7/cpu/392815) / [391841 — 729 SC](https://browser.geekbench.com/v7/cpu/391841) / [389858 — 728 SC](https://browser.geekbench.com/v7/cpu/389858) / [385213 — 2066 MC](https://browser.geekbench.com/v7/cpu/385213) | GPU OpenCL Record: [183548 — 1302 pts](https://browser.geekbench.com/v7/gpu/183548))
- **3DMark Sling Shot Extreme Official Runs:** OpenGL ES 3.1: **`2,736 pts`** (Graphics: **`2,557 pts`**, GT1: 17.30 FPS, GT2: 8.19 FPS) | Vulkan: **`2,734 pts`** (Physics: **`4,053 pts`** World Record, GT1: 17.00 FPS, GT2: 7.99 FPS).
- **Sustained Cortex-A76 Big Clocks:** `2,393 MHz` (~2.39 GHz pinned throughout compute runs).
- **Sub-Workload Highlights (Single-Core — Peak 729 SC World Record Run 391841):**
  - HTML5 Browser: **802** | Navigation: **972** | PDF Viewer: **970** | Audio Encoder: **891** | File Compression: **863** | Asset Compression: **849** | Ray Tracer: **735**
- **Sub-Workload Highlights (Multi-Core — Peak 2108 MC World Record Run 392815):**
  - Ray Tracer: **3,403** | Asset Compression: **3,246** | Text Processing: **2,159** | File Compression: **2,015** | Clang: **1,943** | Photo Library: **1,872**
- **Sub-Workload Highlights (GPU Compute — Peak 1302 pts Run 183548):**
  - Horizon Detection: **2,466** | Fluid Simulation: **1,687** | Photo Filter: **1,644** | Particle Physics: **1,528** | Video Filter: **1,454** | RAW: **1,444**

---

## 5. Repository Layout & File Catalog

All required automation and operational Python/Bash scripts reside **exclusively** in `src/scripts/`:

```text
EverpalTweaks/
├── AGENTS.md                          # Master context & AI operational instructions (This file)
├── README.md                          # Public repository overview & quickstart guide
├── CHANGELOG.md                       # Comprehensive version history & benchmark progression
├── LICENSE                            # Apache 2.0 License
├── .gitignore                         # Build outputs, temporary files, and platform artifacts
│
└── src/
    ├── scripts/                       # 🛠️ Centralized Repository Automation Tooling
    │   ├── autobench.py               # Automated Geekbench 7 (CPU + GPU Vulkan) suite with real-time CLI telemetry
    │   ├── benchpull.py               # Automated ADB extractor for Geekbench 7 & 3DMark Sling Shot Extreme DBs
    │   ├── builder.py                 # Unified master module packager & CRC-32 validator (--all, --memory/-m, --thermal/-t, --vulkan/-v, --spatial/-s, --kernel/-k, --dtbo/-d, --blobs/-b)
    │   ├── decouple_libge2.py         # Vulkan 1.3 one-shot binary patch: DT_NEEDED libged.so -> libge2.so
    │   ├── decrypt_thermal.py         # Xiaomi OpenSSL AES-128-CBC encryption/decryption CLI
    │   ├── dumpboot.py                # ROM boot.img extractor (boot.img direct or payload.bin)
    │   ├── brompull.py                # BROM evidence pull helper (see §9; host twin lives in EvergoBROM/)
    │   ├── win2wsl.py                 # Host<->WSL path/file shuttle helper
    │   ├── synctrees.py               # Automated tree synchronizer for GitHub (FrontlXOX)
    │   └── verifydevice.py            # Live ADB hardware, Vulkan 1.3, frequency & kernel parameter audit CLI
    │
    ├── trees/                         # 🌲 Submodule Trees (himanshuksr0007 & FrontlXOX)
    │   ├── device/
    │   │   ├── mediatek/sepolicy_vndr/ # FrontlXOX vendor sepolicy tree (lineage-23.0)
    │   │   └── xiaomi/everpal/         # himanshuksr0007 device tree (lineage-23.2)
    │   ├── hardware/
    │   │   ├── mediatek/               # FrontlXOX MTK hardware HAL (lineage-23.0)
    │   │   └── xiaomi/                 # FrontlXOX Xiaomi hardware HAL (lineage-23.0)
    │   ├── kernel/
    │   │   └── xiaomi/mt6833/          # Fronx Linux 4.14 kernel (vanilla: lineage-24 = Aqua V3.4; overlay: FronxKernel thin branch)
    │   ├── kernel-5.10/                # 5.10 port tree (branch muse_evergo) — see §9 Linux 5.10 Bringup
    │   └── vendor/
    │       ├── mediatek/ims/           # FrontlXOX MTK IMS vendor blobs (android-16-qpr2)
    │       ├── xiaomi/camera/          # himanshuksr0007 MIUI camera vendor blobs (lineage-23.2)
    │       └── xiaomi/everpal/         # himanshuksr0007 vendor blobs (lineage-23.2)
    │
    ├── modules/                       # 📲 Third-Party Companion Modules (Sanctioned Rule 4 Exception)
    │   ├── *.zip                      # Curated flashable companions (numbered: MagicMountRS, ZygiskNext, ZygiskAssistant, Detach, LSPosed, ReMalwack, HideNavBar, GSFCertFix)
    │   ├── Kaeru/                     # Kaeru flash tooling (flash.sh + version-9/10.bin)
    │   └── ResukiSU/                  # ReSukiSU repack tooling (main.py + python/ avb/mkbootimg helpers)
    │
    └── package/                       # 📦 Flashable Subsystems & Packaging Assets
        ├── templates/                 # Shared Magisk, KernelSU & AnyKernel3 packaging templates
        │   ├── AnyKernel3/            # Base AnyKernel3 flashable zip packaging assets
        │   ├── META-INF/              # Generic Magisk update-binary stubs
        │   ├── SpatialAudio/          # Spatial Audio configuration overlays
        │   └── Vulkan13/              # Hybrid ICD stack, companion libraries & SELinux scripts
        │
        ├── MemoryMgmt/                # 🧠 RAM & LMKD Architecture Subsystem
        │   ├── README.md              # Comprehensive technical manual & QA zone math audit
        │   ├── patch.patch            # Unified diff for device_xiaomi_everpal
        │   ├── package/
        │   │   └── MemoryMgmt.zip     # Flashable module (Author: FrontlXOX)
        │   └── docs/                  # Architectural blueprint & integration guide
        │       └── memory-mgmt.txt    # Master blueprint, LMKD tuning logic & git diffs
        │
        ├── ThermalMgmt/               # 🔥 Thermal Mitigation & mi_thermald Subsystem
        │   ├── README.md              # Hardware audit, decrypted Xiaomi profiles & profile tables
        │   ├── patch.patch            # Unified diff for device and vendor trees
        │   ├── package/
        │   │   └── ThermalMgmt.zip    # Flashable module (Author: FrontlXOX)
        │   └── docs/                  # Benchmark logs, databases & vendor configs
        │       ├── benchmark_history.txt     # Chronological benchmark log
        │       ├── fm_local_results.db       # Raw SQLite database from 3DMark Sling Shot Extreme
        │       ├── history.db                # Raw SQLite database pulled from Geekbench 7
        │       ├── thermal-mgmt.txt          # Master thermal analysis & register teardown
        │       └── vendor_configs/           # Raw .conf & decrypted AES .decrypted.txt Xiaomi thermal profiles
        ├── Vulkan13/                  # 🎮 Vulkan 1.3 Hybrid Engine Subsystem
        │   ├── README.md              # Hardware audit, linker hooks & benchmark records
        │   ├── patch.patch            # Unified diff for device and vendor trees
        │   ├── package/
        │   │   └── Vulkan13-KernelSU.zip  # Flashable module — overlay-only OR kernel+overlay combo (Author: FrontlXOX)
        │   └── docs/                  # Architectural blueprint & vendor configuration guide
        │       └── vulkan-mgmt.txt    # Master Vulkan 1.3 hybrid architecture document
        │
        └── SpatialAudio/             # 🎧 Spatial Audio Routing & Hardware Constraint Subsystem
            ├── README.md             # Hardware audit, routing cascade analysis & HAL tunables
            ├── patch.patch           # Unified diff for device_xiaomi_everpal
            ├── package/
            │   └── SpatialAudio.zip  # Flashable module (Author: FrontlXOX)
            └── docs/                 # Architectural blueprint & technical breakdown
                └── spatial-audio.txt # Master spatial audio routing document
```

---

## 6. Essential Commands & Operational Workflows

### Building Flashable Modules (Unified & Reproducible)

To rebuild all KernelSU/Magisk modules and verify their zip integrity:

```bash
python src/scripts/builder.py --all
```

Or rebuild individual modules:

```bash
python src/scripts/builder.py --memory
python src/scripts/builder.py --thermal
python src/scripts/builder.py --vulkan
python src/scripts/builder.py --spatial
```

_Note: Flashable zips are always written exclusively to `src/package/<Module>/package/`._

Short flags `--memory/-m`, `--thermal/-t`, `--vulkan/-v`, `--spatial/-s` are also accepted. Vulkan-only kernel injection (without a full kernel build): `python src/scripts/builder.py --vulkan --kernel path/to/Image.gz --dtbo path/to/dtbo.img` plus optional `--blobs <dir>`.

### Building the Fronx Kernel (ZorinOS / Ubuntu)

Kernel builds live in the kernel tree (`src/trees/kernel/xiaomi/mt6833/build.sh` — reset-first: always builds from pristine Aqua (tag `AquaV3.4`), see the kernel tree's `AGENTS.md` §5/§11 on the `FronxKernel` branch for the full phase-wise flow).

**Prerequisites** (one-time setup on ZorinOS):

```bash
sudo apt install -y build-essential bc bison flex libssl-dev libelf-dev \
    python3 ccache aarch64-linux-gnu-gcc arm-linux-gnueabi-gcc
```

ZyC Clang 22 is auto-downloaded to `~/toolchains/ZyC-clang-22.0.0` on first run.

**Kernel-only zip** (FronxKernel-\<ver\>_\<IST\>.zip via Addster09's AnyKernel3):

```bash
./src/trees/kernel/xiaomi/mt6833/build.sh
```

**With ReSukiSU + SUSFS patches baked in:**

```bash
./src/trees/kernel/xiaomi/mt6833/build.sh --with-ksu
```

**Clean build (wipe `out/` first):**

```bash
./src/trees/kernel/xiaomi/mt6833/build.sh --clean
```

_Output: `out/FronxKernel-*.zip` (+ AVB-signed `boot.img` when the PI-X base is present) — flash via KernelSU Manager or recovery._

**Injecting a pre-built kernel into the Vulkan module** (without running a full build):

```bash
python src/scripts/builder.py --vulkan \
    --kernel path/to/Image.gz \
    --dtbo path/to/dtbo.img
```


### Auditing Connected Device via ADB

Run a full hardware, Vulkan 1.3, frequency, thermal, and kernel tunable audit:

```bash
python src/scripts/verifydevice.py
```

### Automated Benchmark Execution with Live Telemetry

Run the automated Geekbench 7 benchmark suite with real-time CLI clock & workload streaming:

```bash
# Run both CPU and GPU (Vulkan) benchmarks
python src/scripts/autobench.py

# Run CPU benchmark only
python src/scripts/autobench.py --cpu-only

# Run GPU Vulkan benchmark only
python src/scripts/autobench.py --gpu-only
```

### Decrypting / Inspecting Xiaomi Thermal Profiles

Decrypt a single thermal configuration:

```bash
python src/scripts/decrypt_thermal.py src/package/ThermalMgmt/docs/vendor_configs/thermal-normal.conf
```

Batch decrypt all vendor profiles:

```bash
python src/scripts/decrypt_thermal.py --batch src/package/ThermalMgmt/docs/vendor_configs/
```

### Pulling Live Benchmark Results via ADB

Extract Geekbench 7 CPU & GPU and 3DMark Sling Shot Extreme scores directly from on-device SQLite databases:

```bash
python src/scripts/benchpull.py
```

### Submodule Synchronization (GitHub FrontlXOX)

Sync all submodules directly into GitHub forks using the automated synchronizer:

```bash
python src/scripts/synctrees.py
```

Or via PowerShell:

```powershell
Get-ChildItem -Directory src/trees | ForEach-Object {
    git -C $_.FullName push origin
}
```

### Validating Device State via ADB

Run these non-destructive inspection commands on connected devices:

```bash
# Check current thermal profile and sconfig mode
adb shell "getprop sys.thermal.mode; cat /sys/class/thermal/thermal_message/sconfig"

# Check CPU scaling frequencies
adb shell "cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_cur_freq"

# Inspect memory zones and watermarks
adb shell "cat /proc/zoneinfo | grep -E 'Node|min|low|high'"

# Inspect ZRAM and swap allocation
adb shell "cat /proc/swaps; cat /proc/meminfo | grep -E 'MemTotal|MemFree|MemAvailable|SwapTotal|SwapFree'"

# Inspect LMKD kill logs
adb logcat -d -s lmkd
```

### Git & GitHub Workflow

Commit message convention: `<emoji> [<TYPE>]: <description>`

```bash
# Commit format examples:
git commit -m "🦋 [FEAT]: add dynamic memory compaction trigger"
git commit -m "🐛 [FIX]: resolve thermal zone trip point mismatch"
git commit -m "♻️ [REFACTOR]: update vendor thermal conf parsing script"

# Push and release:
git push origin main
glab release create v1.0.0 "src/package/MemoryMgmt/package/MemoryMgmt.zip#MemoryMgmt.zip" "src/package/ThermalMgmt/package/ThermalMgmt.zip#ThermalMgmt.zip" --name "v1.0.0 - Release"
```

---

## 7. Inviolable Guardrails & Operational Constraints

All agents working within this codebase must strictly observe these rules:

1. 🔄 **Reboot Discipline:** `adb reboot` is allowed when the task requires it (e.g., activating a flashed module). After every reboot, ALWAYS run `adb wait-for-device` before issuing further commands, then tail realtime logs (`adb logcat`) to catch bootloops, SELinux denials, or service crashes early.
2. 🛑 **No Kernel Spinloops:** NEVER write to `/proc/driver/thermal/set_sspm_big_limit_threshold`. It causes an unkillable 84% CPU kernel IPI spinloop.
3. 🛑 **No Backlight Tampering:** NEVER alter `mtk-cl-backlight` cooling levels in thermal configs. Doing so forces PWM brightness to 0, causing permanent black screens on lock/unlock.
4. 🛑 **Zip Placement Boundary:** Builder-produced EverpalTweaks flashable `.zip` archives must reside **exclusively** inside their respective `src/package/` directories (`src/package/MemoryMgmt/package/`, `src/package/ThermalMgmt/package/`, `src/package/Vulkan13/package/`, and `src/package/SpatialAudio/package/`). The sole sanctioned exception is the curated root `src/modules/` third-party companion collection (root/LSPosed/Zygisk/ReSukiSU tooling flashed alongside EverpalTweaks). Never place `.zip` files elsewhere in the repository root or script directories.
5. 🛑 **Scripts Centralization Boundary:** All required Python automation, build, extraction, and verification scripts must reside **exclusively** in the root `src/scripts/` folder. Do not create or reintroduce scripts inside `package/*/scripts/`. The sole sanctioned exception is the third-party `src/modules/ResukiSU/` repack tooling (`main.py` + `python/` helpers), which ships verbatim as part of that companion module.
6. 🛑 **No Secrets or Bloat:** Never commit `.env` files, API tokens, local OS metadata (`.DS_Store`, `Thumbs.db`), Python caches (`__pycache__`), SQLite WAL journal files, or session transcripts / raw JSONL logs (`src/docs/`, `SESSION_TRANSCRIPT.md`, `transcript_archive.jsonl.gz`). Engineering session history must not be committed to the repo.
7. 🛑 **Attribution Integrity:**
   - Magisk / KernelSU modules must maintain `author=FrontlXOX` strictly inside `module.prop`.
   - General project authorship and maintainership belongs to `Author & Maintainer: Shovit Dutta`.
   - Architectural and research credits honor: `Special Thanks & Collaborators: Addster09 x himanshuksr0007 (Goku)`.
   - Under NO circumstances should `FrontlXOX` be listed under Authors & Credits in documentation (project authorship belongs to Shovit Dutta).
8. 🔄 **Benchmark URL Maintenance:** Whenever a new peak record run is achieved, always update the official side-by-side comparison URL (`https://browser.geekbench.com/v7/cpu/compare/<NEW_RECORD_ID>?baseline=380539`) across all documentation markdown files (`README.md`, `AGENTS.md`, `src/package/ThermalMgmt/README.md`).
9. 💬 **Collaborator Communications Protocol (`convo.txt`):** Whenever preparing technical information, updates, advice, or roadmaps to inform or reply to collaborators **Goku (`himanshuksr0007`)** or **Addster09**, ALWAYS create/write to a dedicated file named `convo.txt` in the repository root (`D:\EverpalTweaks\convo.txt`). The message MUST ALWAYS be **compact, concise, punchy, and strictly TO THE POINT**, using an engaging blend of technical accuracy and casual developer Telegram/chat style (e.g., emojis, bullet points, direct code/commit links, zero fluff) ready for the user to copy-paste directly to them.
10. 🐙 **GitHub Primacy & Source Repos:** All project hosting, trees, and collaborator cherry-picks reside on **GitHub**:
    - **Active Android 16 Bringup (himanshuksr0007):** [`device_xiaomi_everpal`](https://github.com/himanshuksr0007/device_xiaomi_everpal) (lineage-23.2), [`vendor_xiaomi_everpal`](https://github.com/himanshuksr0007/vendor_xiaomi_everpal) (lineage-23.2), [`android_kernel_xiaomi_mt6833`](https://github.com/himanshuksr0007/android_kernel_xiaomi_mt6833) (lineage-24.0), [`vendor_xiaomi_camera-everpal`](https://github.com/himanshuksr0007/vendor_xiaomi_camera-everpal) (lineage-23.2).
    - **Platform & Hardware Trees (FrontlXOX):** [`EverpalTweaks`](https://github.com/FrontlXOX/EverpalTweaks), [`android_device_mediatek_sepolicy_vndr`](https://github.com/FrontlXOX/android_device_mediatek_sepolicy_vndr) (lineage-23.0), [`android_hardware_mediatek`](https://github.com/FrontlXOX/android_hardware_mediatek) (lineage-23.0), [`android_hardware_xiaomi`](https://github.com/FrontlXOX/android_hardware_xiaomi) (lineage-23.0), [`android_vendor_mediatek_ims`](https://github.com/FrontlXOX/android_vendor_mediatek_ims) (android-16-qpr2).
    - **Donor Kernel:** [`kernel_millennium_mt6789-common`](https://github.com/MillenniumOSS/kernel_millennium_mt6789-common) (vic).
11. 🌲 **Submodule GitHub Tracking:** All submodules in `src/trees/` track their designated GitHub repos as remote `origin`. Upstream synchronization (`src/scripts/synctrees.py`) pushes directly to `origin` on GitHub.
12. 🤖 **Sub-Agent First Policy:** Before the parent agent makes any direct code edits, file writes, or tree modifications for non-trivial tasks, it MUST first delegate discovery, auditing, and research to specialized sub-agents. The parent agent acts as orchestrator — it reads sub-agent findings, synthesizes them, then and only then executes targeted changes. Direct parent-agent edits without prior sub-agent research are only acceptable for single-line fixes, typo corrections, or trivially scoped changes confirmed at a glance.
13. 🛑 **Flashable Script Encoding Hygiene:** All shell scripts shipped inside flashable zips (`anykernel.sh`, `META-INF/com/google/android/update-binary`, `updater-script`) MUST be pure LF, ASCII, and free of BOM/garbage-byte prefixes. CRLF line endings break the recovery shebang (`#!/sbin/sh^M` → "bad interpreter" → instant sideload abort), and stray non-ASCII bytes (e.g. U+3002 `。` from a bad editor save) become fatal commands under `set -e`. Verify with `file` (must NOT say "with CRLF"), `grep -c $'\r'` (must be 0), and `sh -n` before zipping.
14. 🛑 **Scratch & Output Placement:** All build-related scratch/temp work goes in `./build/` and all outputs in `./out/`. Never use `/tmp/opencode` (or other system temp dirs) for repo work — contents vanish on reboot and are invisible to the user.

---

## 8. AI Operational Directives

### Sub-Agent Delegation (Mandatory)

Agents MUST proactively spawn sub-agents before making changes whenever the task involves:

- **Codebase exploration** — reading multiple files, directories, or submodules to understand current state
- **Multi-tree audits** — verifying consistency across `device_xiaomi_everpal`, `vendor_xiaomi_everpal`, and `android_kernel_xiaomi_mt6833` simultaneously
- **Security / SELinux audits** — checking policy files, file_contexts, property_contexts across the full sepolicy tree
- **Performance / benchmark research** — cross-referencing multiple docs, benchmark DBs, and upstream references
- **Dependency tracing** — mapping `Android.bp` module chains, `PRODUCT_PACKAGES`, `PRODUCT_COPY_FILES` across device and vendor trees
- **Pre-implementation verification** — confirming blob paths, kernel config state, or prop values before applying patches

**Spawn pattern:**
1. Parent agent dispatches `research` sub-agent(s) with precise read-only audit prompts
2. Sub-agent(s) report findings back
3. Parent agent synthesizes findings and executes only the targeted, confirmed edits

### Phase-Wise Execution

Break down complex tasks into sequential phases:

1. **Discovery & Sub-Agent Audit** — delegate broad research; never assume current state
2. **Implementation** — targeted edits based on confirmed findings only
3. **Verification** — run `verifydevice.py`, `builder.py --all`, or `git diff` as appropriate
4. **Commit & Push** — granular, logically grouped commits per tree

Complete and validate each phase before progressing to the next.

### Background Task Rules

- **No polling loops** — NEVER use `schedule` or `manage_task(status)` in a loop to wait for background tasks.
- **Reactive wakeup** — After launching background commands or sub-agents, end the turn. The system notifies on completion.
- **User-driven stalls** — If a task gets stuck, wait for the user to report it.

---

## 9. Linux 5.10 Bringup (everpal — active workstream)

5.10 port tree: `src/trees/kernel-5.10`, branch **`muse_evergo`** (gold donor base). Current base ROM is **AlphaDroid** (`out/AlphaDroid_AospBOOT.img`: hv2, page 2048, base `0x40000000`, k_offset `0x80000`, ramdisk `0x11100000`, tags/dtb `0x7c80000`, os 16.0.0/2026-05, AVB SHA256_RSA2048 rollback 1, salt `0c4a3d71…`, ramdisk 18,443,389 B, stock DTB 170,672 B). Prior Axion base is retired. Debug cmdline carried on every test image: stock bootopt + `androidboot.selinux=permissive hung_task_timeout_secs=8 watchdog_thresh=5 printk.devkmsg=on initcall_debug console=ttyS0,921600n1`.

### Test cycle (flash-based only; `fastboot boot` unsupported)

```bash
fastboot erase misc; fastboot flash boot_a boot.img; fastboot flash boot_b boot.img; fastboot --set-active=b; fastboot reboot;
```

3 hands-off loops (`fastboot reboot` between attempts, no keys) → straight to BROM (keys, no kernel/LK boot) → pulls below → restore → boot system. `--set-active=b` is load-bearing: ROM lives on slot B; slot A has no system (boots landing on A die on empty `system_a`). `erase misc` every round (Rescue Party poisons BCB → recovery-mode boots). Archive every test image in `out/Archive/` (user moves images off-machine; `out/` is gitignored). Every version gets a TL;DR for the user.

### Evidence pipeline (BROM; root/adb no longer used for pulls)

Host kit: `C:\Users\psycosis\Downloads\EvergoBROM\` (`commands.txt` = source of truth, `firmware/` = evergo preloader + DA + auth, `mtk-client/`, `output/`). Fixed host names (`expdb.bin` 40MB, `ramoops.bin` 896K, overwrite per round); WSL files them as `out/bromPull/testXX/{expdb,ramoops}-testXX.bin`. Order matters — DRAM first:

```bash
python mtk-client/mtk da peek 0x48090000 0xe0000 --preloader firmware/preloader_evergo.bin --filename output/ramoops.bin
python mtk-client/mtk r expdb output/expdb.bin --preloader firmware/preloader_evergo.bin --loader firmware/MTK_AllInOne_DA.bin
```

- `peek` (preloader mode) is BANNED — hangs on PreLoader VCOM re-enumeration. `da peek` (DA mode) is the working DRAM path.
- `da` subcommands accept no `--loader`; `mtk-client/Loader/MTK_AllInOne_DA_5.2152.bin` holds a copy of the proven evergo DA (original kept as `.bak`). Revert: `cp mtk-client/Loader/MTK_AllInOne_DA_5.2152.bin.bak mtk-client/Loader/MTK_AllInOne_DA_5.2152.bin`.
- `printgpt` offsets are byte offsets; `rs` units are 4096-byte sectors; `ro` byte reads of some regions return zeros (use `rs`, verify non-zero).
- expdb holds preloader/TEE/LK logs only — kernel evidence lives in pstore DRAM (`0x48090000`, LK-passed DTB region). Anchor multi-record pulls by content (banner hash), never file order. Branches: `muse_evergo` (kernel), `main` (repo).

### Bugs killed (test57→test65)

1. Gold DTB → LK `panic: ASSERT boot_info.c:61 g_boot_info.img_loaded` after a metronomic 5736ms load; kernel never starts. Fix: ship **stock DTB** (test59+). Gold DTB is unproven on Axion/AlphaDroid LK.
2. Stock DTB lacks serial console (gold had none either; stock has `ttyS0`). Fix: `console=ttyS0,921600n1` on cmdline (test58+).
3. `dm-verity: Invalid number of feature args` → `InitFatalReboot` on `/system`. Android 16 sends 10 opt args (FEC); `DM_VERITY_FEC` was off (cap 3). Fix: `CONFIG_DM_VERITY_FEC=y` (test60, commit `4e73c04`).
4. Broken `mt6833.dtb` build: everpal header edit removed IFRAO clock IDs 61/63 but two `.dtsi` files still referenced them. Fix: dropped the 4 dangling lines (same commit).
5. CRNG never seeds (`crng init done` absent, ~50 uninitialized reads) → keystore2 never registers → vold waits → no zygote. TRNG is secure-only (DEVAPC blocks AP MMIO reads — `mtk-rng` on `trng` yields violations, reverted approach). Mitigations shipped: `HW_RANDOM_MTK=y` + `trng` bind (test62, commit `f81dbac`), DT `rng-seed` in `/chosen` (test63; `RANDOM_TRUST_BOOTLOADER` already y, warnings 40→7). DTB path proven via `rngtest=63` marker in `/init` environ (test64).
6. **Blocker solved via root (test66→test69):** keystore2 never registers because beanpod (Keymaster HAL) wedges pre-IPC (zero binder calls in test67 trace; hwservicemanager healthy, answers everything; AIDL binder healthy). Live rooted stock proved beanpod holds `/dev/isee_tee0` (fd 5) + hwbinder (fd 3), wchan `binder_ioctl_write_read`. Our kernel never created it — microtrust tzdriver compiled only as `obj-m` while ramdisk has no `/lib/modules`. Fix: `400/Makefile obj-m → obj-$(CONFIG_MICROTRUST_TZ_DRIVER)` + `CONFIG_ANDROID_BINDERFS=y` (stock uses binderfs symlinks) + dynamic-core/bootprof off (test69, commit `039ffca`); dropped fpc1542 `uuid_fp` dupe (collided once isee went monolithic). Binder transaction tracing (test67, commit `2957d4a`) REVERTED after use — never ship it (dmesg flood).
7. Detours killed: DT `rng-seed` (test63) + `rngtest=63` marker (test64) proved LK merges our bootargs to cmdline, but `ro`/`rs` forensics + persistent DEVAPC `TRNG_APB_S` violations after deleting the `trng` node (test68) prove LK substitutes its own DTB (169861 B `lk_main_dtb`, extracted from `lk_a` — near-identical to stock, same microtrust nodes). DTB edits (except bootargs) are VOID; seed/TRNG approaches dead. TRNG is secure-only (AP reads fault). `rng-seed`/fstab-bypass retired.
8. Device runs patched evergo LK (lk-unlocker) — LK-version markers in pulls refer to it, not stock.
9. Current kernel: `5.10.168` + evergo panel/touch commits; defconfig deltas live in `everpal_510_defconfig` (UNIX/cgroups/loop-16/blk_cgroup/bpf/FEC/HW_RANDOM_MTK/BINDERFS/TEE-builtin).

### Build environment (hard-won)

- Proven: `clang-r416183b` (`build/toolchains/`) on PATH, `CC="ccache clang" LLVM=1 LLVM_IAS=1`, NO `LD=` override (it breaks kconfig linker probe), NO repo-script `KCFLAGS` (clang-22-only warning flag). ZyC-22 turns new warnings (`default-const-init-field-unsafe`, `bitwise-instead-of-logical`, `strict-prototypes`) into errors — do not mix toolchains mid-tree.
- After defconfig edits: `make O=out everpal_510_defconfig && make O=out olddefconfig`, then `-j` build. `syncconfig` passes standalone; `-j` races on the kconfig tool are environmental noise.
- Scratch/build temp → `./build/`; outputs → `./out/`. Never `/tmp/opencode`.
