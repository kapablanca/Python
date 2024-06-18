import numpy as np
import pandas as pd


df = pd.read_csv('liquor_sales_2016_2019.csv')

ag = df.groupby(['zip_code','item_description']).agg({'bottles_sold':sum})

print(ag)
