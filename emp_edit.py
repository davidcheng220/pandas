import pandas as pd
import numpy as np

file = "datasets\Employees.xlsx"

df = pd.read_excel(file)

# print(df['薪水'].describe())

# df['年齡'] = df['年齡'] + 1
def add(x):
    return x + 1

df['年齡'] = df['年齡'].apply(add)
# df['薪水'] = df['薪水']*1.1
# print(df)

def addSalary(salary, bonus):
    return salary*1.1 + bonus

# df.薪水 = df.薪水.apply(addSalary, args=(1000,))
df['薪水'] = df['薪水'].apply(addSalary, args=(1000,))
print(df)

# df["獎金"] = df['薪水']*0.5 
df.insert(1, "獎金", df.薪水* 0.5)
print(df)

# comparasion
print(df[df.薪水 < 25000])

# collect mean value
print(df[['獎金', '薪水', '年齡']].apply(lambda row: np.mean(row), axis=0))