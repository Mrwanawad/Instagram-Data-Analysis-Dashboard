import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
from utils import human_readable, instagram_palette
import os
# streamlit run app/app.py


df = pd.read_csv( 'Data/Feature Engineered Data/Feature Engineered Data.csv' )

KPIs_dict = {
    'Total Followers' : human_readable( int( df['followers_gained'].sum(  ) ) ),
    'Total Posts' : human_readable( len( df ) ),
    'Total Likes' : human_readable( int( df['likes'].sum() ) ),
    'Total Impressions' : human_readable( int( df['impressions'].sum() ) ),
    'Average of engagement rate' : human_readable( int( df['engagement_rate'].mean() ) ),
    'Total Reach' : human_readable( int( df['reach'].sum() ) ),
    
}

# streamlit run app/app.py

st.set_page_config( 'Instagram Dashboard', ':bar_chart:', 'wide' )

kpi_box1, kpi_box2, kpi_box3, kpi_box4, kpi_box5, kpi_box16 = st.columns( 6 )

for kpi_box, text_plus_kpi in zip( [ kpi_box1, kpi_box2, kpi_box3, kpi_box4, kpi_box5, kpi_box16 ],
                               KPIs_dict.items()) :
    
    text = text_plus_kpi[0];        kpi = text_plus_kpi[1]
    kpi_box.markdown( f'<h4 style = "font-family:times;font-size:175%" >{text} : {kpi}</h4>', unsafe_allow_html=True )
    
reach_by_content_category_df = df.groupby( 'content_category' )['reach'].sum().\
    sort_values( ascending=True ).to_frame().reset_index()

chart_1, chart_2, chart_3 = st.columns( 3 )

chart_reach_by_content_category =  px.histogram( reach_by_content_category_df, x = 'reach', y = 'content_category', color = 'content_category',
             color_discrete_sequence= instagram_palette, template= 'simple_white', width = 600
             )    
chart_1.plotly_chart( chart_reach_by_content_category )

insta_img = Image.open( './Insta-logo.jpg' )
chart_2.write( insta_img )