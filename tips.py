import pandas as pd
import numpy as  np
import streamlit as st 
import plotly.express as px


df = px.data.tips()

st.write("""
# Чаевые в ресторане
""")

st.write("""
### Задание: визуализировать данные из датасета [tips](https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv)
""")

st.write(df)

st.write("""
#### Гистограмма распределения значений общего счета 
""")
fig = px.histogram(df, x="total_bill", nbins=20)
st.plotly_chart(fig, theme=None, use_container_width=True)

st.write("""
#### Точечная диаграмма зависимости суммы чаевых от общего счета 
""")
fig = px.scatter(df, x="total_bill", y="tip", color="sex", labels={"sex": "Пол"})
st.plotly_chart(fig, theme=None, use_container_width=True)

st.write("""
#### Диаграма зависимости общего счета от дня недели
""")
fig = px.bar(df, x="day", y="total_bill")
st.plotly_chart(fig, theme=None, use_container_width=True)

st.write("""
#### Точечная диаграмма зависимости суммы чаевых от дня недели
""")
fig = px.scatter(df, x="tip", y="day", color="sex", labels={"sex": "Пол"})
st.plotly_chart(fig, theme=None, use_container_width=True)

st.write("""
#### Диаграмма размаха всех счетов в зависимости от дня недели 
""")
fig = px.box(df, x="day", y="total_bill", color='time')
st.plotly_chart(fig, theme=None, use_container_width=True)

st.write("""
#### Гистограммы распределения суммы чаевых от времени суток
""")
fig = px.histogram(df, x="tip", color="time", nbins=15, barmode='overlay')
st.plotly_chart(fig, theme=None, use_container_width=True)


st.write("""
#### Точечные диаграммы зависимости размера счета и чаевых 
""")
fig = px.scatter(df, x="total_bill", y="tip", color='smoker', facet_col= 'sex')
st.plotly_chart(fig, theme=None, use_container_width=True)