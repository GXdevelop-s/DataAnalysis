import numpy as np
import pandas as pd

if __name__ == '__main__':
    df13 = pd.DataFrame(data=np.random.randint(0, 100, size=(5, 3)), index=list('ABCDE'), columns=['PY', 'NP', 'PD'])
    print(df13)

    def fun1(x):
        x['PY'] += 1
        x['NP'] -= 1
        x['PD'] *= 10


    df13.apply(fun1,axis=1)
    print(df13)
    print(df13.info)

