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
print(df4.loc['1班', '期中'])  # 都是同一级且是最高层索引就直接写不用括号了

# 3.选择
# 3.1列索引
print(df4['期中'])
print(df4['期中']['数学'])  # 变成series了
print(df4['期中'][['数学']])  # 会保留dataframe的形式
print(df4.iloc[:, 2])  # 行全取，取第三列
print(df4.iloc[:, [1, 3]])  # 行全取，取多列，同样是直接对应到最后一层
print(df4.loc[:, ('期中', '数学')])  # 行全取，取期中数学，不能直接对应到最后一层
# 3.2行索引
print(df4.loc['2班'])
print(df4.loc['2班'].loc['张三'])  # 这里注意，如果是 df4.loc['2班']['张三'] 会报错的，因为单独的[]默认是取列的，所以要再次loc
print(df4.loc['2班', '张三'])  # 这和上面的结果是一样的
print(df4.loc[('2班', '张三')])  # 也可以看作一个整体，为了保持一致性推荐这种写法

print(df4.iloc[1])  # 返回第一行，返回值是series
print(df4.iloc[[1]])  # 选择多个（两个中括号套在一起的本质是取多个），这里是第一行，就可以保持dataframe
print(df4.iloc[[1, 3, 0]])  # 选择多个
# ！！！写法很多，别去背，多尝试，主要是要搞清楚三种索引的区别再哪，以及索引和选择/切片的不同是什么，别混淆！！！

# 4 切片(建议使用隐式索引)
# 4.1 行切片
print(df4.iloc[1:4])  # 左闭右开区间
print(df4.loc[('1班', '李四'):('2班', '李四')])  # 因为是显示索引，所以不能直接对应到最后一行，必须要用（）分层，这里就是‘1班李四’这一行一直到‘2班李四’这一行
print(df4.loc['1班':'2班'])  # 多级的切片是需要打圆括号分级，但是同级的切片只需要直接：就行了
# 4.2 列切片  （列切片之前要先对行进行切片）
print(df4.iloc[:, 1:5])
print(df4.iloc[:, '期中':'期末'])  # 最高一层可以这么做
print(df4.iloc[:, ('期中', '数学'):('期末', '数学')])  # 这是不ok的！！！！！！！！！❌，只有列切片才能这样

# 5索引的堆叠 stack() unstack()
# 5.1 stack() 将列索引变成行索引
df4.stack()  # 默认是将最里层的列索引变成行索引
df4.stack(level=-1)  # 默认level为-1 最外层的列索引是第0层，向里依次为第1层、第2层.... 第-1层代表最里面一层
df4.stack(level=1)  # 所以当只有两层的时候-1层就是1层，level等于几就变哪一层的列索引为行索引

# 5.2 unstack() 将行索引变成列索引
df4.unstack()  # 相当于还原stack的操作，但是顺序会变，默认是变到列索引的最里面一层
df4.unstack(level=-1)  # 默认level为-1 最外层的列索引是第0层，向里依次为第1层、第2层.... 第-1层代表最里面一层
df4.unstack(level=1)  # 显然level的划分和stack一样

# 5.3 索引堆叠带来的维度问题和fill_value
# 索引堆叠不是简单的索引“转置”，而是维度的叠加，即将列索引的维度叠加到行索引的最后一个维度上或者反过来，势必就会出现没有对应值的问题会出现空值
# 所以需要fill_value的填充值
df4.unstack(fill_value=0)  # 维度不匹配出现的空值由0来填充

# 6聚合操作sum mean max
# 6.1sum 求和
t_df = df4.loc['1班', '期中']  # 取到1班同学的期中各科成绩，是一个dataframe
t_df.sum()  # 求和
t_df.sum(axis=0)  # 默认axis是0，0代表的是行，即求每一列中多行的和
t_df.sum(axis=1)  # 即求每一行中多列的和
t_df.values.sum()  # 这样就是求所有数的和
# 多层索引求和
df4.sum(axis=0)  # 多层索引的求和默认也是求列索引（指最里面一列）的和
df4.sum(axis=1)  # 求行索引（指最里面一行）的和
# 多层索引求和可以有两个 axis（行or列） level （哪一层）
df4.sum(axis=0, level=0)    # axis为0说明是列索引，level说明求和的时候是最外层列索引对每行求和

# mean求平均值
t_df.mean()
t_df.max()
