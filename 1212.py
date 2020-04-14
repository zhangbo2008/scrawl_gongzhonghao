'''
登录电脑版微信,然后装fiddle,设置好代理,后
浏览公众号,看fiddle抓取的地址.贴过来

只需要得到地址即可.
'''
url='http://mp.weixin.qq.com'

dizhi='/s?__biz=MzA4NDQwNTkzMw==&mid=2650968953&idx=3&sn=a49a0e2865efa17c82202085dbb04e2f&chksm=841188bbb36601ad48de682388e6c4711f86abfae066a32a785144f3e7db14f548f753c54a6a&scene=0&xtrack=1&key=1721249e67c018e4cb10e4f1d6239d0d4f88e2d4c3bf9e4e41099bee31d17c8e83b632aff17bf30b8668c127fd4207caa02e3f7e0e5829208ed810cdb27bac330d07a2227fcc080fe9b80e9e886c687a&ascene=1&uin=Mjg1NDcyMDIyOA%3D%3D&devicetype=Windows+10&version=62080079&lang=zh_CN&exportkey=A8KSVfDEp9b5IHhXO2Lr%2BEo%3D&pass_ticket=ZFpqNdzeoHoU5wMAUkY1Cx0X9BTMCP7XMPJhBh0NbHYxjsLGWGm9YCWJKLMBG1Ug&winzoom=1'



import requests
print(url+dizhi)
tmp=requests.get(url+dizhi,verify=False)

# print(tmp.text)

from bs4 import BeautifulSoup

soup = BeautifulSoup(tmp.text, "html.parser")


print(soup.find_all('div'))