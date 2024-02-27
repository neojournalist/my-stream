# Standard imports
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#plotly
import plotly.express as px
import plotly.graph_objects as go
from urllib.request import urlopen
import json
from copy import deepcopy


# First some MPG Data Exploration
@st.cache_data
def load_data(path):
    int_df = pd.read_csv(path)
    return int_df


int_df_raw = load_data(path="./data/internet_1990_2021.csv")
df = deepcopy(int_df_raw)

# Add title and header
st.title("Which country achieved the most progress with internet penetration?")
st.header("Explore the data and find your answers in this interactive dashboard!")

# Widgets: checkbox (you can replace st.xx with st.sidebar.xx)
if st.checkbox("Show Dataframe"):
    st.subheader("This is my dataset:")
    st.dataframe(data=df)
    # st.table(data=mpg_df)

st.subheader("Internet users' map in 2020")

# # Widgets: selectbox
# years = [1990, 2020]
# year = st.selectbox("Choose a Year", years)

# # # Flow control and plotting
# if year == 1990:
#     year == df[df["Year"] == 1990]
# else:
#     reduced_df = df[df['Year'] == 2020]

with open('./data/countries.geojson', 'r') as f:
    countries = json.load(f)

fig = px.choropleth_mapbox(
    data_frame = df[df['Year']==2020],
    geojson = countries,
    featureidkey = 'properties.ISO_A3',
    locations = 'Code',
    color = 'Individuals using the Internet (% of population)',
    color_continuous_scale = 'viridis',
    opacity = 0.7)

fig.update_layout(mapbox_style="carto-positron",
                  mapbox_zoom=2, mapbox_center = {"lat": 37.0902, "lon": -95.7129})

fig.update_layout(
    width=900,  
    height=400,  
    margin=dict(l=10, r=10, t=10, b=10)  
)


fig.update_geos(
    showframe=False, 
    projection_type="baker"  
)

fig.update_geos(
    projection_scale=1 
)

st.plotly_chart(fig)


# Setting up columns
right_column = st.columns(1)



# # Widgets: radio buttons
show_tops = st.radio(
    label=' Share of internet users', options=['TOP 10 with the highest share', 'BOTTOM 10 with the lowest share'])


# Top 10
top_20 = pd.read_csv('./data/top2020.csv')
bottom_20 = pd.read_csv('./data/bottom_2020.csv')
p_fig = px.bar(top_20, x='Entity', y='internet_2020',
                hover_data=['Entity'],
                labels={'Entity':'Country',
                        'internet_2020': 'share of individuals using internet'}, 
                title = "TOP 10 countries with the most internet users, 2020",
                height=500, width=700)
p_fig.update_layout(
        plot_bgcolor="white"
    )

p2_fig = px.bar(bottom_20, x='Entity', y='internet_2020',
             hover_data=['Entity'],
             labels={'Entity':'Country',
                    'internet_2020': 'share of individuals using internet'}, 
             title = "Bottom 10 countries with the least internet users, 2020",
             height=500, width=700)
p2_fig.update_layout(
    plot_bgcolor="white")

if show_tops == 'TOP 10 with the highest share':
    st.plotly_chart(p_fig)
else:
    st.plotly_chart(p2_fig)

st.subheader("Countries which made the biggest jump in 5 yers")

top_progress = pd.read_csv('./data/top10_progress.csv')
fig2 = px.bar(top_progress, x='Entity', y='per_points',
             hover_data=['Entity'],
             labels={'Entity':'Country',
                    'per_points': '% points'}, 
             title = "TOP 10 countries, from 2015 to 2020",
             height=500, width=700)
fig2.update_layout(
    plot_bgcolor="white"
)
st.plotly_chart(fig2)   

# means = reduced_df.groupby('class').mean(numeric_only=True)

# # In Matplotlib
# m_fig, ax = plt.subplots(figsize=(10, 8))
# ax.scatter(reduced_df['displ'], reduced_df['hwy'], alpha=0.7)

# if show_means == "Yes":
#     ax.scatter(means['displ'], means['hwy'], alpha=0.7, color="red")

# ax.set_title("Engine Size vs. Highway Fuel Mileage")
# ax.set_xlabel('Displacement (Liters)')
# ax.set_ylabel('MPG')

# # In Plotly
# p_fig = px.scatter(reduced_df, x='displ', y='hwy', opacity=0.5,
#                    range_x=[1, 8], range_y=[10, 50],
#                    width=750, height=600,
#                    labels={"displ": "Displacement (Liters)",
#                            "hwy": "MPG"},
#                    title="Engine Size vs. Highway Fuel Mileage")
# p_fig.update_layout(title_font_size=22)

# if show_means == "Yes":
#     p_fig.add_trace(go.Scatter(x=means['displ'], y=means['hwy'],
#                                mode="markers"))
#     p_fig.update_layout(showlegend=False)

# # Select which plot to show


# We can write stuff
url = "https://ourworldindata.org/grapher/share-of-individuals-using-the-internet"
st.write("Data Source:", url)
# "This works too:", url

# Another header
