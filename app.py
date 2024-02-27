# Standard imports
#import pandas as pd

# matplotlib
#import matplotlib as mpl
#import matplotlib.pyplot as plt
#import seaborn as sns
#plotly
#import plotly.express as px
#import plotly.graph_objects as go

import streamlit as st

st.title("MPG")
st.subheader("Hello")
st.subheader("Hello")
st.subheader("Hello")
st.subheader("Hello")

# @st.cache.data
# def load_data(path):
#     df = pd.read_csv(path)
#     return df
#

# st.title("Intro")
# st.header("MPG Data Exploration")

# if st.sidebar.checkbox("Show DataFrame"):

#     st.subheader("This is my dataset")
#     st.dataframe(data=mpg.csv)

# left_column, right_column = st.columns(2)


# years = ["All"]+sorted(pd.unique(mpg_df['year']))
# year = left_column.selectbox("Choose a year:", years)

# show_means = right_column.radio(
#     label="Show class means", options=["Yes", "No"]
# )

# if year == 'All':
#     reduced_df = mpg_df
# else: 
#     reduced_df = mpg[mpg_df['year'] == year]

# means = reduced_df.groupby('class').mean(numeric_only=True)

# m_fig, ax = plt.subplots(figsize=(10,8))
# ax.scatter(mpg_df['displ'])

# if show_means == "Yes":
#     ax.scatter(means['displ'], means['hwy'], alpha=0.7
#     color='red', label = 'Nlam')

# st.pyplot(m_fig)



# url = "https"
# st.write("Data Source:", url)



