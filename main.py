import yfinance as yf
import csv

ticker = yf.Ticker('AAPL')
data = ticker.history(start='2011-08-24', end='2026-04-20')

with open('values.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['date', 'high'])
    for dt, row in data.iterrows():
        writer.writerow([dt.strftime('%Y-%m-%d'), row['High']])

