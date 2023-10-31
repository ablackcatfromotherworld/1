# -*- coding: utf-8 -*-
import re

import requests
url = 'https://video-qn.ibaotu.com/19/93/46/34f888piCrNc.mp4'
response = requests.get(url=url)
content = response.content
# 二进制数据没有编码格式
with open('视频.mp4', mode='wb') as f:
    f.write(content)