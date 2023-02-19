

import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import plotly
import random
import plotly.graph_objs as go
from collections import deque
import pandas as pd






app = dash.Dash(__name__)

header_list = ['Time', 'Humidity', 'Temperature','pH']

df = pd.read_csv(r'C:\Users\saulo\FarmSystemIoT\backend\databaseedge\sensordatalist.csv', names=header_list)

get_temp = df['Temperature'].tail(20)
get_time = df['Time'].tail(20)
get_humi = df['Humidity'].tail(20)








app.layout = html.Div(

    [   
      
          







        
        html.Div(
            [
                html.Img(src=app.get_asset_url('sun.png'), style={
                    'width': '50px', 'height': '50px', 'position': 'absolute', 'textAlign': 'center',
                    "margin-left": "10px",
                    "padding-top": "10px",
                }),


                html.Div(
                    [
                        html.H1(
                            "Sistema IoT Smartfarm",
                            style={
                                "margin-left": "100px",
                                "padding-top": "10px",
                                "color": "white",
                            },
                        )
                    ]
                ),
            ],
            style={
                "background-color": "#2ECC71",
                "height": "70px",
            },
        ),
        
   
          html.Div([
              html.Div([
            html.Div([
          html.Div([
                    html.Div(id='temp'),
                    html.Div(id='humi')
                ], className='temp_humidity_row')
            ], className='temp_humidity_column')
        ], className='temp_humidity twelve columns')
    ], className='row'), 
    

   





       

       
        dcc.Graph(id='live-graph', animate=False,
                  style={'background-color': 'rgba(0,0,0,0)', 'opacity': '0.7',
                         'width': '60%', 'height': '90%', 'position': 'center',
                         'textAlign': 'center',
                         "margin-left": "270px",

                         "padding-top": "40px",
                         


                         },),





        dcc.Interval(
            id='graph-update',
            interval=1000,
            n_intervals=0
        ),
    ]
)


@ app.callback(
    Output('live-graph', 'figure'),
    [Input('graph-update', 'n_intervals')]
)
def update_graph_scatter(n):
    header_list = ['Time', 'Humidity', 'Temperature','pH','pHpred']
    df = pd.read_csv(r'C:\Users\saulo\FarmSystemIoT\backend\databaseedge\sensordatalist.csv', names=header_list)

    get_temp = df['Temperature'].tail(20)
    get_time = df['Time'].tail(20)
    get_humi = df['Humidity'].tail(20)
    get_pH = df['pH'].tail(15)
    get_pHpred = df['pHpred'].tail(20)
   

    X = get_time

    Y1 = get_pHpred

    Y2 = get_pH
 

  








    data = go.Scatter(
        x=list(X),
        y=list(Y1),
        name='Previsão do pH',
        mode='lines+markers'
    )

    data2 = go.Scatter(

        x=list(X),
        y=list(Y2),
        name='Valor pH Real',
        mode='lines+markers'
    )










    layout = go.Layout(
        title='Valores pH',
        xaxis=dict(
            title='Tempo'
        ),
        yaxis=dict(
            title='Valor pH'
        )
    )

   

    return {'data': [data, data2],
            'layout': go.Layout(xaxis=dict(
                title='Tempo'
            ), yaxis=dict(
                title='Valores de pH'
            ))}


@ app.callback(
    Output('temp', 'children'),
    [Input('graph-update', 'n_intervals')]
)
def update_temp(n):
    header_list = ['Time', 'Humidity', 'Temperature','pH']
    df = pd.read_csv(r'C:\Users\saulo\FarmSystemIoT\backend\databaseedge\sensordatalist.csv', names=header_list)

    get_temp = df['Temperature'].tail(20)
    get_time = df['Time'].tail(20)
    get_humi = df['Humidity'].tail(20)
    
    temp = get_temp.iloc[-1]
    return [
        html.Div([
            html.Img(src=app.get_asset_url('hot.png'),
                     style={'height': '50px',
                            'width': '50px',
                            'position': 'absolute',
                            'textAlign': 'center',
                            "margin-left": "400px",
                            "padding-top": "10px",
                             }),
            html.Div([
                
                html.Div('°C', className='symbol',
                style={'height': '50px',
                            'width': '50px',
                            "margin-left": "530px",
                            'top': '130px'
                           
                             } ),
                

                html.Div('{0:.1f}'.format(temp),
                         className='numeric_value',
                         style={'height': '50px',
                            'width': '50px',
                            "margin-left": "460px",
                            "padding-top": "10px",
                            'font-size': '32px',
                            'margin-bottom': '-10px',
                            'font-weight': 'bold',
                            'textAlign': 'center',                
                             'position': 'absolute',
                             'top': '70px',
                             'color':'#666666',                         
                             } ),
            

            ], className = 'temp_symbol')
        ], className='image_temp_row'),
        
               


        html.P('Temperatura', style={'color': '#666666',
                                 'width': '10px',
                            "margin-left": "460px",
                            "padding-top": "10px",
                            'font-size': '12px',
                            'margin-bottom': '-10px',
                            'font-weight': '10',
                            'textAlign': 'center',                
                             'position': 'absolute',
                             'top': '120px',                         
                             } ),
    ]


@ app.callback(
    Output('humi', 'children'),
    [Input('graph-update', 'n_intervals')]
)
def update_humi(n):
    header_list=['Time', 'Humidity', 'Temperature','pH']
    df = pd.read_csv(r'C:\Users\saulo\FarmSystemIoT\backend\databaseedge\sensordatalist.csv', names=header_list)

    get_temp=df['Temperature'].tail(20)
    get_time=df['Time'].tail(20)
    get_humi=df['Humidity'].tail(20)
    
   
    hum = get_humi.iloc[-1]
    return [
        html.Div([
            html.Img(src=app.get_asset_url('humidity.png'),
                      style={'height': '50px',
                            'width': '50px',
                            'position': 'absolute',
                            'textAlign': 'center',
                            "margin-left": "570px",
                            "padding-top": "10px",
                            'top': '70px'
                             }),
            html.Div([
                html.Div('%', className='symbol',
                style={'height': '50px',
                            'width': '50px',
                            "margin-left": "700px",
                           'top': '20px',                         
                             } ),
                            
                                                             
                            
                html.Div('{0:.1f}'.format(hum),
                         className='numeric_value',
                          style={'height': '50px',
                            'width': '50px',
                            "margin-left": "630px",
                            "padding-top": "10px",
                            'font-size': '32px',
                            'margin-bottom': '-10px',
                            'font-weight': 'bold',
                            'textAlign': 'center',                
                             'position': 'absolute',
                             'top': '70px', 
                             'color':'#666666'                        
                             } )
            ], className='temp_symbol')
        ], className='image_temp_row'),

        html.P('Humidade', style={'color': '#666666',
                                 'width': '10px',
                            "margin-left": "560px",
                            "padding-top": "10px",
                            'font-size': '12px',
                            'margin-bottom': '-10px',
                            'font-weight': '10',
                            'textAlign': 'center',                
                             'position': 'absolute',
                             'top': '120px',                         
                             } )
    ]

 








if __name__ == '__main__':
    app.run_server(debug=True)
