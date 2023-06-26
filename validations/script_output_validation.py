from validations.components.script_handler import Script

class ScriptOutputValidation:

    has_errors: bool = True
    error_type: str = ''
    script_output: str = ''

    def __init__(self, script_path: str, answer_path:str) -> None:
        self.script = Script(script_path)
        self.answer_script = Script(answer_path)

    def validate(self) -> bool:
        self.script.run_script()
        self.answer_script.run_script()

        success = False
        message = ''
        if self.script.has_errors:
            self.error_type = 'Script com erro'
            self.script_output = self.script.error_output
            # print(f'[ ScriptOutputValidation ] Script com erro ao rodar')
            # print(f'[ ScriptOutputValidation ] Output_ do erro {self.script.error_output}')
            message = f'Script com erro ao rodar\nOutput do seu código:\n {self.script.error_output}'
        elif self.script.success_output == self.answer_script.success_output:
            self.script_output = self.script.success_output
            # print(f'[ ScriptOutputValidation ] Sucesso')
            # print(f'[ ScriptOutputValidation ] Output esperada:\n {self.answer_script.success_output}')
            # print(f'[ ScriptOutputValidation ] Output obtida:\n {self.script.success_output}')
            message = f'Sucesso\n\nOutput esperada:\n {self.answer_script.success_output}\nOutput obtida:\n {self.script.success_output}'
            success = True
        else:
            self.script_output = self.script.success_output
            # print(f'[ ScriptOutputValidation ] Erro. O resultado está diferente da resposta esperada')
            # print(f'[ ScriptOutputValidation ] Output esperada:\n {self.answer_script.success_output}')
            # print(f'[ ScriptOutputValidation ] Output obtida:\n {self.script.success_output}')
            message = f'Erro no resultado.\nOutput esperada:\n {self.answer_script.success_output}\nOutput obtida:\n {self.script.success_output}'
        
        return success, message
    
if __name__ == '__main__':

    folder_path = 'desafios_de_output/numeros_pares'
    script_path = f'{folder_path}/tentativas/tentativa02.py'
    answer_path = f'{folder_path}/resposta.py'
    

    output_validate = ScriptOutputValidation(script_path, answer_path)
    output_validate.validate()

