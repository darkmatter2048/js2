from pyecharts.charts import Bar, Map, Line, Pie, Grid, Timeline, WordCloud, Map3D,  MapGlobe  # 导入条形图,地图,折线图,玫瑰图 ,grid并行组图组件
from pyecharts import options as opts # 导入配置项模块
from pyecharts.globals import ThemeType # 导入主题模块
from pyecharts.globals import SymbolType

import csv
import pandas as pd
import numpy as np


# 读取原表文件
with open(r"C:\Users\user\Desktop\反战网站\死亡人数.csv", encoding='utf-8' ) as file:
    reader = csv.reader(file)
    # 存储数据
    l0 = []
    for row in reader:
        l0.append(row)
    # print(l0)

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
years=[str(i)+'年' for i in range(1989,2023)]#x轴必须是字符串类型！

#绘图
t1 = Timeline(init_opts=opts.InitOpts(theme=ThemeType.CHALK,width='1536px',height='700px'))
for i in range(1989,2023):
    piecesC = [
            {"min": 10000, 'color': '#7f1100'},
            {"min": 1000, "max": 9999, 'color': '#bd1316'},
            {"min": 500, "max": 999, 'color': '#e64b45'},
            {"min": 100, "max": 499, 'color': '#ff8c71'},
            {"min": 1, "max": 99, 'color': '#fdd2a0'},
            {"max": 1}
        ]
    
    #柱状图
    bar = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
    .add_xaxis(cbar(SW,str(i))[0])
    .add_yaxis("product1", cbar(SW,str(i))[1], stack="stack1", category_gap="50%")
    .set_global_opts(title_opts=opts.TitleOpts(title='柱状图-折线图',
                                                pos_left='7%', pos_top='5%',
                                                title_textstyle_opts=opts.TextStyleOpts(font_size=14,color='cyan'),
                                                is_show=True,
                                            ),
                legend_opts=opts.LegendOpts(is_show = False),
                datazoom_opts=opts.DataZoomOpts(is_show=True, range_start=0, range_end=20, pos_top='43%', ),
                xaxis_opts=opts.AxisOpts(name='',
                                        type_='category',  # 轴的类型
                                        name_location='center',  # 坐标轴轴名称的位置
                                        name_gap=10,  # 坐标轴轴名称距离轴线的距离
                                        axislabel_opts=opts.LabelOpts(color='white', is_show=True),
                                        # 坐标轴标签的颜色

                                        axistick_opts=opts.AxisTickOpts(is_show=True,  # 是否显示坐标轴刻度线
                                                                        is_inside=True,  # 刻度线是否朝内
                                                                        # 坐标轴刻度线的样式
                                                                        linestyle_opts=opts.LineStyleOpts(
                                                                            color='cyan')),
                                        axisline_opts=opts.AxisLineOpts(symbol=['none', 'arrow'],
                                                                        # 坐标轴的箭头的方向
                                                                        # 坐标轴轴线的颜色
                                                                        linestyle_opts=opts.LineStyleOpts(
                                                                            color='cyan'))
                                            ),
                yaxis_opts=opts.AxisOpts(name='人数',  # x轴的名称
                                        type_='value',  # 轴的类型
                                        name_location='center',  # 坐标轴轴名称的位置
                                        name_gap=10,  # 坐标轴轴名称距离轴线的距离
                                        axislabel_opts=opts.LabelOpts(color='cyan', is_show=False),
                                        # 坐标轴标签的颜色
                                        axistick_opts=opts.AxisTickOpts(is_show=True,  # 是否显示坐标轴刻度线
                                                                        is_inside=True,  # 刻度线是否朝内
                                                                        # 坐标轴刻度线的样式
                                                                        linestyle_opts=opts.LineStyleOpts(
                                                                            color='cyan')),
                                        axisline_opts=opts.AxisLineOpts(symbol=['none', 'arrow'],
                                                                        # 坐标轴的箭头的方向
                                                                        # 坐标轴轴线的颜色
                                                                        linestyle_opts=opts.LineStyleOpts(
                                                                            color='cyan'))
                                            ),
                # ----- 视觉映射配置项目
                visualmap_opts=opts.VisualMapOpts(is_piecewise=True,
                                                    is_show=False,
                                                    range_text=['Highe', 'Low'],
                                                    textstyle_opts=opts.TextStyleOpts(color='cyan'),

                                                    # 设置分段颜色
                                                    max_=100000,  # 最大值
                                                    pos_right='1%',
                                                    pos_top='center',
                                                    pieces=piecesC,
                                                    ),
                            )
    # .render("stack_bar_percent.html")
    )

    #折线图
    line = (
    Line()
    .set_global_opts(title_opts=opts.TitleOpts(title='折线图',
                                            pos_left='8%',
                                            title_textstyle_opts=opts.TextStyleOpts(font_size=14),pos_top='49%',
                                            is_show=True),
                                            
        xaxis_opts=opts.AxisOpts(type_="category"),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
        legend_opts=opts.LegendOpts(is_show = False),
    )
    .add_xaxis(xaxis_data=years)
    .add_yaxis(
        series_name="",
        y_axis=zrs,
        symbol="emptyCircle",
        is_symbol_show=True,
        label_opts=opts.LabelOpts(is_show=False),
    )
    .set_global_opts(
                    title_opts=opts.TitleOpts( 
                                        pos_left='8%',
                                        title_textstyle_opts=opts.TextStyleOpts(font_size=14),pos_top='49%'),
                    xaxis_opts=opts.AxisOpts(name='日期',
                                            name_gap=20,
                                            name_textstyle_opts=opts.TextStyleOpts(color='cyan',
                                                                                    font_size=10),
                                            axislabel_opts=opts.LabelOpts(color='cyan'),
                                            axisline_opts=opts.AxisLineOpts(is_show=True,
                                                                            symbol=['none', 'arrow'],
                                                                            linestyle_opts=opts.LineStyleOpts(
                                                                                color='cyan')),
                                            ),
                    yaxis_opts=opts.AxisOpts(name='人数',
                                            min_=0,
                                            name_location='center',
                                            name_gap=10,
                                            name_textstyle_opts=opts.TextStyleOpts(color='cyan',
                                                                                    ),
                                            axislabel_opts=opts.LabelOpts(color='cyan',is_show=False),
                                            axisline_opts=opts.AxisLineOpts(is_show=True,
                                                                            #  设置轴线的颜色
                                                                            linestyle_opts=opts.LineStyleOpts(
                                                                                color='cyan'),symbol=['none', 'arrow']),
                                            ),
                    tooltip_opts=opts.TooltipOpts(trigger='axis', axis_pointer_type='cross'),
                    axispointer_opts=opts.AxisPointerOpts(is_show=True,
                                                        label=opts.LabelOpts(color='black',
                                                                            font_size=12,
                                                                            font_family='SimHei')),
                    legend_opts=opts.LegendOpts(is_show=True,pos_bottom='44%',pos_left='4.5%'),
                    )
        .set_series_opts(linestyle_opts=opts.LineStyleOpts(color='pink',
                                                            width=2,
                                                                       ))
    # .render("basic_line_chart.html")
    )

    #饼图
    x_data = cbar(SW,str(str(i)))[0]
    y_data = cbar(SW,str(str(i)))[1]
    data_pair = [list(z) for z in zip(x_data, y_data)]
    data_pair.sort(key=lambda x: x[1])
    pie = (Pie(init_opts=opts.InitOpts(theme=ThemeType.DARK))
            .add('', data_pair,
                radius=['40', '100'],
                rosetype='area',
                center=['85.8%', '50%'],
                label_opts=opts.LabelOpts(formatter="{b}:{c}人"),
                
                )
            .set_global_opts(title_opts=opts.TitleOpts(title='战争热点',
                                                      pos_right='12%',
                                                      title_textstyle_opts=opts.TextStyleOpts(font_size=14,color='yellow'),
                                                      pos_top='49%'),
                            legend_opts=opts.LegendOpts(is_show=False))

           )
    
    # #词云
    # couldword = (
    #         WordCloud(init_opts=opts.InitOpts(theme=ThemeType.CHALK,))
    #             .add('', data_pair=SW[str(i)], word_size_range=[20, 60],
    #                  textstyle_opts=opts.TextStyleOpts(font_family='Microsoft YaHei', font_weight='bold', ),
    #                  pos_left='70%', pos_right='1%', pos_top='1%', pos_bottom='63%', height='335px', width='500px',
    #                  shape='square')
    #             .set_global_opts(title_opts=opts.TitleOpts(title="战争热点",
    #                                                        title_textstyle_opts=opts.TextStyleOpts(font_size=15),pos_right='12%',
    #                                                        pos_top='2.5%'))
    #     )

    #地图
    map = (
        Map(init_opts=opts.InitOpts(theme=ThemeType.CHALK))
        .add("该年死亡人数", SW[str(i)], "world",
             is_roam=False,
             label_opts=opts.LabelOpts(color='#fcfcfc', font_weight='bold', font_size=12,
                                                font_family='SimHei'), is_map_symbol_show=False)
        .add("累计的死亡人数", eval(LJ[str(i)]), "world",
             is_roam=False,
             label_opts=opts.LabelOpts(color='#fcfcfc', font_weight='bold', font_size=12,
                                                font_family='SimHei'), is_map_symbol_show=False)
        
        .set_global_opts(title_opts=opts.TitleOpts(title='历年世界战争死亡人数',pos_left='center',
                                                title_textstyle_opts=opts.TextStyleOpts(font_size=20,color='red'),
                                                subtitle_textstyle_opts=opts.TextStyleOpts(font_size=18,),
                                                pos_top='1%'),
            datazoom_opts=opts.DataZoomOpts(), 
            legend_opts=opts.LegendOpts(pos_top='7%',
            textstyle_opts=opts.TextStyleOpts(color='white'),
            is_show=True,selected_mode=''),
            visualmap_opts=opts.VisualMapOpts(is_piecewise=True, pieces=piecesC, pos_left='23%',
                pos_top='60%',
                textstyle_opts=opts.TextStyleOpts(color='white')),
            
        )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    )

    #排版整合
    grid = (Grid(init_opts=opts.InitOpts(theme=ThemeType.CHALK, width='1536px',height='672px'))
                .add(bar,
                     grid_opts=opts.GridOpts(pos_left='2.6%',pos_right='77.6%',pos_top='11.5%',pos_bottom='57%'),
                     is_control_axis_index=True,
                 )
                .add(line,
                     grid_opts=opts.GridOpts(pos_left ='2.6%', pos_right = '77.6%', pos_top ='57%', pos_bottom = '10.5%'),
                 )
                .add(pie,
                 grid_opts=opts.GridOpts()
                 )
                .add(map,
                 grid_opts=opts.GridOpts(is_contain_label=True))
                # .add(couldword,grid_opts=opts.GridOpts())
            )
    t1.add(grid, i)
    t1.add_schema(play_interval=350,
                #   is_loop_play=False,
                  orient='horizontal',
                  pos_left='8%',
                  pos_bottom='0.8%',
                  pos_right='10%')
t1.render("世界战争死亡人数可视化.html")