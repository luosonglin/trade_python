import pandas as pd

df = pd.read_csv("/Users/luosonglin/Downloads/2000W/all.csv")

df.query('Name==""').loc[:, 'AAA'].to_csv('/Users/luosonglin/Desktop/Downloads/2000W/xq1-200W.csv',
          columns=['time', 'price', 'pchange', 'change', 'volume', 'amount', 'type'],
          encoding='utf_8_sig', index=False)
