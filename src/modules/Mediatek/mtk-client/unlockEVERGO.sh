#!/bin/bash
cd "$(dirname "$0")"
PATCHED_LK="${1:-../lk-unlocker/lk_patched_evergo.img}"
if [ ! -f "$PATCHED_LK" ]; then
  echo "[-] Patched LK not found: $PATCHED_LK"
  echo "    Run: python3 ../lk-unlocker/lk-unlock.py patch <lk.img> -o $PATCHED_LK"
  exit 1
fi
python3 mtk e metadata,userdata
python3 mtk e md_udc || true
python3 mtk w lk_a,lk_b "$PATCHED_LK,$PATCHED_LK"
python3 mtk reset
echo "[+] Done. Disconnect, boot to fastboot, then:"
echo "    python3 ../lk-unlocker/lk-unlock.py unlock"
