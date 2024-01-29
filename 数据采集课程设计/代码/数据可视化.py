# 导入所需库
import pandas as pd  # 导入 pandas 库用于数据处理
import pymysql  # 导入 pymysql 用于连接 MySQL 数据库
from pyecharts import options as opts  # 导入 pyecharts 中的选项模块
from pyecharts.charts import Bar  # 导入柱状图模块
from pyecharts.globals import ThemeType  # 导入主题类型

# 连接到 MySQL 数据库
db = pymysql.connect(host='127.0.0.1', user='root', port=3306, password='123456', db='mydb', charset='utf8')

# 创建游标对象
cursor = db.cursor()

# 编写 SQL 查询语句，获取数据
sql = '''select addr,replace(product_price,"元/斤","") price 
         from product_info 
         where product_price like "%元/斤%"'''

# 执行 SQL 查询，获取数据并存入 Pandas DataFrame
cursor.execute(sql)
data = cursor.fetchall()  # 获取所有查询结果
pd.set_option('display.precision', 2)  # 设置 pandas 显示精度
df = pd.DataFrame(list(data), columns=['addr', 'price'])  # 创建 DataFrame 存储查询结果

# 显示 DataFrame 的前 500 行数据
df.head(500)

# 将 'price' 列转换为浮点型，并筛选出小于 100 的值
df["price"] = pd.to_numeric(df["price"], downcast="float")  # 将价格列转换为浮点型
df = df[df.iloc[:, 1] < 100]  # 筛选出价格小于 100 的数据

# 按 'addr' 列分组计算 'price' 列的均值，排序并重置索引
price_mean = df.groupby("addr")['price'].mean().sort_values(ascending=False).to_frame()  # 按地址分组计算价格均值
price_mean.reset_index(inplace=True)  # 重置索引

# 提取前 20 个 'addr' 和相应的 'price' 值
x = list(price_mean['addr'])[0:10]  # 获取前 10 个地址数据
y_tmp = list(price_mean['price'])[0:10]  # 获取前 10 个价格数据
y = [round(num, 2) for num in y_tmp]  # 对价格数据保留一位小数并保存

# 定义一个函数，创建带有次级 y 轴的柱状图
def overlap_bar_line(x, y, title) -> Bar:
    bar = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))  # 初始化柱状图并设置主题
        .add_xaxis(x)  # 设置 x 轴数据
        .add_yaxis("惠农网面粉价格Top10发货地", y, bar_width=35,itemstyle_opts=opts.ItemStyleOpts(color="#5793f3"))  # 设置左侧 y 轴数据
        .extend_axis(
            yaxis=opts.AxisOpts(
                axislabel_opts=opts.LabelOpts(formatter="{value}"), interval=15
            )
        )  # 添加次级 y 轴的设置
        .set_series_opts(label_opts=opts.LabelOpts(is_show=True))  # 在柱状图上显示标签
        .set_global_opts(
            title_opts=opts.TitleOpts(title=title),  # 设置标题
            yaxis_opts=opts.AxisOpts(
                axislabel_opts=opts.LabelOpts(formatter="{value}")
            ),  # 设置左侧 y 轴选项
            xaxis_opts=opts.AxisOpts(
                axislabel_opts=opts.LabelOpts(
                    is_show=True, position="top", color="black", rotate=30, interval=0
                )
            ),  # 设置 x 轴选项
        )  # 设置全局选项
    )

    return bar

# 渲染柱状图，并将其保存为一个 HTML 文件
overlap_bar_line(x, y, "").render("C:/Users/LENOVO/Desktop/数据采集课程设计/bar_chart3.html")
