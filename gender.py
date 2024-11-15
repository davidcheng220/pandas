import pandas as pd

url = 'http://bit.ly/kaggletrain'
train = pd.read_csv(url)

# Map sex values to 1 for female and 0 for male
train['Sex'] = train['Sex'].map({'female': 1, 'male': 0})

# Alternatively, map sex values to '女' for female and '男' for male
# train['Sex'] = train['Sex'].map({'female': '女', 'male': '男'})

print(train)
