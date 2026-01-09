import numpy as np
import pandas as pd
import streamlit as st
import streamlit_shadcn_ui as ui
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image
from utils import human_readable, instagram_palette, apply_figure_layout, months_order
import os
# streamlit run app/app.py

import streamlit as st


df = pd.read_csv( 'Data/Feature Engineered Data/Feature Engineered Data.csv' )


media_types = df['media_type'].value_counts().index

with st.sidebar :
    st.subheader( 'Media Type' )
    checkbox_options_multiple = [
    {"label": "Carousel", "id": "Carousel", "default_checked":True},
    {"label": "Video", "id": "Video", "default_checked":True},
    {"label": "Reel", "id": "Reel", "default_checked":True},
    {"label": "Photo", "id": "Photo", "default_checked":True}
]
    checkbox_dict = ui.checkbox(mode="multiple", options=checkbox_options_multiple, key="cb4")
print( checkbox_dict )
media_type =  [ k for k, v in checkbox_dict.items() if v == True ]
df = df.query( 'media_type in @media_type' )

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

chart_1, chart_2, chart_3 = st.columns( [ 0.5, 0.4, 0.75 ] )

chart_reach_by_content_category =  px.histogram( reach_by_content_category_df, x = 'reach', y = 'content_category', color = 'content_category',
             color_discrete_sequence= instagram_palette, template= 'simple_white', width = 600
             )
chart_reach_by_content_category = apply_figure_layout( chart_reach_by_content_category, title_text= 'Reach By Content Category', xlabel_text= 'Total Reach'  , ylabel_text=' ' ).\
                                  update_layout( showlegend = False )
chart_1.plotly_chart( chart_reach_by_content_category, use_container_width= True )

insta_img = Image.open( './Insta-logo.jpg' ).resize( ( 350, 350 ) )
chart_2.write( insta_img )

reach_and_caption_len_by_hashs_df =   df.groupby( 'hashtags_count' )[ [ 'reach', 'caption_length' ] ].sum().reset_index()
chart_reach_caption_by_hash_count = go.Figure()
chart_reach_caption_by_hash_count.add_bar(
    x = reach_and_caption_len_by_hashs_df['hashtags_count'],
    y = reach_and_caption_len_by_hashs_df['reach'],
    marker_color="#7A3FCB",
    name = 'Reach by Hashtags Count'
)
chart_reach_caption_by_hash_count.add_scatter(
    x = reach_and_caption_len_by_hashs_df['hashtags_count'],
    y = reach_and_caption_len_by_hashs_df['caption_length'],
    mode = "lines+markers",
    yaxis= 'y2',
    name = 'Caption Length by Hashtags Count'
)
chart_reach_caption_by_hash_count.update_layout(
    title="Relation between reach and caption length by hashtags count",
    xaxis_title="Hashtags count",

    yaxis=dict(
        title="Sum of reach",
        tickformat=".2s"
    ),

    yaxis2=dict(
        title=dict(
                text = 'Sum of Caption Length', font = dict( family = 'times', size = 20, color = 'black' )
            ),
        overlaying="y",
        side="right",
        tickformat=".2s",
        tickfont =dict( family = 'times', size = 15, color = 'black' )

    ),
    
    template = 'simple_white', bargap = 0.2,
    
    legend = dict(
        orientation = 'h', y = 1.25, x = 0.2,
        font = dict( family = 'times', size = 18, color = 'black' )
    )
    
)    
chart_reach_caption_by_hash_count = apply_figure_layout( chart_reach_caption_by_hash_count )
chart_3.plotly_chart( chart_reach_caption_by_hash_count, use_container_width=True )

chart_21, chart_22 = st.columns( [0.3, 0.7] ) 

chart_followers_gained_by_traffic = px.histogram(df, x = 'traffic_source', y='followers_gained', color = 'traffic_source',
             color_discrete_sequence= instagram_palette[ 4 : 9 ], template = 'simple_white', text_auto=True,
             )
chart_followers_gained_by_traffic = apply_figure_layout( chart_followers_gained_by_traffic, ylabel_text= ' ', title_text = 'Total No. of Followers gained by Traffic Source' ).update_layout( showlegend = False )
chart_followers_gained_by_traffic = chart_followers_gained_by_traffic.update_layout(title=dict( font = dict( size = 17 ) ) )
chart_21.plotly_chart( chart_followers_gained_by_traffic, use_container_width= True )

df['Month Name'] = pd.Categorical( values = df['Month Name'], categories= months_order, ordered=True)
followers_gained_by_month_df = df.groupby( 'Month Name' )['followers_gained'].sum().to_frame().reset_index()

chart_followers_gained_by_month = px.line( followers_gained_by_month_df, x = 'Month Name', y = 'followers_gained',
        template = 'simple_white', markers = True, text='followers_gained', width = 900)
chart_followers_gained_by_month.update_traces(
    texttemplate="%{y:.2s}",
    textposition="top center",
    line=dict(width=5, color = '#E1306C'),
    textfont=dict(
        family="Montserrat",
        size=20,
        color="black"
    )
)
chart_followers_gained_by_month = apply_figure_layout(  chart_followers_gained_by_month, ylabel_text=' ', title_text= 'Total Followers Gained by Month' ).update_layout(title=dict(font =dict( size = 17 )))
chart_22.plotly_chart( chart_followers_gained_by_month, use_container_width=True )