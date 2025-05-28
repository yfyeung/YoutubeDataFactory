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
                        "content": f"请将 youtube 视频的 title 翻译为中文，然后加一个空格，直接给出一个单词描述其类别: {title}",
                    },
                ],
            )

            try:
                response = response.choices[0].message.content
                translated_title, category = response.rsplit(" ", 1)
            except:
                print(response)
                translated_title = response
                category = None

            info["translated_title"] = translated_title
            info["category"] = category

            f2.write(json.dumps(info, ensure_ascii=False) + "\n")
