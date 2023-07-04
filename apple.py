import yfinance as yf
import streamlit as st

st.write("""
# Приложение для отслеживания акций

Показаны данные по акциям компании Apple

""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = 'AAPL'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2000-1-1', end='2023-1-1')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
## Цена открытия
""")
st.line_chart(tickerDf.Open)

st.write("""
## Пиковая цена дня
""")
st.line_chart(tickerDf.High)

st.write("""
## Самая низкая цена дня
""")
st.line_chart(tickerDf.Low)

st.write("""
## Цена закрытия
""")
st.line_chart(tickerDf.Close)

st.write("""
## Объем
""") 
st.line_chart(tickerDf.Volume)

st.write("""
## Дивиденды
""") 
st.line_chart(tickerDf.Dividends)

st.write("""
## Дробление акций
""") 
st.line_chart(tickerDf['Stock Splits'])


