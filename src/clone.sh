# ===================================================|| XOX ||===================================================
# ===================================================|| XOX ||===================================================
#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(git -C "$SCRIPT_DIR" rev-parse --show-toplevel 2>/dev/null || (cd "$SCRIPT_DIR/../.." && pwd))"
TREES_DIR="$REPO_ROOT/src/trees"
info()  { printf '\033[1;34m==>\033[0m %s\n' "$*"; }
ok()    { printf '\033[1;32m  ✓\033[0m %s\n' "$*"; }
warn()  { printf '\033[1;33m  !\033[0m %s\n' "$*"; }
err()   { printf '\033[1;31m  ✗\033[0m %s\n' "$*" >&2; }
header(){ printf '\033[1;36m%s\033[0m\n' "$*"; }
AUTO_SUBMODULE="true"
DO_SYNC="false"
DEPTH="1"
declare -a DEFAULT_TREES=(
    "src/trees/device/mediatek/sepolicy_vndr|https://github.com/FrontlXOX/android_device_mediatek_sepolicy_vndr.git|lineage-24.0"
    "src/trees/device/xiaomi/everpal|https://github.com/FrontlXOX/device_xiaomi_everpal.git|lineage-23.2"
    "src/trees/vendor/xiaomi/everpal|https://github.com/FrontlXOX/vendor_xiaomi_everpal.git|lineage-23.2"
    "src/trees/kernel/xiaomi/mt6833|https://github.com/FrontlXOX/android_kernel_xiaomi_mt6833.git|lineage-24"
    "src/trees/hardware/mediatek|https://github.com/FrontlXOX/android_hardware_mediatek.git|lineage-23.0"
    "src/trees/hardware/xiaomi|https://github.com/FrontlXOX/android_hardware_xiaomi.git|lineage-23.0"
    "src/trees/vendor/mediatek/ims|https://github.com/FrontlXOX/android_vendor_mediatek_ims.git|android-16-qpr2"
    "src/trees/vendor/xiaomi/camera|https://github.com/FrontlXOX/vendor_xiaomi_camera-everpal.git|lineage-23.2"
    "src/trees/kernel-5.10|https://github.com/FrontlXOX/donor_5.10_kernel_xiaomi_gold.git|gold-s-oss"
    "src/modules/Mediatek/lk-unlocker|https://github.com/georgiynesterov/lk-unlock.git|main"
)
show_help() {
    cat << EOF
Usage: $(basename "$0") [options] [<url> <dest_path> [branch]]

Smart Tree Cloner & Submodule Registrator for Everpal.
Clones target repositories with shallow depth 1 (latest commit only), then automatically absorbs and registers them as git submodules.

Modes:
  $(basename "$0")                          Clone and register all default trees & submodules
  $(basename "$0") <url> <dest> [branch]    Clone and register a specific repository as submodule

Options:
  --all                   Process all trees (default when no positional arguments)
  --depth <N>             Clone depth (default: 1, latest commit only)
  --full                  Full clone history (disables shallow clone)
  --no-submodule          Only clone the repository, skip submodule registration
  --sync                  Synchronize all submodules (URLs, branches, active status)
  -h, --help              Show this help message

Examples:
  ./clone.sh
  ./clone.sh https://github.com/example/repo.git src/trees/example main
  ./clone.sh --full
EOF
}
normalize_path() {
    local p="$1"
    if [[ "$p" = /* ]]; then
        if [[ "$p" == "$REPO_ROOT/"* ]]; then
            p="${p#"$REPO_ROOT/"}"
        fi
    else
        if [[ "$p" != src/* ]]; then
            p="src/trees/$p"
        fi
    fi
    echo "$p"
}
clone_and_submodule() {
    local relpath="$1"
    local url="$2"
    local branch="${3:-}"
    relpath="$(normalize_path "$relpath")"
    local target_dir="$REPO_ROOT/$relpath"
    local is_repo="false"
    if git -C "$REPO_ROOT" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
        is_repo="true"
    fi
    info "Processing: $relpath ($url ${branch:+[$branch]})"
    if [ -d "$target_dir/.git" ] || [ -f "$target_dir/.git" ]; then
        info "Existing repository detected at $relpath"
        local current_url
        current_url="$(git -C "$target_dir" remote get-url origin 2>/dev/null || echo "")"
        if [ -n "$current_url" ] && [ "$current_url" != "$url" ]; then
            info "Updating remote URL ($current_url -> $url)"
            git -C "$target_dir" remote set-url origin "$url" 2>/dev/null || true
        fi
        if [ -n "$branch" ]; then
            local curr_branch
            curr_branch="$(git -C "$target_dir" rev-parse --abbrev-ref HEAD 2>/dev/null || echo "HEAD")"
            if [ "$curr_branch" = "HEAD" ] || [ "$curr_branch" != "$branch" ]; then
                info "Aligning branch ($curr_branch -> $branch)"
                git -C "$target_dir" checkout "$branch" 2>/dev/null || {
                    git -C "$target_dir" fetch --depth 1 --no-tags origin "$branch" 2>/dev/null || true
                    git -C "$target_dir" checkout -B "$branch" "origin/$branch" 2>/dev/null || true
                }
            fi
        fi
    else
        mkdir -p "$(dirname "$target_dir")"
        info "Cloning $url ${branch:+(-b $branch)} -> $relpath (latest commit only)"
        local clone_args=()
        if [ -n "$DEPTH" ] && [ "$DEPTH" -gt 0 ]; then
            clone_args+=(--depth "$DEPTH" --single-branch --no-tags)
        fi
        if [ -n "$branch" ]; then
            clone_args+=(-b "$branch")
        fi
        if ! git clone "${clone_args[@]}" "$url" "$target_dir"; then
            warn "Branch clone failed. Attempting fallback clone of default branch (depth $DEPTH)..."
            local fallback_args=()
            if [ -n "$DEPTH" ] && [ "$DEPTH" -gt 0 ]; then
                fallback_args+=(--depth "$DEPTH" --single-branch --no-tags)
            fi
            git clone "${fallback_args[@]}" "$url" "$target_dir"
            if [ -n "$branch" ]; then
                git -C "$target_dir" checkout -B "$branch" "origin/$branch" 2>/dev/null || true
            fi
        fi
        ok "Cloned $relpath"
    fi
    if [ "$AUTO_SUBMODULE" = "true" ] && [ "$is_repo" = "true" ]; then
        info "Registering submodule for $relpath"
        git -C "$REPO_ROOT" submodule absorbgitdirs -- "$relpath" 2>/dev/null || true
        git -C "$REPO_ROOT" config -f .gitmodules "submodule.${relpath}.path" "$relpath"
        git -C "$REPO_ROOT" config -f .gitmodules "submodule.${relpath}.url" "$url"
        [ -n "$branch" ] && git -C "$REPO_ROOT" config -f .gitmodules "submodule.${relpath}.branch" "$branch"
        git -C "$REPO_ROOT" config -f .gitmodules "submodule.${relpath}.shallow" "true"
        git -C "$REPO_ROOT" config -f .gitmodules "submodule.${relpath}.ignore" "dirty"
        git -C "$REPO_ROOT" config "submodule.${relpath}.url" "$url"
        git -C "$REPO_ROOT" config "submodule.${relpath}.active" "true"
        git -C "$REPO_ROOT" config "submodule.${relpath}.shallow" "true"
        git -C "$REPO_ROOT" add "$relpath" 2>/dev/null || true
        git -C "$REPO_ROOT" add .gitmodules 2>/dev/null || true
        git -C "$REPO_ROOT" submodule init "$relpath" >/dev/null 2>&1 || true
        ok "Submodule $relpath registered and synced"
    elif [ "$AUTO_SUBMODULE" = "true" ] && [ "$is_repo" = "false" ]; then
        warn "Not inside a git repository: skipped submodule registration for $relpath"
    fi
}
sync_all() {
    if ! git -C "$REPO_ROOT" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
        warn "Not inside a git repository; cannot sync submodules."
        return 1
    fi
    info "Synchronizing all submodules with .gitmodules..."
    git -C "$REPO_ROOT" submodule sync
    git -C "$REPO_ROOT" submodule update --init --depth 1
    ok "Submodule sync completed."
}
POSITIONAL=()
while [[ $# -gt 0 ]]; do
    case "$1" in
        -h|--help)
            show_help
            exit 0
            ;;
        --no-submodule)
            AUTO_SUBMODULE="false"
            shift
            ;;
        --depth)
            DEPTH="$2"
            shift 2
            ;;
        --depth=*)
            DEPTH="${1#*=}"
            shift
            ;;
        --full)
            DEPTH=""
            shift
            ;;
        --sync)
            DO_SYNC="true"
            shift
            ;;
        --all)
            shift
            ;;
        *)
            POSITIONAL+=("$1")
            shift
            ;;
    esac
done

if [ "$DO_SYNC" = "true" ]; then
    sync_all
    exit 0
fi
header "==================================================="
header " EverpalTweaks Smart Tree Cloner & Submodule Tool "
header "==================================================="
if [ ${#POSITIONAL[@]} -ge 2 ]; then
    URL="${POSITIONAL[0]}"
    DEST="${POSITIONAL[1]}"
    BRANCH="${POSITIONAL[2]:-}"
    clone_and_submodule "$DEST" "$URL" "$BRANCH"
elif [ ${#POSITIONAL[@]} -eq 0 ]; then
    info "Batch mode: Processing all repository trees..."
    for entry in "${DEFAULT_TREES[@]}"; do
        IFS='|' read -r relpath url branch <<< "$entry"
        clone_and_submodule "$relpath" "$url" "$branch"
    done
    if [ -f "$REPO_ROOT/.gitmodules" ]; then
        while IFS= read -r key; do
            [ -z "$key" ] && continue
            sub_path="$(git -C "$REPO_ROOT" config -f .gitmodules "$key.path" 2>/dev/null || echo "")"
            sub_url="$(git -C "$REPO_ROOT" config -f .gitmodules "$key.url" 2>/dev/null || echo "")"
            sub_branch="$(git -C "$REPO_ROOT" config -f .gitmodules "$key.branch" 2>/dev/null || echo "")"
            [ -z "$sub_path" ] || [ -z "$sub_url" ] && continue
            already_done="false"
            for entry in "${DEFAULT_TREES[@]}"; do
                IFS='|' read -r dp _ _ <<< "$entry"
                if [ "$dp" = "$sub_path" ]; then
                    already_done="true"
                    break
                fi
            done
            if [ "$already_done" = "false" ]; then
                clone_and_submodule "$sub_path" "$sub_url" "$sub_branch"
            fi
        done < <(git -C "$REPO_ROOT" config -f .gitmodules --get-regexp '^submodule\..*\.path$' 2>/dev/null | awk '{print $1}' | sed 's/\.path$//')
    fi
    ok "All trees cloned and verified."
    if [ "$AUTO_SUBMODULE" = "true" ]; then
        info "Running git submodule status check:"
        git -C "$REPO_ROOT" submodule status
    fi
else
    err "Invalid arguments. Usage: $0 <url> <dest_path> [branch]"
    exit 1
fi
