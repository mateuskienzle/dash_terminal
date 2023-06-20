from app import *
from dash import dcc, html, Input, Output, State, callback_context
import dash_ace

questao = 1

app.layout = dbc.Container([

    dcc.Location(id='url'),
    dbc.Row([
        dbc.Col([
            dbc.Button(html.Img(src="assets/logo_asimov_dark.png", className='img_button'),className='logo_button'),
        ], md= 4, className='coluna_logo'),
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    html.Button(html.I(className = "fa fa-arrow-left"), className='previous_button', id='botao_previous')
                ], md=4, className='col_previous_button'),
                dbc.Col([
                    html.Button([html.I(className = "fa fa-bars header-icon") , " Course Outline"], className='central_button')
                ], md=4, className='col_central_button'),
                dbc.Col([
                    html.Button(html.I(className = "fa fa-arrow-right"), className='next_button', id='botao_next')
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
                    
                ], id='cardExercise')
            ], className='g-2 my-auto'),
            dbc.Row([
                dbc.Col([
                    
                ], id='cardInstruction')
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

@app.callback(
    Output('cardExercise', 'children'),
    Output('cardInstruction', 'children'),
    Input('botao_next', 'n_clicks'),
    Input('botao_previous', 'n_clicks'),
)

def changeExercise(n1, n2):
    global questao
    trigg_id = callback_context.triggered[0]['prop_id'].split('.')[0]


    if trigg_id == '':
        
        question = open(f"questions/q1.txt").read().split('\n')

        card_exercise =  dbc.Card([
                    dbc.CardHeader([html.I(className='fa fa-book'), html.H6(" Exercise")], className='card_header'),
                    dbc.CardBody([
                        html.H5("ASIMOVZADA"),
                        html.P("Lorem Ipsum Asimov.\n"),
                        html.P("Lorem Ipsum Asimov.\n"),
                        html.P("Lorem Ipsum Asimov.")
                    ])
                ], className='card_question')
        
        card_instruction = dbc.Card([
                            dbc.CardHeader([html.I(className='fa fa-check-circle-o'), html.H6(" Instructions")], className='card_header'),
                            dbc.CardBody([
                                html.P("Lorem Ipsum Asimov.")
                            ])
                        ], className='card_question')

        return card_exercise, card_instruction

    if trigg_id == 'botao_next':

        if questao !=5:
            questao+=1
        question = open(f"questions/q{questao}.txt").read().split('\n')

        print(questao)

        try:
            splitada = (question[: question.index("")])
            last_splitada = (question[question.index("") +1:])
        except ValueError:
            []

        lista_aux = []
        lista_aux2 = []

        for i in splitada[2:]:
            lista_aux.append(html.P(i))
        
        for j in last_splitada[1:]:
            lista_aux2.append(html.P(j))

        card_exercise =  dbc.Card([
                    dbc.CardHeader([html.I(className='fa fa-book'), html.H6([" ", splitada[0]])], className='card_header'),
                    dbc.CardBody([
                        html.H5(splitada[1]),
                        *lista_aux
                    ])
                ], className='card_question')
        
        card_instruction = dbc.Card([
                            dbc.CardHeader([html.I(className='fa fa-check-circle-o'), html.H6([" ", last_splitada[0]])], className='card_header'),
                            dbc.CardBody([
                                *lista_aux2
                            ])
                        ], className='card_question')
        
        return card_exercise, card_instruction
    
    if trigg_id == 'botao_previous':

        if questao !=1:
            questao-=1
        question = open(f"questions/q{questao}.txt").read().split('\n')

        print(questao)

        try:
            splitada = (question[: question.index("")])
            last_splitada = (question[question.index("") +1:])
        except ValueError:
            []

        lista_aux = []
        lista_aux2 = []

        for i in splitada[2:]:
            lista_aux.append(html.P(i))
        
        for j in last_splitada[1:]:
            lista_aux2.append(html.P(j))

        card_exercise =  dbc.Card([
                    dbc.CardHeader([html.I(className='fa fa-book'), html.H6([" ", splitada[0]])], className='card_header'),
                    dbc.CardBody([
                        html.H5(splitada[1]),
                        *lista_aux
                    ])
                ], className='card_question')
        
        card_instruction = dbc.Card([
                            dbc.CardHeader([html.I(className='fa fa-check-circle-o'), html.H6([" ", last_splitada[0]])], className='card_header'),
                            dbc.CardBody([
                                *lista_aux2
                            ])
                        ], className='card_question')
        
        return card_exercise, card_instruction

if __name__ == "__main__":
    app.run_server(port=8050, debug=True)