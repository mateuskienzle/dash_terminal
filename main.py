from app import *
from dash import dcc, html


app.layout = dbc.Container([

    dcc.Location(id='url'),
    dbc.Row([
        dbc.Col([
            dbc.Button(html.Img(src="assets/logo_asimov_dark.png", className='img_button'),className='logo_button'),
        ], md= 4),
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    html.Button("<-", className='button_previous')
                ]),
                dbc.Col([
                    html.Button([html.I(className = "fa fa-bars header-icon") , " Course Outline"], className='button_center')
                ]),
                dbc.Col([
                    html.Button("->", className='button_next')
                ]),
            ])
        ], md=4, style={'text-align' : 'center'}),
        dbc.Col([
            html.Legend("Daily XP")
        ], md=4, style={'text-align' : 'end'}),
    ], justify="between", className='g-2 my-auto'),

    dbc.Row([
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader(["Card Header"], className='card_header'),
                        dbc.CardBody([
                            html.Legend("Col1")
                        ])
                    ], className='card_question')
                ])
            ], className='g-2 my-auto'),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader(["Card Header2"], className='card_header'),
                        dbc.CardBody([
                            html.Legend("Col4")
                        ])
                    ], className='card_question')
                ])
            ], className='g-2 my-auto')
        ], md=5),
        
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.Legend("Col2")
                        ])
                    ], className='card_prompt_superior')
                ])
            ], className='g-2 my-auto'),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.Legend("Col3")
                        ])
                    ], className='card_prompt_inferior')
                ])
            ], className='g-2 my-auto'),
        ],md=7)
    ], className='g-2 my-auto')
], fluid=True)

if __name__ == "__main__":
    app.run_server(port=8050, debug=True)