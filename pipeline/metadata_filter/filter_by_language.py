import json
import sys


def is_any_a_in_b(list_a, list_b):
    normalized_set_b = set(str(item).lower() for item in list_b)
    return any(str(item).lower() in normalized_set_b for item in list_a)


target_language_abbr = ["algeria", "algerie", "ar", "alg", "dz"]
info_file = sys.argv[1]


with open(info_file) as f:
    with open("filtered_" + info_file) as f:
    for info in f:
        info = json.loads(info)

        if info["language"] != "ar" and is_any_a_in_b(target_language_abbr, info["tags"]):
            print(info)
