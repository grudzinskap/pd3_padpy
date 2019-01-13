import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go


wykres1=[pd.read_csv("wykres1_e", sep="\t"), pd.read_csv("wykres1_p", sep="\t"),pd.read_csv("wykres1_m", sep="\t")]
merge=[pd.read_csv("merge_e", sep="\t"),pd.read_csv("merge_p", sep="\t"),pd.read_csv("merge_m", sep="\t")]
mapa=[pd.read_csv("mapa_e", sep="\t"),pd.read_csv("mapa_p", sep="\t"),pd.read_csv("mapa_m", sep="\t")]

names=["English Language Learners Stack Exchange", "Politics Stack Exchange","Movies & TV Stack Exchange"]

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# app.layout =html.Div([
#         html.Div([
#             dcc.Dropdown(
#                 id='stack',
#                 options=[{'label': names[i], 'value': i} for i in range(3)],
#                 value='English Language Learners Stack Exchange'),style={'width': '49%', 'display': 'inline-block'}
# )
# dcc.Slider(
#     id='n-slider',
#     min=1,
#     max=15,
#     value=10,
#     marks={str(i + 1): str(i + 1) for i in range(15)}
#
# )], style = {'width': '49%', 'display': 'inline-block'}),
#
# html.Div([dcc.Graph(id='graph-with-slider2'), dcc.Graph(id='graph-with-slider')]
#          , style={'width': '49%', 'padding': '0px 20px 20px 20px'})
# ])

app.layout =html.Div([
            dcc.Dropdown(
                id='stack',
                options=[{'label': names[i], 'value': i} for i in range(3)],
                value=0)
    ,
            dcc.Slider(
               id='n-slider',
               min=1,
               max=15,
               value=10,
               marks={str(i + 1): str(i + 1) for i in range(15)}

            ),
            html.Div([dcc.Graph(id='graph-with-slider2'), dcc.Graph(id='graph-with-slider'),dcc.Graph(id='graph-with-slider3'),dcc.Graph(id='graph-with-slider4'),dcc.Graph(id='heatmap')]),

            ],style={'width': '49%', 'display': 'inline-block'})



@app.callback(
    dash.dependencies.Output('graph-with-slider2', 'figure'),
    [dash.dependencies.Input('n-slider', 'value'),
     dash.dependencies.Input('stack', 'value')])
def update_figure(n, stack):
    df2 = wykres1[stack].head(n)

    data = [go.Bar(
        x=df2.TagName,
        y=df2.Count,

    )]



    return {
        'data': data,
        'layout': go.Layout(
            xaxis={'title': 'Tags'},
            yaxis={'title': 'Count'},
            #margin={'l': 10, 'b': 60, 't': 60, 'r': 400},
            legend={'x': 0, 'y': 1},
            title='The most popular tags',
        )
    }

@app.callback(
    dash.dependencies.Output('graph-with-slider', 'figure'),
    [dash.dependencies.Input('n-slider', 'value'),
     dash.dependencies.Input('stack', 'value')])
def update_figure(n,stack):




    trace1 = go.Bar(
        x=list(merge[stack].country[:n]),
        y=list(merge[stack].q[:n]),
        name='Questions'
    )
    trace2 = go.Bar(
        x=list(merge[stack].country[:n]),
        y=list(merge[stack].ans[:n]),
        name='Answers'
    )

    data = [trace1, trace2]


    return {
        'data': data,
        'layout': go.Layout(
            barmode='stack',
            xaxis={'title': 'Tags'},
            yaxis={'title': 'Count'},
            #margin={'l': 440, 'b': 40, 't': 10, 'r': 10},
            legend={'x': 0, 'y': 1},
            title='Number of posts',
        )
    }

@app.callback(
    dash.dependencies.Output('graph-with-slider3', 'figure'),
    [dash.dependencies.Input('n-slider', 'value'),
     dash.dependencies.Input('stack', 'value')])
def update_figure(n,stack):



    data = [go.Bar(
        x=list(merge[stack].sort_values(by="q", ascending=False).country[:n]),
        y=list(merge[stack].sort_values(by="q", ascending=False).q[:n]),
    )]
    return {
        'data': data,
        'layout': go.Layout(

            xaxis={'title': 'Tags'},
            yaxis={'title': 'Count'},
            #margin={'l': 440, 'b': 40, 't': 10, 'r': 10},
            legend={'x': 0, 'y': 1},
            title='Number of questions',
        )
    }



@app.callback(
    dash.dependencies.Output('graph-with-slider4', 'figure'),
    [dash.dependencies.Input('n-slider', 'value'),
     dash.dependencies.Input('stack', 'value')])
def update_figure(n,stack):
    data = [go.Bar(
        x=list(merge[stack].sort_values(by="ans", ascending=False).country[:n]),
        y=list(merge[stack].sort_values(by="ans", ascending=False).ans[:n]),
    )]


    return {
        'data': data,
        'layout': go.Layout(

            xaxis={'title': 'Tags'},
            yaxis={'title': 'Count'},
            #margin={'l': 440, 'b': 40, 't': 10, 'r': 10},
            legend={'x': 0, 'y': 1},
            title='Number of answers',
        )
    }



@app.callback(
    dash.dependencies.Output('heatmap', 'figure'),
    [dash.dependencies.Input('n-slider', 'value')])
def update_figure(n):
    df2 = wykres1[0].head(n)

    data = [go.Bar(
        x=df2.TagName,
        y=df2.Count
    )]



    return {
        'data': data,
        'layout': go.Layout(
            xaxis={'title': 'Tags'},
            yaxis={'title': 'Count'},
            #margin={'l': 440, 'b': 40, 't': 10, 'r': 10},
            legend={'x': 0, 'y': 1},
            title='The most popular tags',
        )
    }


if __name__ == '__main__':
    app.run_server(debug=True)

