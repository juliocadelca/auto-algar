from datetime import datetime, timedelta
import pyautogui as py

data_atual = datetime.now() # Obtém a data e hora atuais
hora_atual = data_atual.strftime("%H:%M") # Pega a hora atual
hora_atual_str = str(hora_atual)

BotãoSim = r"C:\Users\juliopc\Desktop\Robos\AutoDownloadBases\BotãoSim.png"

import pyautogui
import time
from datetime import datetime, timedelta

def localizar_e_clicar(image, tempo_espera=5):
    tempo = 0
    while tempo < tempo_espera:
        try:
            location = py.locateOnScreen(image)  # Tenta localizar a imagem na tela
            if location is not None:  # Se a imagem foi encontrada, retorna a localização
                return py.click(location)
        except py.ImageNotFoundException: # Se a imagem não for encontrada, apenas continue o loop
            py.sleep(1) # Aguarda 1 segundo antes de tentar novamente
            tempo += 1

### FUNCIONANDO...
localizar_e_clicar(BotãoSim, 10)

        
