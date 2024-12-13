import keyboard as Key
import sys
import time

# Função para encerrar o programa
def encerrar_programa():
    print("Encerrando o programa...")
    exit()

# Configurar o atalho de teclado global (Ctrl + F1)
Key.add_hotkey('ctrl+f1', encerrar_programa)

# Exemplo de loop principal
try:
    print("Programa em execução. Pressione Ctrl + F1 para encerrar.")
    while True:
        time.sleep(1)  # Adiciona um pequeno atraso para evitar uso excessivo da CPU
except KeyboardInterrupt:
    print("Programa interrompido.")