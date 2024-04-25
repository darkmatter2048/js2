import csv
import pandas as pd
import numpy as np
from pyecharts.charts import Bar, Map, Line, Pie, Grid, Timeline, WordCloud, Map3D,  MapGlobe  # 导入条形图,地图,折线图,玫瑰图 ,grid并行组图组件
from pyecharts import options as opts # 导入配置项模块
from pyecharts.globals import ThemeType # 导入主题模块

# 读取原表文件
with open(r"C:\Users\user\Desktop\反战网站\死亡人数.csv", encoding='utf-8' ) as file:
    reader = csv.reader(file)
    # 存储数据
    l0 = []
    for row in reader:
        l0.append(row)
    
print(l0[0:30])

#每年的数据        
SW={}
year='1988'
l1=[]
for k in l0:
    if k[0]==year:
        l1.append([k[2],k[1]])
    else:
        if year != '1988':
            SW[year]=l1
            l1=[]
            l1.append([k[2],k[1]])
        year=str(int(year)+1)
        # print(year)
SW['2022']=l1
# print(SW['1990'])
# print(SW['1989'])

#累积的数据
LJ={}
year='1988'
l2=[]
for k in l0:
    if k[0]==year:
        l2.append([k[2],k[1]])
    else:
        if year != '1988':
            LJ[year]=str(l2)#列表是可变序列！所以这一步转化为字符串
            l2.append([k[2],k[1]])
        year=str(int(year)+1)
LJ['2022']=str(l2)
# print(LJ['1989'])

#柱状图数据处理
def cbar(dict,i):
    bar_l=dict[i]
    x=[]
    y=[]
    for l in bar_l:
        x.append(l[0])
        y.append(l[1])
    y=[int(num) for num in y]
    return x,y    
# print(cbar(SW,'1990'))   

#折线图数据处理
line_l0=LJ.values()
zrs=[]#1989-2022累计因战争死亡总人数
for m in line_l0:
    m=eval(m)
    num=0
    for v in m:
        num += int(v[1])
    zrs.append(num)
years=[i for i in range(1989,2023)]





    