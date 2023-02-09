import dataframe.dash_app_dataframe as dash_app_dataframe
from dash import html, dcc


def bar_chart_sample():
    sample_layout = html.Div(children=[
        html.Div(
            html.Button(
                dcc.Link(href='/dashapp1/', refresh=True),
            )
        ),
        html.Div(
            dcc.Link(href='/dashapp2/', refresh=True),
        ),
        dcc.Graph(
            id='graph1',
            figure=dash_app_dataframe.fig_data()
        ),
    ])
    return sample_layout
