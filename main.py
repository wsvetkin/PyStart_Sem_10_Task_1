import pandas as pd
import random

from pandas.core.interchange import dataframe

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
data.head()
print(data)


def one_hot_lst(data_list: list) -> dataframe:
    rob_lst = []
    hum_lst = []

    for i in lst:
        if i == 'robot':
            rob_lst.append('1')
            hum_lst.append('0')
        else:
            hum_lst.append('1')
            rob_lst.append('0')

    new_data = pd.DataFrame({'robot': rob_lst, 'human': hum_lst})
    return new_data


print(one_hot_lst(lst))
