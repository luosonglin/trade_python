import tushare as ts
import datetime as dt

# print(ts.get_k_data(code='601318', start='2018-01-01', end='2018-12-31', ktype='D', autype='None', retry_count=3,
#                     pause=0.001))

date = dt.date.today()


df1 = ts.get_stock_basics()
print(df1.head(7))
df1.to_csv('/Users/luosonglin/Desktop/Trade/stock_basics_' + date.strftime('%Y-%m-%d') + '.csv',
          # columns=['time', 'price', 'pchange', 'change', 'volume', 'amount', 'type'],
          encoding='utf_8_sig')

