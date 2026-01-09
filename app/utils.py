import plotly.express as px
from plotly.graph_objects import Figure


def human_readable(n):
    if n >= 1_000_000_000:
        return f"{n/1_000_000_000:.0f}Bn"
    elif n >= 1_000_000:
        return f"{n/1_000_000:.0f}Mn"
    elif n >= 1_000:
        return f"{n/1_000:.0f}K"
    else:
        return str(n)
    
instagram_palette = [
    "#1F6AE1",  # Blue
    "#3A5BDC",  # Blue-Purple
    "#5A4FD6",  # Indigo
    "#7A3FCB",  # Purple
    "#9B3CB4",  # Violet
    "#C13584",  # Magenta
    "#E1306C",  # Pink
    "#F56040",  # Orange
    "#FCAF45",  # Light Orange
    "#FFD166"   # Yellow
]

months_order = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

def apply_figure_layout( fig : Figure, title_text = '', xlabel_text = '', ylabel_text = '' ) -> Figure :
    
    xlabel_text = fig.layout.xaxis.title.text if xlabel_text == '' else xlabel_text
    ylabel_text = fig.layout.yaxis.title.text if ylabel_text == '' else ylabel_text
    title_text = fig.layout.title.text if ylabel_text == '' else title_text
    
    fig.update_layout(
        
        title = dict(
            text = title_text,
            font = dict( family = 'times', size = 25, color = 'black' )
        ),
        
        xaxis = dict(
            title = dict(
                text = xlabel_text, font = dict( family = 'times', size = 20, color = 'black' )
            ),
        tickfont =dict( family = 'times', size = 15, color = 'black' )

        ),
        
        yaxis = dict(
            title = dict(
                text = ylabel_text, font = dict( family = 'times', size = 20, color = 'black' )
            ),
        tickfont =dict( family = 'times', size = 15, color = 'black' )

        ),
    )  
    
    return fig

