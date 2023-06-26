import json
import os

from dash import dcc, html, Input, Output, State, callback_context, no_update
import dash_ace

from app import *
from tools import *
from validations.script_output_validation import ScriptOutputValidation


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
                    html.Button([html.I(className = "fa fa-bars header-icon") , " Guia de Desafios"], className='central_button')
                ], md=4, xs=4, className='col_central_button'),
                dbc.Col([
                    html.Button(html.I(className = "fa fa-arrow-right"), className='next_button', id='nextButton')
                ], md=4, xs=4,className='col_next_button'),
            ])
        ], md=4,className='col_navigate_buttons'),
        dbc.Col([
            dbc.Button("RUN", className='run_button', id='runButton')
        ], md=4, className='col_run_button')
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
                        id='terminalInput',
                        value='',
                        theme='twilight',
                        mode='python',
                        tabSize=1,
                        enableBasicAutocompletion=True,
                        enableLiveAutocompletion=True,
                        autocompleter='/autocompleter?prefix=',
                        placeholder='#Insira seu código aqui',
                        height='70vh'
                        )
                    ])
                ])
            ], className='g-2 my-auto'),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader([
                            html.H6('OUTPUT:')
                        ], className='cardOutputHeader'),
                        dbc.CardBody([
                            
                        ], id='cardOutput', className='cardOutputBody')
                    ])
                ], md=11)
            ], className= 'g-2 my-auto')
        ], md=7)
    ], className='g-2 my-auto')
], fluid=True)

@app.callback(
    Output('cardExercise', 'children'),
    Output('cardInstruction', 'children'),
    Output('cardOutput', 'children'),
    Input('nextButton', 'n_clicks'),
    Input('previousButton', 'n_clicks'),
    Input('runButton', 'n_clicks'),
    State('terminalInput', 'value')
)

def changeExercise(n1, n2, n3, input_terminal):
    global questionCounter
    trigg_id = callback_context.triggered[0]['prop_id'].split('.')[0]

    if trigg_id == 'nextButton':
        if questionCounter !=2:
            questionCounter+=1
    elif trigg_id == 'previousButton':
        if questionCounter !=1:
            questionCounter-=1

    
    if trigg_id in ['nextButton', 'previousButton', '']:

        with open(f"questions_json/q{questionCounter}.json") as raw_question:
            question = json.loads(raw_question.read())

        exercicio_tag = 'Exercício'
        instruction_name_tag = 'Instrução'
        exercicio_name_tag = question['title']
        exercicio_descricao = question['description']
        instruction_tag = question['instructions']

        output_message = []
        for msg in exercicio_descricao.split('\n'):
            output_message.extend([html.Br(),html.Br(), msg])

        card_exercise =  dbc.Card([
            dbc.CardHeader([html.I(className='fa fa-book'), html.H6([" ", exercicio_tag])], className='card_header'),
            dbc.CardBody([
                html.H5(exercicio_name_tag),
                html.P(output_message[1:]),
            ])
        ], className='card_question')

        output_message = []
        for msg in instruction_tag.split('\n'):
            output_message.extend([html.Br(),html.Br(), msg])
        
        card_instruction = dbc.Card([
                            dbc.CardHeader([html.I(className='fa fa-check-circle-o'), html.H6([" ", instruction_name_tag])], className='card_header'),
                            dbc.CardBody([
                            html.P(output_message[1:]),
                            ])
                        ], className='card_question')
        
        return card_exercise, card_instruction, 'Clique em "RUN" para rodar o código'


    if trigg_id == 'runButton':


        file_name = generate_file_input_name()
        with open(file_name, 'w') as f:
            f.write(input_terminal)


        script_path = file_name
        answer_path = f'solutions/sol{questionCounter}.py'
        
        output_validate = ScriptOutputValidation(script_path, answer_path)
        success, message = output_validate.validate()
        print(message)
        os.remove(file_name)

        output_message = []
        for msg in message.split('\n'):
            output_message.extend([html.Br(), msg])
        
        return no_update, no_update, output_message[1:]
    


if __name__ == "__main__":
    app.run_server(port=8050, debug=False)