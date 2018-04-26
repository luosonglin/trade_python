import tushare as ts
import pandas as pd
import datetime as dt

# print(ts.get_today_ticks(code='601318'))


date = dt.date.today()


# df = ts.get_today_ticks(code='601318', date='2018-03-27')
# df.to_csv('/Users/luosonglin/Desktop/Trade/601318-' + date.strftime('%Y-%m-%d') + '.csv',
#           columns=['time', 'price', 'pchange', 'change', 'volume', 'amount', 'type'],
#           encoding='utf_8_sig')


# reader = pd.read_csv('/Users/luosonglin/Desktop/Trade/601318-' + date.strftime('%Y-%m-%d') + '.csv', index_col=[0,2])
# print(reader)



# print(date)
# print(date.strftime('%Y-%m-%d'))
# print('/Users/luosonglin/Desktop/Trade/601318/' + date.strftime('%Y-%m-%d') + '.csv')


# print(reader.to_json())

# df2 = ts.get_latest_news()
# print(df2)


def read():
    return pd.read_csv('/Users/luosonglin/Desktop/Trade/601318-' + date.strftime('%Y-%m-%d') + '.csv', index_col=[0, 2])


# df = ts.get_day_all()
# df.to_csv('/Users/luosonglin/Desktop/Trade/day_all_' + date.strftime('%Y-%m-%d') + '.csv',
#           # columns=['time', 'price', 'pchange', 'change', 'volume', 'amount', 'type'],
#           encoding='utf_8_sig')


# df = ts.get_sina_dd('601318', date='2018-03-29', vol=1000)
# df.to_csv('/Users/luosonglin/Desktop/Trade/601318-dd1000-2018-03-29.csv',
#           encoding='utf_8_sig')

# print(ts.get_ppi())

print(ts.get_realtime_quotes("601318"))
# print(ts.get_realtime_quotes("000651"))
# print(ts.get_realtime_quotes("002049"))

# df = ts.get_realtime_quotes("601318")
# print(df.to_json())

# dadan
df = ts.get_sina_dd('000651', date='2018-04-26', vol=100)
df.to_csv('/Users/luosonglin/Desktop/Trade/000651-dd-' + date.strftime('%Y-%m-%d') + 'AM.csv',
          columns=['code', 'name', 'time', 'price', 'volume', 'preprice', 'type'],
          encoding='utf_8_sig')