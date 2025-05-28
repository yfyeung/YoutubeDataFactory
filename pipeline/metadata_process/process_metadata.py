import json
import sys
from tqdm import tqdm

from zhipuai import ZhipuAI

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
            translated_title = response.choices[0].message.content

            response = client.chat.completions.create(
                model="glm-4-flash",
                messages=[
                    {
                        "role": "user",
                        "content": f"根据 youtube 视频的 title，直接给出一个英文单词描述其类别: {title}",
                    },
                ],
            )
            category = response.choices[0].message.content

            info["translated_title"] = translated_title
            info["category"] = category

            f2.write(json.dumps(info, ensure_ascii=False) + "\n")
