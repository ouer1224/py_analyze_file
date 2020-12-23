

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

'''
####正则表达式,提取猫眼的top100
myheaders={'User-Agent':'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10'}
r=requests.get("https://www.bqkan.com/1_1094/5403177.html",headers=myheaders)
if(r.status_code==200):
    print(r.status_code)
    r.encoding=r.apparent_encoding;
    #print(r.text)
    fp=open('./test.html','w+',encoding='utf-8')
    demo = r.text
    soup = BeautifulSoup(demo, "html.parser")
    fp.write(soup.prettify())
    fp.close();
    txts=soup.find_all('div',id="content", class_='showtxt');
    print(f"noval txt=\n {txts}");
    print(f"end txt=\n {txts[0].text}")
    text=txts[0].text;
    t=text.replace('\xa0'*3,'\n');
    print(f'end = \n {t}')
else:
    print(f"failed!!!={r.status_code}")

'''

'''
####正则表达式,提取笔趣阁
myheaders={'User-Agent':'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10'}
r=requests.get("https://www.bqkan.com/1_1094/5403177.html",headers=myheaders)
if(r.status_code==200):
    print(r.status_code)
    r.encoding=r.apparent_encoding;
    fp=open('./test.html','w+',encoding='utf-8')
    demo = r.text
    soup = BeautifulSoup(demo, "html.parser")
    txts = soup.prettify();
    fp.write(txts)
    fp.close();

'''

'''
txts="""
 <div class="showtxt" id="content">
     <script>
      app2();
     </script>
     <br/>
     <script>
      read2();
     </script>
     帽儿山，位于东林山脉中，山下有一个村子，民风淳朴，以耕田为生，与世隔绝。
     <br/>
     <br/>
     <br/>
     <br/>
     “这不怨我啊，你那什么破香啊，每次点燃都会打雷，好几次都差点霹死我，我躲过了十三次，已经很不容易了。”白小纯可怜兮兮的说道。
     <br/>
     <br/>
     中年修士看着白小纯，半晌无语。
     <br/>
     <br/>
     “既然你这么害怕，为什么还要强行去点香十多次？”中年修士缓缓开口。
     <br/>
     <br/>
     “我怕死啊，修仙不是能长生么，我想长生啊。”白小纯委屈的说道。
     <br/>
     <br/>
     中年修士再次无语，不过觉得此子总算执念可嘉，扔到门派里磨炼一番，或可在性子上改变一二。
     <br/>
     <br/>
     于是略一思索，大袖一甩卷着白小纯化作一道长虹，直奔天边而去。
     <br/>
     <br/>
     “跟我走吧。”
     <br/>
     <br/>
     “去哪？这也太高了吧……”白小纯看到自己在天上飞，下面是万丈深渊，立刻脸色苍白，斧头一扔，死死的抱住仙人的大腿。
     <br/>
     <br/>
     中年修士看了眼自己的腿，无奈开口。
     <br/>
     <br/>
     “灵溪宗。”
     <br/>
     <br/>
     兄弟姐妹们，阔别2个月，你们想不想我啊，我非常想你们！
     <br/>
     <br/>
     这本书，我做了详细的大纲，每次回顾大纲里的情节，都很兴奋，有种燃烧的感觉，我非常满意，明天，正式更新，依旧是中午一章，晚上一章！
     <br/>
     <br/>
     很兴奋，我们已沉寂了数月，如今归来，要……再战起点！
     <br/>
     <br/>
     新书期，兄弟姐妹，别忘了收藏与推荐啊，收藏与推荐至关重要！
     <br/>
     <br/>
     求收藏！！求推荐！！
     <br/>
     <br/>
     让众人知晓，我们……归来了！
     <br/>
     <br/>
     我们的目标，依旧是……点击榜，推荐榜，第一！xh:.181.241.250
     <br/>
     <script>
      app2();
     </script>
     <br/>
     <br/>
     (https://www.bqkan.com/1_1094/5403177.html)
     <br/>
     <br/>
     <script>
      chaptererror();
     </script>
     <br/>
     请记住本书首发域名：www.bqkan.com。笔趣阁手机版阅读网址：m.bqkan.com
    </div>     
"""
pattern=r'class="showtxt" id="content"(.*?)</div>'
searchObj =re.search(pattern,txts,re.DOTALL|re.M|re.I);
content=searchObj.group();
print(content)

pattern=r'<br/>(.*?)<br/>'
searchObj =re.search(pattern,content,re.S)#re.DOTALL|re.M|re.I);
text=searchObj.group(0);
#print(f"text={text}")

res=re.findall(pattern,content,re.S)
#print(f"{type(res)}")
#print(f"{res}")
#print(''.join(res))

'''




####正则表达式,提取笔趣阁
myheaders={'User-Agent':'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10'}
r=requests.get("https://www.bqkan.com/1_1094/",headers=myheaders)
if(r.status_code==200):
    print(r.status_code)
    r.encoding=r.apparent_encoding;
    fp=open('./test.html','w+',encoding='utf-8')
    demo = r.text
    soup = BeautifulSoup(demo, "html.parser")
    txts = soup.prettify();
    fp.write(txts)
    fp.close();

    fp=open('./list.txt','w+',encoding='utf-8')
    pattern=r'<div class="listmain">(.*?)</div>';
    res=re.findall(pattern,txts,re.S);
    #print(f"res={res}")
    str1=res[0];
    fp.write(str1)
    fp.close();

    with open('./list_no_dd.txt','w+',encoding='utf-8') as fp:
        pattern=r'<a (.*?)</a>';
        res=re.findall(pattern,str1,re.S);
        print(len(res))
        fp_listend=open('./list_end.txt','w+',encoding='utf-8');
        flag_save=0;
        for i in res:
            fp.write(i)
            tmp_res=i.split();
            print(tmp_res)
            stra=tmp_res[0];
            pattern=r'href="(.*?)">'
            ref=re.findall(pattern,stra,re.S);
            print(ref[0]+' '+' '.join(tmp_res[1:]))
            if(tmp_res[1]=='章节目录'):
                flag_save=1;
                continue;
            pattern=r'第(.*?)章'
            strb=tmp_res[1];
            matchobj=re.match(pattern,strb);

            if matchobj==None:
                continue;
            if(flag_save==1):
                fp_listend.write('https://www.bqkan.com'+ref[0]+' '+' '.join(tmp_res[1:])+'\n')

        fp_listend.close()

else:
    print("failed to request")













