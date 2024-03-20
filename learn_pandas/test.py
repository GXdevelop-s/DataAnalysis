import numpy as np
import pandas as pd

if __name__ == '__main__':
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
print(df4)