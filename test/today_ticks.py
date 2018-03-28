import tushare as ts
import pandas as pd

# print(ts.get_today_ticks(code='601318'))


df = ts.get_today_ticks(code='601318')
df.to_csv('/Users/luosonglin/Desktop/Trade/haha.csv', columns=['time', 'price','pchange','change','volume','amount','type'])

# reader = pd.read_csv('/Users/luosonglin/Desktop/Trade/haha.csv', header=)
