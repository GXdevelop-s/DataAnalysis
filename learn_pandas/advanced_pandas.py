import numpy as np
import pandas as pd

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

# 总结：pandas的多层次索引推荐用pd.MultiIndex.from_product笛卡尔积的方式构建，构建三要素：1.矩阵式数据 2.from_product构建index 3.from_product构建column

# 2.多层次索引元素访问
# 2.1 中括号索引 中阔号索引是可以显式隐式混用的
print(df4['期中'])  # 会拿到期中下所有班级所有人所有科目的成绩（也就是说行索引不变），返回值是一个df
print(df4['期中']['数学'])  # 同样的还是行索引不变，得到一个两层索引的series
print(df4['期中']['数学']['1班'])  # 行索引会变化，只拿到有1班数据的两层索引的series
print(df4['期中']['数学']['1班']['张三'])  # 最终得到单个元素
# 2.2 隐式索引
print(df4.iloc[0, 1])  # 隐式索引是直接对应到最后一层的，是和多层索引无关的，所以多层索引对于隐式索引来说是比较简单的
# 2.3 显式索引
print(df4.loc[('1班', '张三'), ('期中', '数学')])  # 显示索引是要分维度的，行索引单独用括号括起来，列索引也单独用括号括起来，里面再按照一级一级去分

# 3.选择和切片
# 3.1列索引
print(df4['期中'])
print(df4['期中']['数学'])  # 变成series了
print(df4['期中'][['数学']])  # 会保留dataframe的形式
print(df4.iloc[:, 2])  # 行全取，取第三列
print(df4.iloc[:, [1, 3]])  # 行全取，取多列，同样是直接对应到最后一层
print(df4.loc[:, ('期中', '数学')])  ## 行全取，取期中数学，不能直接对应到最后一层
# 3.2行索引
