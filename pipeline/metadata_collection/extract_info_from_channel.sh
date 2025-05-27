#! /usr/bin/bash

channel="Elbiladtv1"
workspace_dir="/content/drive/MyDrive/dataset/youtube_algeria"

echo "Processing channel: $channel"
yt-dlp \
  -j \
  -I "0:10000" \
  --cookies ${workspace_dir}/cookies.txt \
  --download-archive ${workspace_dir}/manifests_${channel}.txt \
  "https://www.youtube.com/@${channel}/videos" \
  | jq -c -r '{id, channel_id, language, title, description, tags, categories, media_type, live_status, license, duration, upload_date, view_count, like_count}' \
  | tee ${workspace_dir}/manifests_${channel}-0.json
