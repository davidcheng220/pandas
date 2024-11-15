import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

url = 'http://bit.ly/kaggletrain'
df = pd.read_csv(url)

# print(df.describe())
# df.describe(include=[np,number])
print(df.describe(include=[np.number]))


print("\n", "*"*20)
print(df.Age.describe())

print(df.describe(exclude=[np.number]))


print("\n", "*"*20)
print(df.Sex.describe())
# ?返回唯一值的數組（或列表），不關心其數量
print(df.Embarked.unique())
# 不重複的有幾種
print(df.Embarked.nunique())
# 計算數量
print(df.Embarked.value_counts())

plt.figure("登船港口分佈")
df.Embarked= df.Embarked.fillna('S')
plt.hist(df.Embarked)
plt.show()