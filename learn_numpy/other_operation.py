import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # 1.ndarray的四个重要属性：ndim维度，shape形状（各维度的长度），size总长度，dtype元素类型
    neymar = plt.imread('neymar.jpg')
    print(neymar.shape)  # 三个维度(999, 999, 3)
    print(neymar.ndim)  # 维度3
    print(neymar.size)  # 总数据量 999*999*3
    print(neymar.dtype)  # 元素的类型 uint8，无符号整数，8位表示一个字节0000 0000 ，如果有符号是2^7，无符号所以是2^8

    # 2. ndarray的基本操作：索引和切片

    # 2.1索引一维与列表完全一致，多维时间同理；修改就是赋值，可以整行的修改n[5,3]=[1,2,3,4]
    l = [1, 2, 3, 3, 4]
    na1 = np.array(l)
    x = na1[0]
    y = na1[-1]
    # 二维
    na2 = np.random.randint(0, 10, size=(4, 5))
    last_digit1 = na2[3][4]  # 最后一个数字
    last_digit2 = na2[-1][-1]
    last_digit3 = na2[3, 4]  # 简写

    # 2.2 切片和列表完全一致，多维同理
    na3 = np.random.randint(10)
    digit2_6 = na3[2:6]
    reversed_array = na3[::-1]
    # 二维
    na4 = np.random.randint(0, 10, size=(6, 8))
    print(na4[0])  # 取一行
    print(na4[1:4])  # 取连续多行
    print(na4[[1, 2, 4]])  # 取不连续的多行再写一个中括号，这里不是切片，切片一定是连续的
    # 取列的时候要先取行
    print(na4[:, 0])  # 取一列   需要切片加索引 逗号可以区分维度，所以先取所有行再取第0列即可
    print(na4[1:4, 0])  # 先取0-3行，再取0列
    print(na4[:, 2:4])  # 取连续的多列
    # 翻转操作
    na5 = np.random.randint(0, 256, size=(100, 100, 3))  # 随意一个图片矩阵
    print(na5[::-1])  # 行翻转
    print(na5[:, ::-1])  # 列翻转
    print(na5[:, :, ::-1])  # 颜色翻转
    print(na5[::10, ::10, ::-1])  # 步长为10，模糊处理

    # 3 ndarray变形、级联、拆分
    # 3.1变形reshape函数，
    n1 = np.arange(1, 21)
    np.reshape(n1, (4, 5))  # 变成二维，用np调用函数，第一个参数为数组，第二个参数是新的形状
    n1.reshape((5, 4))  # 也可以直接用数组进行调用
    n1.reshape(5, 4)  # 这种写法也正确，但是还是尽量统一
    n1.reshape((2, -1))  # 使用-1，-1表示任意剩余维度的长度（自动计算剩下的维度），例如20个数，2为行数，那么剩下的就是10列
    n1.reshape(-1)  # -1表示自动计算该轴的长度，并且只有一个参数说明是一维数组，这是将数组变成一维的好方法
    # 3.2级联 np.concatenate()参数是列表或者元组，级联的数组维度必须相同（上下合并列一致，左右合并行一致），可通过axis参数改变级联方向
    n2 = np.random.randint(1, 100, size=(3, 4))
    n3 = np.random.randint(1, 100, size=(3, 4))
    np.concatenate((n2, n3))  # 默认上下合并
    np.concatenate((n2, n3), axis=0)  # 上下合并
    np.concatenate((n2, n3), axis=1)  # 左右合并
    # 水平级联np.hstack()和垂直级联np.vstack()
    np.hstack(n2, n3)
    np.vstack(n2, n3)
    # 3.3 切分/拆分/分割；切分，以水平切分为例，垂直切分同理
    n4 = np.random.randint(0, 100, size=(6, 4))
    n4_list1 = np.vsplit(n4, 3)  # 垂直平均拆分成三份，返回一个含有三个ndarray的列表
    n4_list2 = np.vsplit(n4, (1, 2, 4))  # 按照指定位置拆分：1指在0行和1行之间拆一刀，2指在1行和2行之间拆一刀，4指在3行和4行之间拆一刀
    n4_list3 = np.split(n4, 2, axis=0)  # 可以水平也可垂直，默认水平,拆分成两份

    # 4 ndarray 副本、复制、拷贝
    # 在python中               赋值：用的是同一个内存，所以说改一个其他的也就都改了
    # 不想要两个都变的情况下会用到 拷贝：copy()
    n5 = np.random.randint(0, 100, size=(6, 4))
    n5_copy = n5.copy()

    # 5.聚合操作
    # 5.1 求和 np.sum()
    n6 = np.arange(10)
    total1 = np.sum(n6)
    # 二维求和
    n7 = np.random.randint(0, 100, size=(6, 4))
    total2 = np.sum(n7)  # 所有数字的和
    total3 = np.sum(n7, axis=0)  # 表示每一列的多行求和
    # 最大、小、平均、中位、百分位、标准差、方差
    max_num = np.max(n7)
    min_num = np.min(n7)
    mean_num = np.mean(n7)  # 两种一模一样
    row_mean_num = np.mean(n7, axis=1)  # 求每一行的平均值，也就是对列数不同的值求平均
    average_num = np.average(n7)
    median_num = np.median(n7)  # 中位数
    percentile_num = np.percentile(n7, q=50)  # 百分位数，q=50时是中位数
    power_num = np.power(n7, 3)  # 三次方 或者 n**3效果一样
    std_num = np.std(n7)  # 标准差
    var_num = np.var(n7)  # 方差
    # 求下标
    np.argmax(n7)  # 第一个最大值的下标
    np.argmin(n7)  # 第一个最小值的下标
    np.argwhere(n7 == np.max(n7))  # 找出所有最大值的下标
    # np.sum()和np.nansum() nan:数值类型，不是一个正常数值，表示空。np.nan:float类型
    np.sum(n7)  # 若有空值，无法求和
    np.sumnan(n7)  # 排除掉nan之后，剩下的数的和

    # 其它数学操作
    np.abs(n7)  # 绝对值
    np.sqrt(n7)  # 平方根
    np.square(n7)  # 平方
    np.exp(n7)  # 指数运算
    np.log(n7)  # 以e为底对数
    np.sin(n7)
    np.cos(n7)
    np.tan(n7)
    np.round(n7, 2)  # 四舍五入，默认整数，第二个参数是小数点后几位
    np.ceil(n7)  # 向上取整
    np.floor(n7)  # 向下取整
    np.cumsum(n7)  # 累加，按照斐波那契数列方式对原数组累加形成新数组

    # ndarray排序
    # np.sort():接受一个数组作为参数，并返回一个新的已排序的数组，而不会修改原始数组  内部是混合排序
    # ndarray.sort(): 这是一个数组对象的方法，它对原始数组进行排序，并不返回一个新的数组。它会直接修改原始数组的顺序，并返回None;原地排序不占用内存空间，内部是快速排序
    n8 = np.random.randint(0, 10, size=6)
    sorted_n8 = np.sort(n8)
    n9 = np.random.randint(0, 10, size=6)
    n9.sort()

    # ndarray文件操作
    # save:保存ndarray到一个npy文件当中
    # savez:保存多个array保存到一个npz文件中，以字典的方式存，返回值也是字典
    # 保存ndy
    arr = np.array([1, 2, 3, 4, 5])
    np.save('my_array.npy', arr)
    loaded_arr = np.load('my_array.npy')
    print(loaded_arr)
    # 保存ndz
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    np.savez('my_arrays.npz', array1=arr1, array2=arr2)
    loaded_data = np.load('my_arrays.npz')
    arr1 = loaded_data['array1']
    arr2 = loaded_data['array2']
    print(arr1)
    print(arr2)

    # csv、txt文件的读写操作
    n = np.arange(19)
    np.savetxt('arr.csv', n, delimiter=',')
    np.loadtxt('arr.csv', delimiter=',', dtype=np.int16)

    # 归一化/正则化
    n9 = np.random.randint(0, 100, size=(5, 5))
    min1 = np.min(n9)
    max1 = np.max(n9)
    new_n9 = (n9 - min1) / (max1 - min1)
