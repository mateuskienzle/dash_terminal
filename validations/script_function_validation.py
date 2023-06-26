from validations.components.module_handler import Modules

ERROR_TYPES = {
    0: 'Módulo com erro',
    1: 'Módulo não contém a função solicitada',
    2: 'Função não contém os argumentos solicitados',
    3: 'Função com resultado discrepante da solução',
    5: 'Erro ao rodar função'

}

class ScriptFunctionValidation:

    has_errors: bool = True
    error_code: int = -1
    error_type: str = ''
    function_output: str = ''

    def __init__(self, module_path: str, answer_module_path:str) -> None:
        self.module = Modules(module_path)
        self.answer_module = Modules(answer_module_path)

    def _set_error(self, error_code: int, exception_text: str = ''):
        self.error_code = error_code
        self.error_type = ERROR_TYPES[error_code]
        self.has_errors = True

        if error_code == 0:
            print(f'[ ScriptFunctionValidation ] Script com erro ao rodar')
            print(f'[ ScriptFunctionValidation ] Output do erro: {self.module.global_error}')
        elif error_code == 1:
            print(f'[ ScriptFunctionValidation ] Erro. Não foi encontrada a função de nome {self.answer_module.function_name}')
        elif error_code == 2:
            function_name = self.answer_module.function_name
            function_args = self.answer_module.get_function_args(function_name)
            print(f'[ ScriptFunctionValidation ] Erro. Não foram encontrados os argumentos corretos: ({",".join(function_args)})')
        elif error_code == 5:
            print(f'[ ScriptFunctionValidation ] Erro ao rodar função: {exception_text}')
        elif error_code == 3:
            print(f'[ ScriptFunctionValidation ] Resultado não está batendo')
            print(f'{exception_text}')


    def _check_module_consistency(self) -> bool:
        if self.module.has_errors:
            self._set_error(0)
            return False
        return True
    
    def _check_module_function_names(self) -> bool:
        if not self.answer_module.function_name in self.module.module_functions:
            self._set_error(1)
            return False
        return True
    
    def _check_module_args_name(self) -> bool:
        function_name = self.answer_module.function_name
        if self.module.get_function_args(function_name) != self.answer_module.get_function_args(function_name):
            self._set_error(2)
            return False
        return True
    
    def _check_function_consistency(self, kwargs) -> bool:
        function_name = self.answer_module.function_name
        user_return = self.module.run_function(function_name, kwargs)
        if self.module.has_errors and self.module.error_code == 5:
            self._set_error(5, f'{user_return}')
            return False
        return True
    
    def _compare_function_returns(self, kwargs) -> bool:
        function_name = self.answer_module.function_name
        user_return = self.module.run_function(function_name, kwargs)
        answer_return = self.answer_module.run_function(function_name, kwargs)
        if answer_return != user_return:
            resultado_obtido_txt = f'Resultado obtido para params = {kwargs} > {user_return}'
            resultado_esperado_txt = f'Resultado esperado para params = {kwargs} > {answer_return}'
            self._set_error(3, f'{resultado_obtido_txt}\n{resultado_esperado_txt}')
            return False
        return True


    def validate(self) -> bool:
        self.module.load()
        self.answer_module.load()

        success = self._check_module_consistency()
        success = success and self._check_module_function_names()
        success = success and self._check_module_args_name()

        for test_params in  self.answer_module.testing_params:
            success = success and self._check_function_consistency(test_params)
            if not success: break
            success = success and self._compare_function_returns(test_params)
            if not success: break
            
        return success


if __name__ == '__main__':

    folder_path = 'desafios_de_funcao/sequencia_fibonacci'
    script_path = f'{folder_path}/tentativas/tentativa01.py'
    answer_path = f'{folder_path}/resposta.py'

    self = ScriptFunctionValidation(script_path, answer_path)
    self.validate()


