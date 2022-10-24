import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn')

st.title('World Cities')
df = pd.read_csv('worldcities.csv')

# 创建一个从0-40的滑块用于筛选人口数据
population_filter = st.sidebar.slider('Minimal Population (Millions):', 0.0, 40.0, 3.6) 
# title, min, max, default

# 创建多选框
capital_filter = st.sidebar.multiselect(
     'Capital Selector',
     df.capital.unique(),  # options
     df.capital.unique())  # defaults

# 创建输入框
# .sidebar:将部件放在侧边栏
# .form(xxx):根据xxx来分组
form = st.sidebar.form("country_form")
country_filter = form.text_input('Country Name (enter ALL to reset)', 'ALL')
# form.text_input(输入框标题，默认值)
form.form_submit_button("Apply")


# filter by population
df = df[df.population >= population_filter]

# filter by country
df = df[df.capital.isin(capital_filter)]

if country_filter!='ALL':
    df = df[df.country == country_filter]

# show on map
st.map(df)

# show dataframe
st.subheader('City Details:')
st.write(df[['city', 'country', 'population']])

# show the plot
st.subheader('Total Population By Country')
fig, ax = plt.subplots(figsize=(20, 5))
pop_sum = df.groupby('country')['population'].sum()
pop_sum.plot.bar(ax=ax)
st.pyplot(fig)

# cd my-streamlit
# streamlit run app-cities.py