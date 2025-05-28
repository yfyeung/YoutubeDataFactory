#! /usr/bin/bash

channel=$1
WORKSPACE_ROOT=$2

echo "Processing channel: $channel"
yt-dlp \
  -j \
  -I "0:10000" \
  --cookies ${WORKSPACE_ROOT}/cookies.txt \
  --download-archive ${WORKSPACE_ROOT}/manifests_${channel}.txt \
  "https://www.youtube.com/@${channel}/videos" \
  | jq -c -r '{id, channel_id, language, title, description, tags, categories, media_type, live_status, license, duration, upload_date, view_count, like_count}' \
  | tee ${WORKSPACE_ROOT}/manifests_${channel}-0.json
