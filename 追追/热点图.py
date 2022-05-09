encodings = 'utf-8'
import csv

import pandas as pd
import pyecharts.options as opts
from pyecharts.globals import ThemeType
from pyecharts.charts import Map


def r():
    data_pair = []
    with open('2019省市GDP.csv', 'r', encoding='utf-8') as t:
        reader = csv.reader(t)
        counter = 0
        try:
            for line in reader:
                if counter > 1:
                    data_pair.append((line[1], float(line[2])))
                counter += 1
        except(ValueError):
            pass
        finally:
            return data_pair


# data = pd.read_csv('2019省市GDP.csv')
# datas = [(i,j)for i,j in zip(data.index,data.values)]
datas = r()
map = Map(init_opts=opts.InitOpts(width="1000px", height="600px", theme=ThemeType.DARK))
map.add(series_name='2019全国省市GDP', data_pair=datas, center=[109.5, 34.5], is_map_symbol_show=False)
map.set_global_opts(
    title_opts=opts.TitleOpts(
        title="2019年全国GPD情况(单位:亿元) ", subtitle="数据来源:排行榜网站",
        pos_left="center", pos_top="top",
        title_textstyle_opts=opts.TextStyleOpts(font_size=20, color="rgba(255,255,255, 0.9)")))
visual_map_opts = opts.VisualMapOpts(
    is_calculable=True, dimension=0,
    pos_left="30", pos_top="bottom", range_text=["最高", "最低"], range_color=["lightskyblue", "yellow", "red"],
    textstyle_opts=opts.TextStyleOpts(color="#fff"))
map.render("china_2019.html")
