# 爬取网站数据
import pandas as pd

rank = pd.read_html('https://www.phb123.com/city/GDP/37038.html')
rank[0].set_index(0, inplace=True)
print(rank[0].iloc[:154, :4])
rank[0] = rank[0].iloc[:, :4]
rank[0].to_csv("2019省市GDP.csv", encoding='utf_8_sig')
print("finish")

# 清洗数据（将该年份没有数据的城市删去）
data = pd.read_csv('2019省市GDP.csv', nrows=25, usecols=['1', '2'])
data = data.dropna()
print(data)
data.to_csv('2019有数据省市GDP.csv')

# 数据可视化1（将19年城市GDP进行排名并用柱状图显示）
import pyecharts.options as opts
from pyecharts.charts import Bar

data = pd.read_csv('2019有数据省市GDP.csv')
x = [z for z in data['1']]
y = [z for z in data['2']]
bar = (
    Bar(opts.InitOpts(width="1200px", height='600px'))
        .add_xaxis(x)
        .add_yaxis('2019上半年GDP（亿元 ）', y, category_gap='50%')
        .set_global_opts(
        title_opts=opts.TitleOpts(title='2019年GDP排行', pos_left='center'),
        xaxis_opts=opts.AxisOpts(type_='category', axislabel_opts=opts.LabelOpts(rotate=-45)),
        yaxis_opts=opts.AxisOpts(min_=0, max_=16000, interval=1000),
        legend_opts=opts.LegendOpts(is_show=False)
    )
        .render('bar.html')
)

# from pyecharts.charts import Map
# datafile =r"C: Users125892DesktopEE # TÄHh 7.csv"
# data =pd.read_csv (datafile,encoding='gbk')
# print(data)
# attr=data['1']
# value=data['2']
# map=Map("2019年各省市GDP排行" , title_color="#2E2E2E",title_text_size=24,title_top=20, title_pos="center", width=1200, height=800,background_color='white')
# map.add("" ,attr,value)
# map.show_config()
# map.render (path="2019全国GDP.html")
