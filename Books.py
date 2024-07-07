import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
df_reviews = pd.read_csv("customer reviews.csv")
df_top100 = pd.read_csv("Top-100 Trending Books.csv")

price_max = df_top100["book price"].max()
price_min = df_top100["book price"].min()

max_price = st.sidebar.slider("Price Range", price_min, price_max, price_max)
df_book = df_top100[df_top100["book price"] <= max_price]
graf = px.bar(df_book["year of publication"].value_counts())
histogram = px.histogram(df_top100["book price"])

st.title("Top 100 Best selling Books of Amazon")
df_book
col1, col2 = st.columns(2)
col1.plotly_chart(graf)
col2.plotly_chart(histogram)