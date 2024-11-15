import pandas as pd
import numpy as np

url = 'http://bit.ly/kaggletrain'
df = pd.read_csv(url)

# print(df.describe())
# df.describe(include=[np,number])
print(df.describe(include=[np.number]))


print("\n", "*"*20)
print(df.Age.describe())