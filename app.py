import yfinance as yf
import streamlit as st

st.write("""
# Тестирование возможностей Streamlit на примере компании Apple 

#### Графики цен закрытия акций, объемов продаж и распределения дивидентов компании Apple

""")


tickerData = yf.Ticker('AAPL')

tickerDf = tickerData.history(interval = '1d', start='2013-1-1', end='2023-1-1')

st.write("""
## Цена закрытия

""")
st.line_chart(tickerDf.Close)

st.write("""
## Объемы продаж


""")
st.line_chart(tickerDf.Volume)

st.write("""
## Распределение дивидентов

""")
st.line_chart(tickerDf.Dividends)
