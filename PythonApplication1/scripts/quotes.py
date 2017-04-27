# Filename: quotes.py 
from matplotlib.finance import quotes_historical_yahoo_ochl 
from datetime import date 
import pandas as pd 
today = date.today() 
start = (today.year-1, today.month, today.day) 
quotes = quotes_historical_yahoo_ochl('AXP', start, today) 
df = pd.DataFrame(quotes) 
print df