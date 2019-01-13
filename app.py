import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1('Stack Data Analysis'),
    dcc.Tabs(id="tabs-example", value='tab-1-example', children=[
        dcc.Tab(label='Hello', value='tab-1-example'),
        dcc.Tab(label='Word Cloud', value='tab-2-example'),
        dcc.Tab(label='Map', value='tab-3-example'),
        dcc.Tab(label='The best of', value='tab-4-example'),
    ]),
    html.Div(id='tabs-content-example')
])


@app.callback(Output('tabs-content-example', 'children'),
              [Input('tabs-example', 'value')])
def render_content(tab):
    if tab == 'tab-1-example':
        return html.Div([
            html.H3('Hello in application ..... Choose stack to analyse:'),
            dcc.Checklist(
                options=[
                    {'label': 'English Language Learners Stack Exchange - Q&A for speakers of other languages learning English.', 'value': 'ell'},
                    {'label': 'Politics Stack Exchange - Q&A for people interested in governments, policies, and political processes.', 'value': 'politics'},
                    {'label': 'Movies & TV Stack Exchange - Q&A site for movie and tv enthusiasts.', 'value': 'movies'}
                ],
                values=[]
            ),

            html.H3('Descripion tabs'),
        ])
    elif tab == 'tab-2-example':
        return html.Div([
            html.H3('Tab content 2'),
            dcc.Slider(value=4, min=-10, max=20, step=0.5,
                       labels={-5: '-5 Degrees', 0: '0', 10: '10 Degrees'}),
            dcc.Graph(
                id='graph-2-tabs',
                figure={
                    'data': [{
                        'x': [1, 2, 3],
                        'y': [5, 10, 6],
                        'type': 'bar'
                    }]
                }
            )
        ])
    elif tab == 'tab-3-example':
        return html.Div([
            html.H3('Tab content 2'),
            dcc.Graph(
                id='graph-2-tabs',
                figure={
                    'data': [{
                        'x': [1, 2, 3],
                        'y': [5, 10, 6],
                        'type': 'bar'
                    }]
                }
            )
        ])
    elif tab == 'tab-4-example':
        return html.Div([
            html.H3('Tab content 2'),
            dcc.RangeSlider(
                marks={-1:'-1', 0:'0', 1:'1'},
                min=-1,
                max=1,
                value=[-1, 1]
            ),
            dcc.Graph(
                id='graph-2-tabs',
                figure={
                    'data': [{
                        'x': [1, 2, 3],
                        'y': [5, 10, 6],
                        'type': 'bar'
                    }]
                }
            )
        ])


if __name__ == '__main__':
    app.run_server(debug=True)