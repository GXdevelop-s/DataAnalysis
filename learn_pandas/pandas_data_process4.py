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