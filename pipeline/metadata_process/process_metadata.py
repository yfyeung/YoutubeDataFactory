import json
import re
import sys

from tqdm import tqdm
from zhipuai import ZhipuAI


def keep_chinese_and_punctuation_regex(text):
    pattern = r"[\u4e00-\u9fff\u3000-\u303f\uff00-\uffef]"
    return "".join(re.findall(pattern, text))


def keep_enlish_letters(text):
    return "".join(filter(str.isalpha, text))


info_file = sys.argv[1]
api_key = sys.argv[2]

client = ZhipuAI(api_key=api_key)

with open(info_file) as f1:
    with open(info_file.replace(".json", "-processed.json"), "w") as f2:
        for info in tqdm(f1):
            info = json.loads(info)
            title = info["title"]

            response = client.chat.completions.create(
                model="glm-4-flash",
                messages=[
                    {
                        "role": "user",
                        "content": f"请将 youtube 视频的 title 翻译为中文，直接给出翻译结果: {title}",
                    },
                ],
            )
            translated_title = keep_chinese_and_punctuation_regex(
                response.choices[0].message.content
            )

            response = client.chat.completions.create(
                model="glm-4-flash",
                messages=[
                    {
                        "role": "user",
                        "content": f"Given YouTube video title, directly output a single English word subject, very broad domain like Politics, Economics, Culture, Military, Technology, Society, Environment, Health, Education, Sports, Crime: {title}",
                    },
                ],
            )
            category = keep_enlish_letters(response.choices[0].message.content)

            info["translated_title"] = translated_title
            info["category"] = category

            f2.write(json.dumps(info, ensure_ascii=False) + "\n")
