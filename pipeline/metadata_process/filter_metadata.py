import json
import logging
import sys


def is_any_a_in_b(list_a, list_b):
    normalized_set_b = set(str(item).lower() for item in list_b)
    return any(str(item).lower() in normalized_set_b for item in list_a)


channel_id = "UCfF6CkUvCBleM19CkgNyrYw"
target_language_abbr = ["algeria", "algerie", "ar", "alg", "dz"]
min_duration = 60
max_duration = 60 * 20


info_file = sys.argv[1]
with open(info_file) as f1:
    with open(info_file.replace(".json", "-filtered.json"), "w") as f2:
        for info in f1:
            info = json.loads(info)

            if (
                info["channel_id"] != channel_id
            ):  # ensure crawling is restricted to the target channel.
                logging.warning(
                    "Skipping item from unexpected channel: ", info["channel_id"]
                )
                continue

            if info["language"] != "ar" or not is_any_a_in_b(
                target_language_abbr, info["tags"]
            ):  # ensure target language
                continue

            if (
                info["media_type"] != "video" or info["live_status"] != "not_live"
            ):  # ensure video formet
                continue

            if (
                info["duration"] < min_duration or info["duration"] > max_duration
            ):  # ensure duration within 1min and 20min
                continue

            if info["like_count"] < 100:  # ensure high popularity
                continue

            fields_to_keep = [
                "channel_id",
                "id",
                "title",
                "description",
                "duration",
                "upload_date",
            ]
            info = {field: info[field] for field in fields_to_keep}

            f2.write(json.dumps(info, ensure_ascii=False) + "\n")
