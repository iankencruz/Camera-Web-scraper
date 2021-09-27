import pandas as pd


df = pd.read_csv('product_cameras.csv', encoding='latin1', index_col='Brand')

df.style.set_properties(**{'text-align': 'left'})

df['Top-Price'] = df['Top-Price'].str.replace('$', '', regex=True)
df['Top-Price'] = df['Top-Price'].astype(float, errors='ignore')

# if '$' in df["Sale-Price"]:
#     df['Sale-Price'] = df['Sale-Price'].str.replace('$', '')
#     df['Sale-Price'] = df['Sale-Price'].astype(float, errors='ignore')
# else:
#     print('Error: Sale-Price NaN Object Found')



brand_df = df.sort_values('Brand', ascending=True)
top_df = df.sort_values('Top-Price', ascending=True)
sale_df = df.sort_values('Sale-Price', ascending=True)
id_df = df.sort_values('id', ascending=True)



top_df['Top-Price'] = '$' + top_df['Top-Price'].astype(str) 
# sale_df['Sale-Price'] = '$' + sale_df['Sale-Price'].astype(str)

brand_name = df['Top-Price']
sale_name = df['Sale-Price']

new_df = pd.DataFrame(brand_name)
new_df['Sale-Price'] = top_df
print(new_df)
# writer = pd.ExcelWriter("product_cameras.xlsx", engine = 'xlsxwriter')
# df.to_excel(writer, sheet_name = 'All')
# brand_df.to_excel(writer, sheet_name = 'Brand')
# top_df.to_excel(writer, sheet_name = 'Top-Price')
# sale_df.to_excel(writer, sheet_name = 'Sale-Price')
# id_df.to_excel(writer, sheet_name = 'id')
# writer.save()