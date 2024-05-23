'''
pandas是基于numpy的一种工具，为解决数据分析任务而创建
pandas的主要数据结构是series（一维数据）和dataframe二维数据
处理数据：数据整理与清洗、数据分析与建模，数据可视化
'''
import numpy as np
import pandas as pd

if __name__ == '__main__':
    # series是一种类似于一维数组的对象，由下面两个部分组成
    # values：一维数据     index：相关的数据索引标签
    # 1.series创建
    # 1.1 由列表和numpy数组创建，默认索引为0~N-1的整数型索引,索引不一定是数字也不一定从零开始，可以改变
    li1 = [11, 22, 33, 44]
    s1 = pd.Series(li1)
    n = np.array(li1)
    s2 = pd.Series(n)  # 除了dtype不一样，其他的都一样
    print(s1.values)  # ndarray的一维数组
    print(s1.index)  # 索引
    # 修改索引
    s1.index = ['A', 'B', 'C', 'D']
    s2.index = list('BCDE')
    # 通过index获取值,数字的索引要用中括号
    print(s1.A)
    print(s1['A'])
    print(s2.B)
    print(s2['B'])

    # 由字典创建 key是索引，value是value
    dict1 = {
        'a': 11,
        'b': 22,
        'c': 33,
        'd': 44
    }
    s3 = pd.Series(dict1)
    dict2 = {
        'a': np.random.randint(1, 10, size=(2, 3)),
        'b': np.random.randint(1, 10, size=(2, 3)),
        'c': np.random.randint(1, 10, size=(2, 3)),
        'd': np.random.randint(1, 10, size=(2, 3))
    }
    s4 = pd.Series(dict2)
    s5 = pd.Series([1, 2, 3], index=['李白', '鲁班', '杜甫'], name='历史人物')

    # 2 Series的索引
    # 2.1 显示索引（基于标签选择）
    # · 使用index中的元素作为索引值
    # · 使用.loc[] 推荐
    s6 = pd.Series({'python': 150, 'numpy': 100, 'pandas': 130})
    print(s6['python'])  # 值
    print(s6.numpy)
    print(s6[['python', 'numpy']])  # 这样使用两个中括号取出来的还是一个Series，一次取多个数据
    print(s6[['python']])
    # 使用loc[]
    print(s6.loc['python'])  # 值
    print(s6.loc[['python', 'numpy']])
    print(s6.loc[['pandas']])

    # 2.2 隐式索引（即不使用index，使用数字下标）（基于位置选择）
    print(s6[0])
    print(s6[[0, 2]])
    print(s6[[0]])
    # 使用 iloc[],注意不能与混用
    print(s6.iloc[0])
    print(s6.iloc[[0, 2]])
    print(s6.iloc[[0]])

    # 3 Series的切片
    # 3.1 隐式切片：左闭右开
    print(s6[1:4])
    print(s6.iloc[1:4])
    # 3.2 显示切片：左闭右闭
    print(s6['python':'pandas'])
    print(s6.loc['python':'pandas'])

    # 4 Series的基本属性和方法
    # 属性 shape形状 size元素个数  index索引 value值 name名字
    # 方法 head()查看前几条数据，默认五条  tail()查看后几条数据，默认5条  取值顺序不变，返回值是一个Series
    dict3 = {
        'a': 11,
        'b': 22,
        'c': 33,
        'd': 44,
        'e': 55,
        'f': 66,
        'g': 77
    }
    s7 = pd.Series(dict3)
    s7.head(2)  # 查看前2条数据
    s7.tail()

    # 5 检测数据缺失
    # pd.isnull()   pd.notnull()   isnull()   notnull()
    s8 = pd.Series(['ZHANGSAN', 'LISI', 'WANGWU', np.nan])
    s8.isnull()  # 判断是否为空,返回值是一个Series，index没变，values会变成True 或者False，dtype为bool
    pd.isnull(s8)  # 同上
    s8.notnull()  # 判断是否不为空,返回值是一个Series，index没变，values会变成True 或者False，dtype为bool
    pd.notnull(s8)  # 同上
    # 5.1 通过bool值索引过滤数据
    # 过滤空置
    selected_s8 = s8[[True, False, False, False, True, True, True]]  # 用bool值做索引，写True的位置保留，写False的位置删除
    # 根据这个原理和检测数据值缺失的函数
    condi1 = s8.isnull()
    full_data_s8 = s8[~condi1]  # condi1中空值是True，所以~取反True和False；之后将condi1放到索引出就完成了空值的过滤

    # 6 Series的运算
    # 6.1 适用于numpy的运算也适用于Series
    # 基本运算
    s7 + 100
    s7 / 100
    s7 // 2
    s7 ** 2
    s7 % 2
    # 6.2 Series之间的运算，不论位置，只论索引
    # 在运算中自动对齐索引
    # 如果索引不对应，则补NaN
    # Series没有广播机制
    s9 = pd.Series(np.random.randint(10, 100, size=3))
    s10 = pd.Series(np.random.randint(10, 100, size=3))
    s910 = s9 + s10  # 对应元素相加（本质是索引的顺序相同）
    s11 = pd.Series(np.random.randint(10, 100, size=4))
    s911 = s9 + s11  # 没有的元素会为NaN
    # 若修改了索引顺序， 则按照索引相加（而不是按照顺序对应相加）
    new_s9 = s9[1, 2, 0]  # 调整s9的索引顺序
    s109 = s9 + s10  # s109和s910的结果是不一样的
    # 若想保留所有的index，则需要使用add()函数
    s9.add(s11, fill_value=0)  # s9没有的位置，用0填充

    # 7 遍历Series
    # 7.1使用for循环遍历
    for value in s9:
        print(value)
    # 7.2 使用Pandas提供的迭代器
    for index, value in s9.items():
        print('Index: {}, Value: {}'.format(index, value))
