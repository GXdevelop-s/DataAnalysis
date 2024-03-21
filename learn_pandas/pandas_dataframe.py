'''
DataFrame是一个表格型的数据结构，可以看作时由Series组成的字典
设计的初衷时将Series的使用场景从一维拓展到多维，DataFrame既有行索引，也有列索引
DataFrame的基本属性和方法：
行索引：index
列索引：columns
值：values （numpy的二维数组）
shape：形状
head()：查看前几条数据，默认五条
tail()：查看后几条数据，默认五条
'''
import numpy as np
import pandas as pd

# 1.创建DataFrame
# 1.1用一个字典来创建，字典的key键作为每一列的名称，DataFrame会自动加上每一行的索引
d1 = {
    'name': ['a', 'b', 'c'],
    'age': [1, 2, 3]
}
df = pd.DataFrame(d1)

# 1.2 创建DataFrame的其他方式
# 设置index、columns
df.index = list('ABC')
df.columns = ['name2', 'age2']
df2 = pd.DataFrame(d1, index=list('abc'))
df3 = pd.DataFrame(
    data=np.random.randint(10, 100, size=(2, 2)),
    index=['小红', '小明'],
    columns=['年龄', '成绩']
)

# 2 DataFrame索引
# 中括号式索引（默认是先取列索引）
print(df3.小红)  # 得到一个Series
print(df3['小红'])  # 同上
print(df3[['小红']])  # 得到一个DataFrame
print(df3['小红', '小明'])  # 这必然是一个DataFrame
print(df[0])  # 注意此处选择的是数据的第一列
print(df[1:4])  # 注意此时用的是行切片1-3行，其他情况的中括号索引都是列

# loc&iloc索引
# 使用 .loc 显式索引
print(df.loc['x'])  # 选择行标签为 'x' 的行，返回值是一个Series，index是df的columns
print(df.loc['x', 'A'])  # 选择行标签为 'x'、列标签为 'A' 的元素，如果有多个元素，则返回Series
print(df.loc[['x', 'y'], ['A', 'B']])  # 选择行标签为 'x' 和 'y'、列标签为 'A' 和 'B' 的数据（四个元素），返回值是一个DataFrame，这不是切片而是选择
print(df.loc['start_row':'end_row', 'start_column':'end_column'])  # 这是切片，标签切片是左闭右闭!!! 返回值是一个dataframe

# 使用 .iloc 隐式索引
print(df.iloc[0])  # 选择索引为 0 的行
print(df.iloc[0, 0])  # 选择行索引为 0、列索引为 0 的元素
print(df.iloc[0:2, 0:2])  # 位置切片是左闭右开!!!；选择行索引为 0 到 1、列索引为 0 到 1 的数据 返回值是一个dataframe

# 使用 .at    该方法只适用于快速访问单个元素，不能访问多个元素且不能切片;这在需要高性能的情况下非常有用，特别是在处理大型数据集时
print(df.at['row_label', 'column_label'])

# 3 DataFrame的运算
'''
在运算中自动对齐不同索引的数量
如果索引不对应，则补NaN
DataFrame没有广播机制
'''
df4 = pd.DataFrame(
    data=np.random.randint(0, 100, size=(3, 3)),
    index=['小明', '小红', '小黄'],
    columns=['语文', '数学', '英语']
)
# DataFrame和标量之间的运算
print(df4 + 100)
print(df4 - 100)
print(df4 * 100)
print(df4 / 100)
print(df4 % 100)
print(df4 ** 2)  # 平方
# DataFrame之间的运算
df34 = df3 + df4  # 对应元素相加
df14 = df + df4  # 不对应的元素相加，空的地方用NaN补齐
df.add(df4, fill_value=80)  # 非要填充起来可以用add函数，其中fill_value可以实现操作，填充之后再相加
df.divide(df3, fill_value=2)  # 除法
s = pd.Series([100, 10, 1], index=df4.columns)
print(df4 + s)  # df的每一行都加上一个s，直接相加默认是按照Series的index对应df4的column相加的
print(df4.add(s, axis='columns'))  # 按columns相加
print(df4.add(s, axis=1))  # 按columns相加 ；若是axis为0，则s的index匹配不了df4的index，就会给df4的index新加上s的index，元素全是NaN
s2 = pd.Series([100, 10, 1], index=df4.columns)
print(df4.add(s, axis=0))  # 按照index相加

# 4 遍历DataFrame
'''
遍历是低效的，最符合Pandas使用逻辑的是向量化的操作
但是为了实现元素级别上的操作，可以用以下三种方法
1.apply()方法在行上或列上应用一个函数  这比向量化慢但是比迭代要块
2.applymap()方法在DataFrame的每个元素上应用一个函数
3.布尔索引也可以被视为一种向量化的元素级操作，可以使用它来选择满足特定条件的元素
'''

# 4.1 使用迭代器按行遍历，使用 iterrows()方法；iterrows() 返回一个迭代器，允许你遍历 DataFrame 的每一行
for index, row in df.iterrows():
    # 迭代每行
    print(f'Row index: {index}')
    print(f'Row data:\n{row}\n')
    for column in df.columns:
        # 每行再迭代行内元素
        element = row[column]
        print(f'Row index: {index}, Column name: {column}, Value: {element}')

# 4.2 使用迭代器按行遍历，使用 itertuples()方法；itertuples() 方法返回一个迭代器，允许你遍历 DataFrame 的每一行，每次迭代返回一个命名元组，其中包含行的索引和数据。
for row in df.itertuples():
    print(f'Index: {row.Index}')
    print(f'Row data - A: {row.name2}, B: {row.age2}')  # 忽略报错代码没问题
    for value in row:
        # 迭代行内元素
        print(f'Value: {value}')

# 4.3 使用列名并直接遍历并返回元素
'''
外层循环直接写了for column in df 而不是 in df.column ,这是因为当你直接遍历DataFrame对象时，默认就是按列遍历的
而内层循环则是需要写in df.index
'''
for column in df:
    for index in df.index:
        element = df.at[index, column]

# 4.4 使用iteritems()方法按行遍历访问元素，该方法专门用来遍历列，迭代器每次迭代返回的键值对是列名和Series形式的列数据
for column_name, series in df.iteritems():
    for index, element in series.items():
        # 在这里，'element'是具体的元素，'index'是行索引
        pass
