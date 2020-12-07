
import matplotlib.pyplot as plt

soc1=[
0,
1,
2,
3,
4,
5,
6,
7,
8,
9,
10,
11,
12,
13,
14,
15,
16,
17,
18,
19,
20,
21,
22,
23,
24,
25,
26,
27,
28,
29,
30,
31,
32,
33,
34,
35,
40,
45,
50,
60,
70,
80,
90,
95,
100
]

soc=[]
i=0;
lensoc= len(soc1);
while(lensoc>0):
    lensoc-=1;
    soc.append(soc1[lensoc]);


vol1=[
2.892,
2.951,
3.01,
3.082,
3.106,
3.131,
3.156,
3.18,
3.205,
3.206,
3.208,
3.209,
3.211,
3.212,
3.217,
3.222,
3.228,
3.233,
3.238,
3.242,
3.247,
3.251,
3.255,
3.259,
3.262,
3.265,
3.269,
3.272,
3.275,
3.277,
3.28,
3.282,
3.284,
3.286,
3.287,
3.295,
3.296,
3.297,
3.297,
3.306,
3.331,
3.331,
3.331,
3.332,
3.347
]

vol=[]
i=0;
lenvol= len(vol1);
while(lenvol>0):
    lenvol-=1;
    vol.append(vol1[lenvol]*1000)

"""
plt.figure();
plt.plot(soc,vol,'b-',lw=1);
plt.grid();
plt.show()
"""
xmajorLocator  = plt.MultipleLocator(10) #将x主刻度标签设置为10的倍数
xmajorFormatter = plt.FormatStrFormatter('%1.1f') #设置x轴标签文本的格式
xminorLocator  = plt.MultipleLocator(2) #将x轴次刻度标签设置为5的倍数
ymajorLocator  = plt.MultipleLocator(50) #将y轴主刻度标签设置为0.5的倍数
ymajorFormatter = plt.FormatStrFormatter('%1.1f') #设置y轴标签文本的格式
yminorLocator  = plt.MultipleLocator(10) #将此y轴次刻度标签设置为0.1的倍数

ax = plt.subplot(111) #注意:一般都在ax中设置,不再plot中设置
plt.plot(soc,vol,'--b*')
#设置主刻度标签的位置,标签文本的格式
ax.xaxis.set_major_locator(xmajorLocator)
ax.xaxis.set_major_formatter(xmajorFormatter)
ax.yaxis.set_major_locator(ymajorLocator)
ax.yaxis.set_major_formatter(ymajorFormatter)
#显示次刻度标签的位置,没有标签文本
ax.xaxis.set_minor_locator(xminorLocator)
ax.yaxis.set_minor_locator(yminorLocator)
ax.xaxis.grid(True, which='minor') #x坐标轴的网格使用主刻度
ax.yaxis.grid(True, which='minor') #y坐标轴的网格使用次刻度

plt.show()