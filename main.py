from app import *
from dash import dcc, html
import dash_ace


app.layout = dbc.Container([

    dcc.Location(id='url'),
    dbc.Row([
        dbc.Col([
            dbc.Button(html.Img(src="assets/logo_asimov_dark.png", className='img_button'),className='logo_button'),
        ], md= 4, className='coluna_logo'),
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    html.Button(html.I(className = "fa fa-arrow-left"), className='previous_button')
                ], md=4, className='col_previous_button'),
                dbc.Col([
                    html.Button([html.I(className = "fa fa-bars header-icon") , " Course Outline"], className='central_button')
                ], md=4, className='col_central_button'),
                dbc.Col([
                    html.Button(html.I(className = "fa fa-arrow-right"), className='next_button')
                ], md=4, className='col_next_button'),
            ])
        ], md=4,className='col_navigate_buttons'),
        dbc.Col([
             html.H5(["Daily XP ", html.I(className = "fa fa-spinner")])
        ], md=4, className='col_daily_xp'),
    ], justify="between", className='g-2 my-auto'),

    dbc.Row([
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader([html.I(className='fa fa-book'), html.H6(" Exercise")], className='card_header'),
                        dbc.CardBody([
                            html.H5("Categorial data in scatter plots"),
                            html.P("In the video, we explored how men's education and age at marriage related to other variables in our dataset, the divorce DataFrame. Now, you'll take a look at how women's education and age at marriage relate to other variables!\n"),
                            html.P("Your task is to create a scatter plot of each woman's age and income, layering in the categorical variable of education level for additional context.\n"),
                            html.P("The divorce DataFrame has been loaded for you, and woman_age_marriage has already been defined as a column representing an estimate of the woman's age at the time of marriage. pandas has been loaded as pd, matplotlib.pyplot has been loaded as plt, and Seaborn has been loaded as sns")

                        ])
                    ], className='card_question')
                ])
            ], className='g-2 my-auto'),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader([html.I(className='fa fa-check-circle-o'), html.H6(" Instructions")], className='card_header'),
                        dbc.CardBody([
                            html.P("Create a scatter plot that shows woman_age_marriage on the x-axis and income_woman on the y-axis; each data point should be colored based on the woman's level of education, represented by education_woman.")
                        ])
                    ], className='card_question')
                ])
            ], className='g-2 my-auto')
        ], md=5),
        
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    html.Div([
                        dash_ace.DashAceEditor(
                        id='input',
                        value='',
                        theme='twilight',
                        mode='python',
                        tabSize=1,
                        enableBasicAutocompletion=True,
                        enableLiveAutocompletion=True,
                        autocompleter='/autocompleter?prefix=',
                        placeholder='Python code ...',
                        height='90vh'
                        )
                    ])
                ])
            ], className='g-2 my-auto'),
        ], md=7)
    ], className='g-2 my-auto')
], fluid=True)

if __name__ == "__main__":
    app.run_server(port=8050, debug=True)