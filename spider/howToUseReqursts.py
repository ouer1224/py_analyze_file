

import requests
import os
import json
from bs4 import BeautifulSoup
import re
'''
###百度搜索
keyword='python'
try:
    keyval={'wd':keyword};
    r=requests.request("get","http://www.baidu.com/s",params=keyval)
    print(r.url)
    r.raise_for_status();
    r.encoding=r.apparent_encoding;
    #print(r.text);
    print(f"{len(r.text)}")
except:
    print('产生异常');


strtxt=r.text
with open("./test.html",'w+',encoding='utf-8') as fp:
    fp.write(strtxt)

'''

'''
######爬取图片
url='https://pic1.zhimg.com/v2-cde0b40f4780f9d8aad224a1ba5d1517_r.jpg'
path='./'+url.split('/')[-1];

try:
    r=requests.get(url);
    with open(path,'wb') as fp:
        fp.write(r.content)
        print('保存成功')
except IOError as e:
    print(str(e))

'''

'''
####查询IP地址
url="http://www.ip38.com/ip.php?ip="
try:
    r=requests.request('get',url+'104.193.88.77');
    r.raise_for_status()
    r.encoding=r.apparent_encoding;
    print(f"{r.text}")
except IOError as e:
    print(str(e));

'''


'''
#####在线翻译
def get_trans_dat(word=None):
    url="http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule";
    #pos参数放在请求实体里,构建一个新的字典
    form_dat={
        'i':word,
        'from':'AUTO',
        'to':'AUTO',
        'smartresult':'dict',
        'client': 'fanyideskweb',
        'salt': '15569272902260',
        'sign': 'b2781ea3e179798436b2afb674ebd223',
        'ts': '1556927290226',
        'bv': '94d71a52069585850d26a662e1bcef22',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME'
    }
    #请求表单数据
    r=requests.request('post',url,data=form_dat);
    print(r.text)
    content=json.loads(r.text)
    print(content['translateResult'][0][0]['tgt'])
    print(content['translateResult'])

word=input("请输入你要翻译的文字: ");
get_trans_dat(word);
'''



'''

s=BeautifulSoup('<p>hello</p>','html.parser');
print(s.p.string)

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

s=BeautifulSoup(html,'html5lib');
#print(s.prettify())
#print(f"s===={s}")

print('===================')
r = requests.get("http://python123.io/ws/demo.html")
demo = r.text
print(f"demo={demo}")
soup = BeautifulSoup(demo,"html.parser")
print(f"tile={soup.title}") #获取标题
print(f"a={soup.a}") #获取a标签
print(f"tilestr={soup.title.string}")

print(f"a_name={soup.a.name}") #每个<tag>都有自己的名字，通过<tag>.name获取
print(f"p.name={soup.p.name}")
tag = soup.a                        #此处只将第一个a的tag取出来了,第二个a的tag如何取出来
print(f"tag_attrs={tag.attrs}")
print(f"tag_attrs_class=={tag.attrs['class']}")
print(f"tag_attr_href=={tag.attrs['href']}")
print(f"type_tag_attrs=={type(tag.attrs)}")
print(f"type_tag==={type(tag)}")

print("------1-------")
print(soup.a.next_sibling)
print("------2-------")
print(soup.a.next_sibling.next_sibling)
print("------3-------")
print(soup.a.previous_sibling)

#print(soup.prettify()) #输出html标准格式内容
with open('./test.html','w+') as fp:
    fp.write(r.text)
'''


####正则表达式,提取猫眼的top100
myheaders={'User-Agent':'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10'}
r=requests.get("https://book.douban.com/latest?icn=index-latestbook-all",headers=myheaders)
if(r.status_code==200):
    print(r.status_code)
    r.encoding=r.apparent_encoding;
    #print(r.text)
    fp=open('./test.html','w+',encoding='utf-8')
    fp.write(r.text)
    fp.close();
else:
    print(f"failed!!!={r.status_code}")

