import pandas as pd
data = pd.read_csv("./test-task_dataset_summer_products.csv")
df = pd.DataFrame(data, columns = ['origin_country', 'price', 'rating_count', 'rating_five_count', 'product_id'])
dfProducts = pd.DataFrame(df.groupby('origin_country', dropna=False).mean()[['price']]);
five_percentage = (df.groupby('origin_country', dropna=False)["rating_five_count"].sum() / df.groupby('origin_country', dropna=False)["rating_count"].sum()) * 100
dfProducts['five_percentage'] = five_percentage
print(dfProducts)
