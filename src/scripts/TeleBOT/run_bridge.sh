#!/usr/bin/env bash
cd "$(dirname "$0")"
while true; do
  echo "--- starting tg_bridge at $(date '+%F %T') ---" >> bridge.log
  python3 index.py >> bridge.log 2>&1
  echo "--- tg_bridge exited ($?), restarting in 3s ---" >> bridge.log
  sleep 3
done
