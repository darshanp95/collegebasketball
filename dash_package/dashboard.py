
# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash_package import app
from queries import *
import plotly.graph_objs as go

def avg_salaries():

    coach_names = [tup[0] for tup in average_coach_salary()]
    coach_salaries = [tup[1] for tup in average_coach_salary()]

    return [coach_names, coach_salaries]




app.layout = html.Div(children=[
    html.H1(children='Average Salaries'),

    html.Div(children='''
        An average of all of the coaches salaries in college basketball
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [{'x': avg_salaries()[0], 'y': avg_salaries()[1], 'type': 'bar'}],
            'layout': go.Scatter('title': {'Average Salaries'},
            'type': 'lines', 'y' : average_all_coaches_salarycoach_salary()}
                }}
    )
])
