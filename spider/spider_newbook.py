

import requests
import os
import json
from bs4 import BeautifulSoup
import re


url='https://jrjpc.com/'
dat_re_get=requests.request('get',url);
dat_re_get.raise_for_status()
#print(dat_re_get.text)

soup=BeautifulSoup(dat_re_get.text,'html.parser');
#print(soup.prettify())
temp_html=soup.prettify()

with open('./tmp_html.txt','w+',encoding='utf-8') as file_temp_html:
    file_temp_html.write(temp_html)

pattern=r'<h4 class="item-heading text-ellipsis">.*?href="(.*?)target="_blank">(.*?)<span.*?</h4>.*?<p class="item-excerpt.*?>(.*?)</p>'
res=re.findall(pattern,temp_html,re.S);

fp_newbook=open('./new_book.txt','w+',encoding='utf-8')
for tmp_dat in res:
    dat_noSpace=re.sub(r'\n\s{1,}','',tmp_dat[1])
    #print(dat_noSpace)
    tmp_res=re.match(r'《(.*?)》',dat_noSpace)
    print(tmp_res.group(1))
    jianjie=re.sub(r'\s{1,}','',tmp_dat[2])
    fp_newbook.write(str(tmp_res.group(1))+'\n'+str(tmp_dat[0])+'\n'+str(jianjie)+'\n')
fp_newbook.close()

