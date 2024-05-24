import pandas as pd
import numpy as np


def make_df(indexs, columns):
    data = [[str(j) + str(i) for j in columns] for i in indexs]
    df = pd.DataFrame(data=data, index=indexs, columns=columns)
    return df


if __name__ == '__main__':
    df = make_df([1, 2, 3, 4, 5], list('ABCD'))
    # 1.数据合并 pd.concat() pd.append() pd.merge()
    # 1.1 简单级联
    df1 = make_df([1, 2], ['A', 'B'])
    df2 = make_df([3, 4], ['A', 'B'])
    c_df12 = pd.concat([df1, df2])  # 默认上下（垂直）进行合并
    l_df12 = pd.concat([df1, df2], axis=1)  # 水平合并，由于index不一致，所以会错位，变成4*4的df，并产生nan
    print(l_df12)
    # 忽略行索引，重置索引
    igi_df12 = pd.concat([df1, df2], ignore_index=True)  # 行索引会在合并后从0开始重新开始排序
    # 使用多层索引keys 加一层索引
    mutii_df12 = pd.concat([df1, df2], keys=['x', 'y'])  # 给index多加一层索引，加在最外层，x给df1，y给df2

    # 1.2不匹配级联
    # 不匹配是指级联的维度的索引不一致。例如纵向级联时列索引不一致，横向级联时行索引不一致
    # 外连接
    df3 = make_df([1, 2, 3, 4], list('ABCD'))
    df4 = make_df([2, 3, 4, 5], list('BCDE'))
    df34 = pd.concat([df3, df4])  # 对应索引不匹配，会自动用nan填充，这里的就是np.nan
    # 所以这些都是外连接，会将所有的数据都进行连接
    df34_outer = pd.concat([df3, df4], join='outer')  # 默认的连接就是外连接
    print(df34_outer)
    # 内连接——只连接匹配的项
    df34_inner = pd.concat([df3, df4], join='inner')  # 只显示共同的部分，即只显示BCD
    print(df34_inner)

    # 1.3 append追加 专门用于在后面追加 通常更适用于追加单个DataFrame或Series，但灵活性不如concat；也是不匹配的话会产生nan
    result = df3._append(df4, ignore_index=True)  # 重置index

    # 1.4 pd.merge()合并
    # 类似于关系型数据库中表和表的合并，与concat的区别就在与它需要依据某一共同的行或列来进行合并
    # 使用pd.merge()合并时会自动根据两者相同column名称的那一列，作为key来合并 且每一列元素的顺序不要求一致
    # 一对一合并
    df5 = pd.DataFrame({
        'name': ['张三', '李四', '王五'],
        'id': [1, 2, 3],
        'age': [22, 33, 44]
    })
    df6 = pd.DataFrame({
        'id': [2, 3, 4],
        'sex': ['男', '女', '男'],
        'job': ['saler', 'ceo', 'coder']
    })
    df56 = pd.merge(df5, df6)  # 会根据id这一列来合并，并且只合并id为2，3的；若有多个相同列，需用on参数指名
    df56_new = df5.merge(df6)  # 两种写法是等价的
    print(df56)
    # 多对一合并
    df7 = pd.DataFrame({
        'name': ['张三', '李四', '王五'],
        'id': [1, 2, 2],
        'age': [22, 33, 44]
    })
    df8 = pd.DataFrame({
        'id': [2, 3, 4],
        'sex': ['男', '女', '男'],
        'job': ['saler', 'ceo', 'coder']
    })
    df78 = pd.merge(df7, df8)  # 只合并能匹配上的id，并且id=2会被合并两次；如果另一个df也有重复的2，则按照笛卡尔积的方式尽可能合并即可，
    print(df78)
    # 没有共同列则报错，或者使用left_on right_on分别指定2个表中的不同列作为连接的字段,例如:
    df7 = pd.DataFrame({
        'name': ['张三', '李四', '王五'],
        'id1': [1, 2, 2],
        'age': [22, 33, 44]
    })
    df8 = pd.DataFrame({
        'id2': [2, 3, 4],
        'sex': ['男', '女', '男'],
        'job': ['saler', 'ceo', 'coder']
    })
    df78 = pd.merge(df7, df8, left_on='id1', right_on='id2')
    # 也可以使用行索引作为连接的字段
    df78_hang = pd.merge(df7, df8, left_index=True, right_index=True)
    # 也可以左边用行索引，右边用某个列
    df78_hang_lie = pd.merge(df7, df8, left_index=True, right_on='id2')

    # 内合并和外合并
    df78_inner = pd.merge(df7, df8, how='inner')  # 内连接只显示匹配的
    df78_outer = pd.merge(df7, df8, how='outer')  # 外连接会显示两个表的所有数据
    # 左合并和右合并
    df78_left = pd.merge(df7, df8, how='left')  # 左合并显示左边表的所有数据和右边表的公共数据
    df78_right = pd.merge(df7, df8, how='right')  # 右合并显示右边表的所有数据和左边表的公共数据

    # 冲突解决
    df7 = pd.DataFrame({
        'name': ['张三', '李四', '王五'],
        'id': [1, 2, 2],
        'age': [22, 33, 44]
    })
    df8 = pd.DataFrame({
        'id': [2, 3, 4],
        'sex': ['男', '女', '男'],
        'name': ['saler', 'ceo', 'coder']
    })
    df78_s = pd.merge(df7, df8, on='id', right_on='id', suffixes=('_left', '_right'))  # 合并之后有名字冲突的列用suffixes参数加后缀解决
    '''
    merge合并总结：
	•	合并有三种现象：一对一、多对一、多对多。
	•	合并默认会找相同的列名进行合并，如果有多个列名相同，用on来指定。
	•	如果没有列名相同，但是数据又相同，可以通过left_on，right_on来分别指定要合并的列。
	•	如果想和index合并，使用left_index，right_index来指定。
	•	如果多个列相同，合并之后可以通过suffixes来区分。
	•	还可以通过how来控制合并的结果，默认是内合并，还有外合并outer，左合并left，右合并right。
    
    '''
