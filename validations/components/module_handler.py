import importlib
import inspect
import types
import typing

from .script_handler import Script

MODULE_ERROR_TYPES = {
    0: 'Módulo crashou. Erro ao importá-lo',
    1: 'Erro ao importar o módulo',
    2: 'Nenhuma função encontrada no módulo',
    3: 'Mais de uma função encontrada no módulo',
    4: 'Erro não identificado',
    5: 'Erro ao rodar a funcao',
}


class Modules:
    has_errors: bool = False
    module: typing.Optional[types.ModuleType] = None
    module_functions: typing.Optional[list] = None
    function_name: str = ''
    testing_params: dict = {}
    script: typing.Optional[Script] = None
    global_error: str = ""
    error_code: int = -1

    def __init__(self, module_path: str) -> None:
        self.module_path = module_path

    def _set_error(self, error_code: int, exception_text: str = ''):
        self.error_code = error_code
        self.global_error = MODULE_ERROR_TYPES[error_code]
        self.has_errors = True
    
    def _check_module_consistency(self):
        self.script = Script(self.module_path)
        self.script.run_script()
        if self.script.has_errors:
            self._set_error(0)
    
    def _import_module(self):
        try:
            self.module = None
            self.module = importlib.import_module(self.module_path.replace('.py', '').replace('/', '.'))
            self.module = importlib.reload(self.module)
        except Exception as e:
            self._set_error(1)
    
    def _import_module_function(self):
        self.module_functions = [func for func in dir(self.module) if ((not func.startswith('__')) 
                                                                        and callable(getattr(self.module, func)))]
        if len(self.module_functions) == 0:
            self._set_error(2)

        else:
            self.function_name = self.module_functions[-1]
            if 'testing_params' in dir(self.module):
                self.testing_params = getattr(self.module, 'testing_params')

    def _reset_errors(self):
        self.error_code = -1
        self.global_error = ''
        self.has_errors = False
    
    def run_function(self, function_name, kwargs):
        try:
            return getattr(self.module, function_name)(**kwargs)
        except Exception as e:
            self._set_error(5)
            return e
    
    def get_function_args(self, function_name):
        return list(inspect.signature(getattr(self.module, function_name)).parameters.keys())

    def load(self):
        try:
            self.has_errors = False
            self._check_module_consistency()
            if not self.has_errors: self._import_module()
            if not self.has_errors: self._import_module_function()
            if not self.has_errors: self._reset_errors()
        except Exception as e:
            self._set_error(4)



