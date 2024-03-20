import numpy as np
import pandas as pd
import matplotlib as plt

# Pandas 层次化索引
# 1 创建多层次索引
# 1.1 隐式构造——最常见的方法是给DataFrame构造函数的index参数传递两个或更多的数组，同理Series也可以
data1 = np.random.randint(0, 100, size=(6, 6))
index1 = [
    ['1班', '1班', '1班', '2班', '2班', '2班'],  # 两个列表是两个不同的层次，连续三个相同的只会显示一个
    ['小x', '小d', '小v', '小e', '小q', '小o']
]
columns1 = [
    ['期中', '期中', '期中', '期末', '期末', '期末'],  # 连续三个相同的只会显示一个
    ['语文', '数学', '英语', '语文', '数学', '英语']
]
df1 = pd.DataFrame(data=data1, index=index1, columns=columns1)

# 2 显示构造 pd.MultiIndex    注意data和多层index之间的数据匹配
# 2.1 使用数组
data2 = np.random.randint(0, 100, size=(6, 6))
index2 = pd.MultiIndex.from_arrays([
    ['1班', '1班', '1班', '2班', '2班', '2班'],  # 连续三个相同的只会显示一个
    ['小x', '小d', '小v', '小e', '小q', '小o']
])
columns2 = [
    ['期中', '期中', '期中', '期末', '期末', '期末'],  # 连续三个相同的只会显示一个
    ['语文', '数学', '英语', '语文', '数学', '英语']
]
df2 = pd.DataFrame(data=data2, index=index2, columns=columns2)

# 2.2使用tuple
data3 = np.random.randint(0, 100, size=(6, 6))
index3 = pd.MultiIndex.from_tuples(
    (
        ('1班', '张三'), ('1班', '李四'), ('1班', '王五'),
        ('2班', '张三'), ('2班', '李四'), ('2班', '王五'),
    )
)
columns3 = [
    ['期中', '期中', '期中', '期末', '期末', '期末'],  # 连续三个相同的只会显示一个
    ['语文', '数学', '英语', '语文', '数学', '英语']
]
df3 = pd.DataFrame(data=data3, index=index3, columns=columns3)

# 2.3使用product  笛卡尔积  （a,b）（c,d）=>(a,c)(a,d)(b,c)(b,d)
data4 = np.random.randint(0, 100, size=(6, 6))
index4 = pd.MultiIndex.from_product([
    ['1班', '2班'],
    ['张三', '李四', '王五']
])
columns4 = pd.MultiIndex.from_product([
    ['期中', '期末'],  # 连续三个相同的只会显示一个
    ['语文', '数学', '英语']
])
df4 = pd.DataFrame(data=data4, index=index4, columns=columns4)
