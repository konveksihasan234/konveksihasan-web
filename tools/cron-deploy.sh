#!/bin/bash
# Dijalankan Cron Job cPanel tiap 15 menit.
# Tarik perubahan dari GitHub; bila ada commit baru, jalankan deploy (.cpanel.yml) ke public_html.
REPO=/home/konvek17/repositories/konveksihasan-web
LOG="$HOME/logs/konveksihasan-deploy.log"
mkdir -p "$HOME/logs"

cd "$REPO" || exit 1
LAMA=$(git rev-parse HEAD)
if ! git pull -q --ff-only origin main >>"$LOG" 2>&1; then
  echo "$(date '+%F %T') GAGAL git pull" >>"$LOG"
  exit 1
fi
BARU=$(git rev-parse HEAD)

if [ "$LAMA" != "$BARU" ]; then
  if uapi VersionControlDeployment create repository_root="$REPO" >>"$LOG" 2>&1; then
    echo "$(date '+%F %T') deploy $BARU" >>"$LOG"
  else
    echo "$(date '+%F %T') GAGAL deploy $BARU" >>"$LOG"
  fi
fi
