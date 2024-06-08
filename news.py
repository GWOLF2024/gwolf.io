import os
from datetime import date
import requests


def handle_request(url2):
    try:
        response = requests.get(url2)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print("请求失败，状态码：", e.response.status_code)
        return None


# 获取当前日期并作为文件名的一部分
current_date = date.today().strftime("%Y%m%d")
filename = f"d:/news/{current_date}.html"

# 检查文件是否存在
if os.path.exists(filename):
    print("文件已存在，不执行任何操作。")
else:
    url = "https://news.topurl.cn/"  # 替换为您需要请求的URL
    result = handle_request(url)
    if result:
        print("请求成功，返回内容：")
        print(result)
    else:
        print("请求失败，请检查网络连接或稍后重试。")

    # 将结果写入文件
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(result)

    print("已保存")

