import tushare as ts
import datetime


print(ts.get_today_ticks(code='601318'))

# today = datetime.date.today()
# df = ts.get_today_ticks(code='601318')
# df.to_csv('/Users/luosonglin/Desktop/Trade/'+today+".csv", columns=['time','price','pchange','change','volume','amount','type'])