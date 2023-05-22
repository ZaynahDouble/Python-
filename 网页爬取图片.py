import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

# 发送HTTP GET请求获取网页内容
url = "http://www.lvlvg.com/bsdq/"
response = requests.get(url)
content = response.text

# 使用BeautifulSoup解析网页内容
soup = BeautifulSoup(content, 'html.parser')

# 定位目标元素
panel_divs = soup.select('body div.left.main_l div.container div.content div.mod-panel div.bd div.panels div.panel')

# 保存图片的目录路径
save_dir = 'C:/Users/zengyahon/Desktop/photo/001/'

# 遍历panel_divs并保存图片
for panel_div in panel_divs:
    # 获取每个panel_div中的li列表
    lis = panel_div.select('li')

    # 遍历li列表并保存图片
    for li in lis:
        # 获取第一个span中的img和第二个span中的文字
        img = li.select_one('span:nth-of-type(1) img')
        text = li.select_one('span:nth-of-type(2)').text.strip()

        # 下载图片并保存
        if img:
            img_url = img['src']
            # 添加协议前缀
            full_img_url = urljoin(url, img_url)
            # 根据第二个span中的文字生成图片的文件名
            filename = f"{text}.jpg"
            # 拼接完整的文件路径
            file_path = os.path.join(save_dir, filename)
            # 发送HTTP GET请求下载图片并保存到指定路径
            response = requests.get(full_img_url)
            with open(file_path, 'wb') as f:
                f.write(response.content)
            print(f"保存图片：{file_path}")

print("图片下载完成。")
