from os import sep
import pandas as pd


src_df = pd.read_csv('product_cameras.csv', encoding='latin1')
src_to_excel = src_df.to_excel('product_cameras.xlsx')


df = pd.read_excel('product_cameras.xlsx')



brand_df = df.sort_values('Brand', ascending=True)
top_df = df.sort_values('Top-Price', ascending=True)
sale_df = df.sort_values('Sale-Price', ascending=True)
id_df = df.sort_values('id', ascending=True)









writer = pd.ExcelWriter("test_file.xlsx", engine = 'xlsxwriter')
df.to_excel(writer, sheet_name = 'All')
brand_df.to_excel(writer, sheet_name = 'Brand')
top_df.to_excel(writer, sheet_name = 'Top-Price')
sale_df.to_excel(writer, sheet_name = 'Sale-Price')
id_df.to_excel(writer, sheet_name = 'id')
writer.save()