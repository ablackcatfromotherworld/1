import requests
url = 'https://movie.douban.com/top250?filter='
# response 可以看作是地址响应的数据<对象>
headers={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}
response = requests.get(url=url, headers=headers)
print(response)
# 返回响应体数据
# get 是一种请求方式
# .text 获取对象中的文本内容<str>html
print(response.text)
'''
爬虫项目实现的步骤
1.找数据所对应的地址<链接地址>，数据抓包确认，分析网页性质<静态网页，动态网页>
2.根据地址发送请求，(文字，二进制<图片，视频，音频>，js，css)
3.基于请求的数据，进行数据解析(筛选需要的数据，剔除不需要的数据)
4.数据的保存(本地，数据库)
'''
