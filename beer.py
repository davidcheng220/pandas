import pandas as pd

url = 'http://bit.ly/drinksbycountry'
drinks = pd.read_csv(url)


# # print(drinks[['country', 'beer_servings', 'spirit_servings', 'wine_servings', 'total_litres_of_pure_alcohol']].describe())
# print(drinks['beer_servings'].describe())

# 分析整個國家喝酒分析
print(drinks.describe())
# 在drinks的beer servings 到wine servings的欄位取最大值
print("-"*20)

print(drinks.loc[:, 'beer_servings':'wine_servings'].apply(max, axis=0))
# 運用Loc函式取所有的資料 從country到wine serving攔
print("-"*20)
print("Serving: ")
servings = drinks.loc[:, "country":"wine_servings"]
print(servings)

# 在表格中找出哪國beer喝最多 運用sort_values
print("-"*20)
print("Beer Serving: ")
beer_s = servings.sort_values("beer_servings", ascending=False)
print(beer_s)
print(beer_s.iat[0,0])

# 烈酒
print("-"*20)
print("Spirit Serving: ")
spirit_s = servings.sort_values("spirit_servings", ascending=False)
print(spirit_s)
print(spirit_s.iat[0,0])

# 紅酒
print("-"*20)
print("Wine Serving: ")
wine_s = servings.sort_values("wine_servings", ascending=False)
print(wine_s)
print(wine_s.iat[0,0])