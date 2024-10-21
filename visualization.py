import streamlit as st
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
import plotly.express as px


def load_data():
    df = pd.read_csv(r"/Users/ayagad/Hotel_canceling/Hotel_Booking_canceling_final.csv")
    return df
df = load_data()
n_rows=st.slider('Choose number of rows to display',min_value=5,max_value=len(df),step=1)
columns_show=st.multiselect('Select Columns to show',df.columns.to_list(),default=df.columns.to_list())
st.write(df[:n_rows][columns_show])
book_cancelled = df['booking status'].value_counts()
labels = book_cancelled.index
values = book_cancelled.values

    # Select top 5 slices
top_5_labels = labels[:5]
top_5_values = values[:5]
fig = px.pie(names=top_5_labels,
                    values=top_5_values,
                    hole=0.3,  # To create a doughnut-style pie chart
                    title="bool Cancelled or not",
                    labels={'label': 'hotel_book', 'value': 'Count'},
                    color_discrete_sequence=px.colors.qualitative.Set3)
st.plotly_chart(fig)
room_type = df['room type'].value_counts()
labels = room_type.index
values = room_type.values

    # Select top 5 slices
top_5_labels = labels[:5]
top_5_values = values[:5]
fig = px.pie(names=top_5_labels,
                    values=top_5_values,
                    hole=0.3,  # To create a doughnut-style pie chart
                    title="Room Type",
                    labels={'label': 'Type', 'value': 'Count'},
                    color_discrete_sequence=px.colors.qualitative.Set2)
st.plotly_chart(fig)
Market_segment = df['market segment type'].value_counts()
labels = Market_segment.index
values = Market_segment.values

    # Select top 5 slices
top_5_labels = labels[:5]
top_5_values = values[:5]
fig = px.pie(names=top_5_labels,
                    values=top_5_values,
                    hole=0.3,  # To create a doughnut-style pie chart
                    title="Market Segment Type",
                    labels={'label': 'Type', 'value': 'Count'},
                    color_discrete_sequence=px.colors.qualitative.Set2)
st.plotly_chart(fig)
meal_type = df['type of meal'].value_counts()
labels = meal_type.index
values = meal_type.values

    # Select top 5 slices
top_5_labels = labels[:5]
top_5_values = values[:5]
fig = px.pie(names=top_5_labels,
                    values=top_5_values,
                    hole=0.3,  # To create a doughnut-style pie chart
                    title="Meal Type",
                    labels={'label': 'Type', 'value': 'Count'},
                    color_discrete_sequence=px.colors.qualitative.Set1)
st.plotly_chart(fig)
numerical_columns=df.select_dtypes(include=np.number).columns.to_list()
histogram_feature=st.selectbox('Select feature to Histogram',numerical_columns)
fig_hist= px.histogram(df,x=histogram_feature)
st.plotly_chart(fig_hist)

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=df,x="booking status",y="P-C",ax=ax)
plt.ylabel("Previously cancelled")
st.pyplot(fig)
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=df,x="booking status",y="P-not-C",ax=ax)
plt.ylabel("Previously cancelled")
st.pyplot(fig)
fig, ax = plt.subplots(figsize=(10, 6))
sns.countplot(data=df,x='market segment type',hue='booking status',ax=ax)
plt.ylabel("Previously cancelled")
st.pyplot(fig)
fig, ax = plt.subplots(figsize=(10, 6))
sns.countplot(data=df,x='repeated',hue='booking status',ax=ax)
plt.ylabel("Previously cancelled")
st.pyplot(fig)
fig, ax = plt.subplots(figsize=(10, 6))
sns.countplot(data=df,x='special requests',hue='booking status',ax=ax)
plt.ylabel("Previously cancelled")
st.pyplot(fig)
