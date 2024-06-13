import numpy as np
import pandas as pd
import pymysql
from sqlalchemy import create_engine  # 就是一个orm，能pythonic的操作数据库

if __name__ == '__main__':
    # 1.数据分组聚合
    '''
    数据聚合是数据处理的最后一步，通常是要使每一个数组生成一个单一的数值
    数据分类处理：
        分组：先把数据分成几组
        用函数处理：为不同组的数据应用不同的函数以转换数据
        合并：把不同组得到的结果合并起来
    '''
    df1 = pd.DataFrame({
        'color': ['red', 'blue', 'green', 'green', 'red', 'red', 'yellow'],
        'price': [3, 7, 1, 9, 3, 7, 8]
    })
    # 按color进行分组
    grouped = df1.groupby(
        by='color')  # 返回的是一个DataFrameGroupBy对象，这个对象本身并不是一个DataFrame，而是一个包含多个组的中间对象，每个组都是原始df分组列值相同的那些行。
    print(grouped)  # 结果是<pandas.core.groupby.generic.DataFrameGroupBy object at 0x103097070>
    print(grouped.groups)  # groups用来查看分组情况，目前是每个color中所含的index值，因为对price还没有做处理
    # 遍历每个分组
    for name, group in grouped:
        # print(name)
        # print(group)    # 这是个df，说明遍历GroupBy对象，每个元素是一个dataframe
        pass
    # 分组+聚合
    r1 = df1.groupby(by='color').sum()  # 按照color分组，对price求和，因为只有price有值，返回值是一个dataframe
    # 练习
    # 1对ddd进行聚合操作，求出颜色为白色的价格总和
    # 2对ddd进行聚合操作，分别求出萝卜的所有重量和平均价格
    # 3使用merge合并总重量和平均价格
    ddd = pd.DataFrame(
        data={
            'item': ["萝卜", "白菜", "辣椒", "冬瓜", "萝卜", "白菜", "辣椒", "冬瓜"],
            'color': ["白", "青", "红", "白", "青", "红", "白", "青"],
            'weight': [10, 20, 10, 10, 30, 40, 50, 60],
            'price': [0.99, 1.99, 2.99, 3.99, 4, 5, 6, 7]
        }
    )
    # 1  解法1:分组后再按price求和  解法2:查询出所有白色的行，再聚合
    s_group_ddd = ddd.groupby(by='color')['price']  # DataframeGroupBy取单列是SeriesGroupBy
    d_group_ddd = ddd.groupby(by='color')[['price']]  # DataframeGroupBy取多列是DataframeGroupBy
    white_total = s_group_ddd.sum()['白']  # XxxGroupBy对象聚合之后就会变成Xxx
    print(white_total)

    # 2
    carrot_weight = ddd.groupby(by='item')[['weight']].sum()
    print(carrot_weight)
    carrot_avg_price = ddd.groupby(by='item')[['price']].mean()
    print(carrot_avg_price)

    # 3
    merge_r = carrot_weight.merge(carrot_avg_price, left_index=True, right_index=True)
    print(merge_r)

    # 2.mysql加载数据
    data = np.random.randint(0, 100, size=(5, 5))
    df2 = pd.DataFrame(data=data)
    # 连接mysql，也就是创建数据库连接对象
    conn = create_engine('mysql+pymysql://username:password@127.0.0.1:3306/db')
    # df.to_sql()保存到MySql
    df2.to_sql(
        name='',  # 表名
        con=conn,  # 数据库连接对象
        if_exists='append',  # 如果表存在就追加数据
        index=False  # 是否保存行索引
    )
    # 从MySql中加载数据
    pd.read_sql(
        'select * from table1',
        con=conn,  # 数据库连接对象
        index_col='x'  # 行索引用哪一个字段
    )
