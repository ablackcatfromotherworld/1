# -*- coding: utf-8 -*-
import re

import requests
url = 'https://www.hexuexiao.cn/a/134274.html'
response = requests.get(url=url)
data = response.text
"""
<a class="btn btn-default btn-xs" href="https://i.hexuexiao.cn/up/49/13/20/7207921acd473789d2b5c0645c201349.jpg.source.jpg" role="button" target="_blank">
                            <i class="fa fa-download" style="color: #999;"></i> 下载本图
                        </a>
"""
"""
<a class="btn btn-default btn-xs" href="(.*?)" role="button".*?
"""
url_img = re.findall('<a class="btn btn-default btn-xs" href="(.*?)" role=.*?', data, re.S)[0]
img_contend = requests.get(url=url_img).content
# 准备图片名字
img_name = url_img.split('/')[-1]
with open('1.jpg', mode='wb') as f:
   f.write(img_contend)