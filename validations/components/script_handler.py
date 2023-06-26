import subprocess

TIME_OUT = 3

class Script:

    has_errors: bool = False
    was_script_tested: bool = False
    error_output: str = "Script não rodado"
    success_output: str = "Script não rodado"
    global_error: str = "Script não rodado"


    def __init__(self, script_path: str) -> None:
        self.script_path = script_path

    def change_path(self, script_path: str) -> None:
        self.script_path = script_path

    def run_script(self) -> None:

        try:
            script_output = subprocess.run(['python3', self.script_path], capture_output=True, text=True, timeout=TIME_OUT)

            if not script_output.returncode == 0:
                self.has_errors = True
            else:
                self.has_errors = False

            self.error_output = script_output.stderr
            self.success_output = script_output.stdout
            self.was_script_tested = True
            self.global_error = ''

        except Exception as e:
            print(f"Global error: {e}")
            self.global_error = str(e)




if __name__ == '__main__':



    script = Script('example_script.py')
    script.run_script()

    script.success_output.split('\n')




