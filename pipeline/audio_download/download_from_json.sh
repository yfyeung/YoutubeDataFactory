#!/bin/bash

JSON_FILE=$1
WORKSPACE_ROOT=$2
channel_name=$3
archive_file=${WORKSPACE_ROOT}/"download_${channel_name}.txt"
output_dir=${WORKSPACE_ROOT}/${channel_name}

mkdir -p $output_dir

while IFS= read -r line; do
  video_id=$(echo "$line" | jq -r .id)

  youtube_url="http://www.youtube.com/watch?v=${video_id}"

  yt-dlp -f 'ba' \
    --download-archive $archive_file \
    --cookies ${WORKSPACE_ROOT}/cookies.txt \
    "$youtube_url" -o ${output_dir}/'%(channel_id)s#%(id)s.%(ext)s'
done < $JSON_FILE
