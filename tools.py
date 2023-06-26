import time

def generate_file_input_name(directory_path='user_input/'):
    return f'{directory_path}file_{int(time.time()*1000)}.py'

def generate_file_ouput_name(directory_path='user_output/'):
    return f'{directory_path}file_{int(time.time()*1000)}.py'