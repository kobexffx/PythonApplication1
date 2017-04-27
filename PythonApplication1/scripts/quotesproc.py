from matplotlib.finance import quotes_historical_yahoo_ochl
from datetime import date
from datetime import datetime
import pandas as pd
today = date.today()
start = (today.year-1, today.month, today.day)
quotes = quotes_historical_yahoo_ochl('AXP', start, today)
fields = ['date','open','close','high','low','volume']
list1 = []
for i in range(0,len(quotes)):
    x = date.fromordinal(int(quotes[i][0]))
    y = datetime.strftime(x,'%Y-%m-%d')
    list1.append(y)
quotesdf = pd.DataFrame(quotes, index = list1, columns = fields)
quotesdf = quotesdf.drop(['date'], axis = 1)
print quotesdf
