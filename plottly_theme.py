import plotly.graph_objects as go

def apply_custom_theme(fig, title="Plot Title", subtitle="Subtitle", xlabel="xlabel", ylabel="ylabel"):
    """
    Applies a custom theme to a Plotly figure.

    Parameters:
        fig (go.Figure): The figure to style.
        title (str): The main title of the plot.
        subtitle (str): A subtitle under the main title.
        xlabel (str): Label for the x-axis.
        ylabel (str): Label for the y-axis.
    """
    fig.update_layout(
        title=dict(
            text=f"{title}<br><span style='font-size:12px;color:#888888;'>{subtitle}</span>",
            x=0.05,
            xanchor='left',
            font=dict(size=18, family='IBM Plex Sans, sans-serif', color='#222222')
        ),
        xaxis=dict(
            title=xlabel,
            titlefont=dict(size=14, family='IBM Plex Sans, sans-serif', color='#222222'),
            tickfont=dict(size=12, family='IBM Plex Sans, sans-serif', color='#555555'),
            showgrid=True,
            gridwidth=0.5,
            gridcolor='#EEEEEE',
            zeroline=False,
            showline=False
        ),
        yaxis=dict(
            title=ylabel,
            titlefont=dict(size=14, family='IBM Plex Sans, sans-serif', color='#222222'),
            tickfont=dict(size=12, family='IBM Plex Sans, sans-serif', color='#555555'),
            showgrid=True,
            gridwidth=0.5,
            gridcolor='#EEEEEE',
            zeroline=False,
            showline=False
        ),
        legend=dict(
            font=dict(size=12, family='IBM Plex Sans, sans-serif'),
            x=1, y=1.1, xanchor='right', yanchor='top', orientation='h'
        ),
        plot_bgcolor='white',
        paper_bgcolor='white',
        margin=dict(l=40, r=40, t=80, b=0),
        font=dict(family='IBM Plex Sans, sans-serif')
    )
    
    return fig
