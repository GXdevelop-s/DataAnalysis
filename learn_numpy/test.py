import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

if __name__ == '__main__':
    s8 = pd.Series(['ZHANGSAN', 'LISI', 'WANGWU', np.nan])
    s=s8.isnull()  # 判断是否为空
    print(s)