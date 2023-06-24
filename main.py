from app import *
from dash import dcc, html, Input, Output, State, callback_context, no_update
import dash_ace

questionCounter = 1

app.layout = dbc.Container([

    dcc.Location(id='url'),
    dbc.Row([
        dbc.Col([
            dbc.Button(html.Img(src="assets/logo_asimov_dark.png", className='img_button'),className='logo_button'),
        ], md= 4, className='coluna_logo'),
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    html.Button(html.I(className = "fa fa-arrow-left"), className='previous_button', id='previousButton')
                ], md=4, xs=4, className='col_previous_button'),
                dbc.Col([
                    html.Button([html.I(className = "fa fa-bars header-icon") , " Course Outline"], className='central_button')
                ], md=4, xs=4, className='col_central_button'),
                dbc.Col([
                    html.Button(html.I(className = "fa fa-arrow-right"), className='next_button', id='nextButton')
                ], md=4, xs=4,className='col_next_button'),
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
                    dbc.Button("RUN", className='run_button', id='runButton')
                ], className='col_run_button')
            ]),
            dbc.Row([
                dbc.Col([
                    html.Div([
                        dash_ace.DashAceEditor(
                        id='terminalInput',
                        value='',
                        theme='twilight',
                        mode='python',
                        tabSize=1,
                        enableBasicAutocompletion=True,
                        enableLiveAutocompletion=True,
                        autocompleter='/autocompleter?prefix=',
                        placeholder='#Insira seu código aqui',
                        height='88vh'
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
    Input('nextButton', 'n_clicks'),
    Input('previousButton', 'n_clicks'),
    Input('runButton', 'n_clicks'),
    State('terminalInput', 'value')
)

def changeExercise(n1, n2, n3, input_terminal):
    global questionCounter
    trigg_id = callback_context.triggered[0]['prop_id'].split('.')[0]


    if trigg_id == '':
        
        question = open(f"questions/q1.txt").read().split('\n')

        try:
            splited = (question[: question.index("")])
            last_splited = (question[question.index("") +1:])
        except ValueError:
            []

        lista_aux = []
        lista_aux2 = []

        for i in splited[2:]:
            lista_aux.append(html.P(i))
        
        for j in last_splited[1:]:
            lista_aux2.append(html.P(j))

        card_exercise =  dbc.Card([
                    dbc.CardHeader([html.I(className='fa fa-book'), html.H6([" ", splited[0]])], className='card_header'),
                    dbc.CardBody([
                        html.H5(splited[1]),
                        *lista_aux
                    ])
                ], className='card_question')
        
        card_instruction = dbc.Card([
                            dbc.CardHeader([html.I(className='fa fa-check-circle-o'), html.H6([" ", last_splited[0]])], className='card_header'),
                            dbc.CardBody([
                                *lista_aux2
                            ])
                        ], className='card_question')
        
        return card_exercise, card_instruction

    if trigg_id == 'nextButton':

        if questionCounter !=5:
            questionCounter+=1
        question = open(f"questions/q{questionCounter}.txt").read().split('\n')

        # print(questionCounter)

        try:
            splited = (question[: question.index("")])
            last_splited = (question[question.index("") +1:])
        except ValueError:
            []

        lista_aux = []
        lista_aux2 = []

        for i in splited[2:]:
            lista_aux.append(html.P(i))
        
        for j in last_splited[1:]:
            lista_aux2.append(html.P(j))

        card_exercise =  dbc.Card([
                    dbc.CardHeader([html.I(className='fa fa-book'), html.H6([" ", splited[0]])], className='card_header'),
                    dbc.CardBody([
                        html.H5(splited[1]),
                        *lista_aux
                    ])
                ], className='card_question')
        
        card_instruction = dbc.Card([
                            dbc.CardHeader([html.I(className='fa fa-check-circle-o'), html.H6([" ", last_splited[0]])], className='card_header'),
                            dbc.CardBody([
                                *lista_aux2
                            ])
                        ], className='card_question')
        
        return card_exercise, card_instruction
    
    if trigg_id == 'previousButton':

        if questionCounter !=1:
            questionCounter-=1
        question = open(f"questions/q{questionCounter}.txt").read().split('\n')

        print(questionCounter)

        try:
            splited = (question[: question.index("")])
            last_splited = (question[question.index("") +1:])
        except ValueError:
            []

        question_content = []
        instruction_content = []

        for i in splited[2:]:
            question_content.append(html.P(i))
        
        for j in last_splited[1:]:
            instruction_content.append(html.P(j))

        card_exercise =  dbc.Card([
                    dbc.CardHeader([html.I(className='fa fa-book'), html.H6([" ", splited[0]])], className='card_header'),
                    dbc.CardBody([
                        html.H5(splited[1]),
                        *question_content
                    ])
                ], className='card_question')
        
        card_instruction = dbc.Card([
                            dbc.CardHeader([html.I(className='fa fa-check-circle-o'), html.H6([" ", last_splited[0]])], className='card_header'),
                            dbc.CardBody([
                                *instruction_content
                            ])
                        ], className='card_question')
        
        return card_exercise, card_instruction
    
    if trigg_id == 'runButton':

        with open('terminal_input.txt', 'w') as f:
            f.write(input_terminal)

        return no_update
    


if __name__ == "__main__":
    app.run_server(port=8050, debug=True)