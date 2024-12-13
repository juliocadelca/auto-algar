import subprocess
import time

def kill_process(process_name):
    try:
        # Executa o comando taskkill
        subprocess.run(['taskkill', '/IM', process_name, '/F'], check=True)
        print(f'O processo {process_name} foi encerrado com sucesso.')
        time.sleep(2)
    except subprocess.CalledProcessError as e:
        print(f'Erro ao tentar encerrar o processo {process_name}: {e}')
        time.sleep(2)

if __name__ == "__main__":
    process_name = 'MAIN.exe'  # Nome do processo a ser encerrado
    kill_process(process_name)