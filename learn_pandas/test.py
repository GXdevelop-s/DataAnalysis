import numpy as np
import pandas as pd

if __name__ == '__main__':
    df1 = pd.DataFrame({
        'color': ['red', 'blue', 'green', 'green', 'red', 'red', 'yellow'],
        'price': [3, 7, 1, 9, 3, 7, 8]
    })
    grouped = df1.groupby(by='color')
    for name, group in grouped:
        print(name)
        print(group)