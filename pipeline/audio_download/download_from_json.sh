#!/bin/bash

JSON_FILE=$1
archive_file="download_$(basename "$JSON_FILE" .json).txt"

while IFS= read -r line; do
  video_id=$(echo "$line" | jq -r .id)

  youtube_url="http://www.youtube.com/watch?v=${video_id}"

  yt-dlp -f 'ba' \
    --download-archive $archive_file \
    --cookies cookies.txt \
    "$youtube_url" -o '%(channel_id)s#%(id)s.%(ext)s'
done < $JSON_FILE
