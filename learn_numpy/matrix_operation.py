import numpy as np

if __name__ == '__main__':
    # 矩阵的加减乘除
    # 矩阵和常数的加减乘除
    n1 = np.random.randint(0, 10, size=(4, 5))
    n2 = n1 + 10
    n3 = n1 - 10
    n4 = n1 * 10
    n5 = n1 / 10  # 除
    n6 = n1 // 10  # 整除
    n7 = n1 ** 2  # 平方
    n8 = n1 % 2  # 余数
    n9 = n1 + n2
    n10 = n1 * n2  # 两个矩阵的对应元素相乘
    # 线性代数中的矩阵运算
    n11 = np.dot(n1, n2)  # 乘法
    n12 = np.linalg.inv(n11)  # 矩阵求逆
    x = np.linalg.det(n12)  # 求行列式的值
    r = np.linalg.matrix_rank(n12)  #求矩阵的秩

    # 广播机制
    # 广播允许你在不同形状的数组之间进行数学运算，其背后的核心逻辑是：NumPy会尝试通过扩展数组的形状来使它们能够广播到相同的形状。
    # ndarray广播机制规则：1.为缺失的维度补维度（只能增加维度） 2.缺失元素用已有值填充
    n13 = np.ones(shape=(2, 3), dtype=np.int8)
    n14 = np.arange(3)
    n15 = n13 + n14  # 此时numpy就会为n14补充一行与第0行数值相同来完成矩阵相加
