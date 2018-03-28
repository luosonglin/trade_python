import tushare as ts

print(ts.get_k_data(code='601318', start='2018-01-01', end='2018-03-28', ktype='D', autype='None', retry_count=3,
                    pause=0.001))
