import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    neymar = plt.imread('neymar.jpg')  # 读取图片数据
    print(neymar)  # 彩色图片在本质上是一个三维数组，第一个维度高度，第二个宽度，第三个是RGB范围在0-255，可知黑白图片是二维数组，视频是四维
    print(neymar.shape)  # 返回一个三元组,（高度的行数，宽度的行数，3表示三个RGB颜色），
    print(type(neymar))  # 数据类型为ndarray，指多维数组，nd指的是n dimension
    plt.imshow(neymar)
    plt.show()  # pycharm中需要手动调用来触发图像显示

    # ndarray
    # 1.创建
    # 1.1 用列表创建 几维的列表就创建几维的数组
    list1 = [1, 12, 23, 3]
    n1 = np.array(list1)
    print(n1.shape)  # 有几个元素就是几维，元素大小表示每一维中的数量；列表则没有这个属性，且要求ndarray中的所有元素数据类型相同
    # 如果传进来的列表中有不同的类型，则强制统一为同一类型 ，优先级str>float>int

    # 1.2用np.ones(shape,dtype=None,order='C')创建一个所有元素都为1的多维数组
    # shape为形状，dtype为元素类型，order为C是行为主,F是以列为主
    n2 = np.ones(shape=(3, 4), dtype=np.int16)  # 3行4列的2^16次方整形的数组
    # 1.3 用np.zeros(shape,dtype=None,order='C')创建一个所有元素都为0的多维数组
    n3 = np.zeros(shape=(3, 4), dtype=np.int16)
    # 1.4 用np.full(shape,fill_value,dtype=None,order='C')创建一个所有元素都为指定元素的多维数组
    n4 = np.full(shape=(3, 4), fill_value=8, dtype=np.int16)  # fill_value为指定的元素
    # 1.5 用np.eye(N,M=None,k=0,dtype=float)创建一个对角线为1 其它位置为0的单位矩阵，N为行，M为列（默认方阵），（-）k值为向（左）右偏移几个位置，即左边多两个0列
    n5 = np.eye(6, 6, k=-2, dtype=np.int16)
    # 1.6 用np.linspace(start,stop,num=50,endpoint=True,retstep=False,dtype=None)创建一个等差数列,num数列中的个数,endpoint是否包含结束值，retstep是否返回等差值
    n6 = np.linspace(0, 100, num=51)
    # 1.7 用np.arange(start,stop,step，dtype=None)创建一个数值范围的数组，和python中range功能类似
    n7 = np.arange(0, 10, 2)
    # 1.8 用np.random.randint(low,high，size=None，dtype=None)产生随机整数 size为数组形状
    n8 = np.random.randint(0, 256, size=(30, 40, 50))
    plt.imshow(n8)  # 这样可随机出彩色图片
    plt.show()
    n8_1 = np.random.randint(0, 5, size=6)  # 含有六个随机数的一维数组
    # 1.9 np.random.randn(d0,d1,d2,....,dn)创建一个服从标准正太分布的多维数组,dn是第n个维度的数值个数
    n9 = np.random.randn(3, 4)
    # 1.10 用np.random.normal(loc=0.0,scale=1.0，size=None)创建一个服从正太分布的多维数组
    n10 = np.random.normal(loc=100, scale=10, size=(3, 4))
    # 1.11 用np.random.random(size=None)创建一个元素为0-1（左闭右开）的随机数的多维数组
    n11 = np.random.random()
    n11_1 = np.random.random(size=(3, 4))
    # 1.12 用np.random.rand(d0,d1,d2,..,dn)创建一个元素为0-1（左闭右开）的随机数的多维数组，和上面类似
    n12 = np.random.rand(1, 3, 4)  # 三个维度
