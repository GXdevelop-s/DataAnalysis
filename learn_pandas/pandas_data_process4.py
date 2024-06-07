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

    # 2 pandas缺失值处理
    '''
    缺失值：None和np.nan
    None是Python内置的常量，用于表示“无值”或“空值”。它的类型是NoneType是空对象。  np.nan是NumPy库中的一个常量，用于表示“不是一个数字”（Not a Number）。它的类型是浮点数（float）。
    None通常用于函数没有返回值、变量未赋值或明确表示“空”的场景，例如：if x is None 。 np.nan通常用于处理数值数据中的缺失值或无效值，特别是在数组和数据分析中。
    None与任何其他对象的比较通常是False（除了与自己比较）。可以使用is关键字来检查一个变量是否是None。np.nan与任何数值的比较总是False，包括与自己比较也是False（np.nan == np.nan是False）。可以使用np.isnan()函数来检查一个值是否是np.nan。
    None不能参与任何数学运算，如果尝试对None进行数学运算会抛出TypeError。  np.nan可以参与数学运算，但结果通常也是np.nan，例如：np.nan + 1仍然是np.nan。
    object的运算效率要比float要慢很多
    '''
    '''
    isnull()
    notnull()
    all()和any()
    dropna()
    fillna()
    '''
    # 2.1np.nan运算————可以用np.nan*()来计算，此时会过滤掉nan
    array1 = np.array([1, 2, 3, 4, np.nan, 5])
    s = np.sum(array1)  # 结果仍然是np.nan，其他直接对np.nan的数学运算也是不可以的
    s2 = np.nansum(array1)  # 结果是15.0

    # 2.2 pandas中的None和np.nan
    data = np.random.randint(0, 100, size=(5, 5))
    df9 = pd.DataFrame(data=data, columns=list('ABCDE'))
    df9.loc[1, 'C'] = np.nan
    df9.loc[4, 'E'] = None
    print(df9)  # 在pandas中无论写None还是np.nan都会被一律识别为np.nan

    # 2.3 缺失值检测
    # df.isnull
    bool_df9 = df9.isnull()  # 会返回一个同样结构的df，如果是空值就会是True，如果有值就会是False
    print(bool_df9)
    bool2_df9 = df9.notnull()  # 会返回一个同样结构的df，和isnull()相反，如果是空值就会是False，如果有值就会是 True ,
    # all():必须全部为True才是True，any()只要有一个为True就为True
    boll_result = df9.isnull().any()  # 返回值是一个Series，其索引是df的列，尽可能找到有空值的列
    boll_result2 = df9.isnull().all()  # 返回值是一个Series，必须全部为空的行或列才会是True
    boll_result3 = df9.notnull().all()  # 返回值是一个Series，找不为空的，即找所有都没有空值的列
    boll_result4 = df9.notnull().any()  # 只要有一个不为空就可以
    # 改成找行的只需要给all()和any()换个维度就可以
    boll_result5 = df9.notnull().all(axis=1)

    # 2.4 过滤数据
    # 使用bool值进行过滤
    # 行过滤
    cond = df9.isnull().any(axis=1)  # 现在是有空的行就会是true,作为条件来使用
    print(df9[cond])  # 是true的行才会被保留，也就是有空值才会被保留  ps：当你向数据框 df9 提供一个布尔序列或布尔数组（列表或Numpy数组）时，Pandas 默认这些布尔值是用来索引行的！！！
    print(df9[~cond])  # ～取反，和上面相反
    # 列过滤
    print(df9.loc[:, cond])  # 行不做处理，对列加条件
    print(df9.loc[:, ~cond])  # 列过滤取反
    # 过滤场景举例：假设现在需要选择出所有 age这一列大于10的人员名单，怎么pandas实现
    cond2 = df9['age'] > 10  # 这部分是一个逐元素比较是否大于10的操作，结果是一个布尔序列
    order10_df = df9[cond2]

    # 使用过滤函数dropna()进行过滤
    new_df9 = df9.dropna(axis=1)  # 删除有空的列，默认删除有空的行
    # 必须所有数据都为nan才会删除
    print(df9.dropna(how='all'))  # 行中所有值都是空的才会删除
    print(df9.dropna(how='any', axis=1))  # 列中有空值就会删除
    # 修改原数据
    df9.dropna(inplace=True)
    # inplace=True 参数会直接修改原始的 DataFrame (df9)，并返回 None，所以保险的做法是先搞一个副本
    df9_copy = df9.copy()
    print(df9_copy.dropna(inplace=True))

    # 使用函数fillna()进行空值的填充
    df10 = df9.copy()
    df10.fillna(value=10, inplace=False, limit=100)  # limit是限制填充的次数且 inplace参数决定了函数是否有返回值
    foredf10 = df10.fillna(method='ffill', inplace=False, limit=100)  # 向前填充 forefill 配合axis=1 则是向左填充
    backdf10 = df10.fillna(method='bfill', inplace=False, limit=100)  # 向后填充 backfill  配合axis=0 则是向右填充

    # 3. pandas 重复值处理
    # duplicated（）   ————检测是否有重复的行
    # drop_duplicated（） ——————删除重复的行
    # 一般来说重复值只考虑行，因为无论是excel还是结构型数据库都是行才有意义
    df11 = make_df([1, 2, 3, 4], list('ABCD'))
    # 让前两行的数据重复
    df11.loc[1] = df11.loc[2]

    # 识别重复数据
    # 是否出现和前面的行重复了
    dup_series = df11.duplicated()  # 返回值是一个series，其索引是原df的行索引
    # 标记方式选择
    df11.duplicated(keep='first')  # 默认选项 标记除了第一次出现之外的所有重复行为 True。第一次出现的行被视为唯一行，不会被标记为重复
    df11.duplicated(keep='last')  # 标记除了最后一次出现之外的所有重复行为 True。最后一次出现的行被视为唯一行，不会被标记为重复
    df11.duplicated(keep=False)  # 所有重复的行都标记为 True，即使是第一次或最后一次出现的行也不例外。
    # 判断某几列组合的重复数据
    df11.duplicated(subset=['B', 'D'])  # 在这个例子中，只有在列 'B' 和列 'D' 的组合值相同时，行才被认为是重复的。

    # 删除重复值
    df11_copy = df11.copy()
    df11_copy.drop_duplicates()
    # 某几列组合重复删除
    df11_copy.drop_duplicates(subset=['B', 'D'])
    df11_copy.drop_duplicates(subset=['B', 'D'], keep='last')  # 表示保留最后出现的一行，前面重复的删除掉

    # 4.pandas 数据映射
    '''
    replace()函数：替换元素
    map()函数：处理某一单独的列
    rename()函数：替换索引
    '''
    # 4.1replace()函数：替换元素
    index = ['张三', '李四', '王五', '赵高']
    columns = ['js', 'py', 'c#', 'php']
    data2 = np.random.randint(0, 100, size=(4, 4))
    df12 = pd.DataFrame(data=data2, index=index, columns=columns)
    df12.replace({5: 50, 1: 100}, inplace=True)  # 将所有5变成50，1变成100
    # 4.2 map()函数：处理单独列（批量处理列中元素）,是series的方法，不是dataframe的方法 且map中可以使用lambda函数
    df12_copy = df12.copy()
    # 结合匿名函数lambda使用
    df12_copy['py'].map(lambda x: x * 10)  # 虽然df12_copy['py']*10也可以完成，但是复杂一些用map更好
    df12_copy['python'] = df12_copy['py'].map(lambda x: x * 10)  # 在最后新增一列
    df12_copy['python是否及格'] = df12_copy['py'].map(lambda x: '及格' if x > 60 else '不及格')  # 新增一列判断某列是否满足某个条件


    # 结合普通函数使用——判断js成绩 不及格 及格 优秀
    def band(n):
        if n < 60:
            return 'fail'
        elif 60 <= n < 80:
            return 'pass'
        else:
            return 'great'


    df12_copy['js等级'] = df12_copy['js'].map(band)
    # 4.3rename()函数：替换索引
    df12_copy.rename(index={'赵高': 'sb'})  # 默认替换行索引
    df12_copy.rename(columns={'js': 'javascript'}, inplace=True)    # 替换列索引
    # 重置索引
    df12_copy.reset_index(inplace=True) # 将行索引变成新的数字索引，原来的行索引变成一列数据
    # 设置索引
    df12_copy.set_index(keys=['php'])   # 这会将php这一列的数据作为行索引
