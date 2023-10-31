import re
import os
os.mkdir('./bqb')
import requests
url = 'https://www.fabiaoqing.com/'
response = requests.get(url=url)
data = response.text
"""
<img class="ui image" src="(.*?)" alt=".*?"/ style=".*?">

"""
img_urls = re.findall('<img class="ui image" src="(.*?)" alt=".*?"/ style=".*?">', data, re.S)
for img_url in img_urls:
    contend = requests.get(url=img_url).content
    name = img_url.split('/')[-1]
    with open('./bqb/'+name, mode='wb') as f:
        f.write(contend)

"""
表情包爬取
将此页面下的前十页图片全部获取下来：https://fabiaoqing.com/biaoqing
"""
# import re
# import os
# """请下下方开始编写代码"""
# os.mkdir('./img')
# import requests
#
# for page in range(1, 11):
#     print(f'======================正在抓取第{page}页数据==========================')
#     response = requests.get(f'https://fabiaoqing.com/biaoqing/lists/page/{page}.html')
#     html_data = response.text
#     # print(html_data)
#
#     # 解析这一页图片地址
#     """
#     <img class="ui image lazy" data-original=".*?" src="(.*?)" title=.*?
#
#     <img class="ui image lazy" data-original="(.*?)" src=.*?
#     """
#     result = re.findall('<img class="ui image lazy" data-original="(.*?)" src=.*?', html_data, re.S)
#     # print(result)
#
#     for img_url in result:
#         img_response = requests.get(img_url)
#         img_data = img_response.content  # 请求图片数据
#         file_name = img_url.split('/')[-1]
#
#         with open('img\\' + file_name, mode='wb') as f:
#             f.write(img_data)
#             print('正在保存:', file_name)