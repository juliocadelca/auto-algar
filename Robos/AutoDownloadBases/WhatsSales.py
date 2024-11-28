import pyautogui as py
from datetime import datetime
import os


# Obtém a data e hora atuais
data_atual = datetime.now()

# Extrai o dia, mês e ano
dia_atual = data_atual.day
mes_atual = data_atual.month
ano_atual = data_atual.year

# Converte para string
dia_atual_str = str(dia_atual)
mes_atual_str = str(mes_atual)
ano_atual_str = str(ano_atual)

# Criar uma lista de horas de 9:00 a 9:59
horas = [f"9:{str(minuto).zfill(2)}" for minuto in range(60)]
listanovehoras = horas

# Pega a hora atual
hora_atual = data_atual.strftime("%H:%M")

# Converte para string
hora_atual_str = str(hora_atual)


def ler_mes_anterior(): # Função para ler o mês anterior de um arquivo
    if os.path.exists("mes_anterior.txt"):
        with open("mes_anterior.txt", "r") as file:
            return int(file.read().strip())
    return None  # Retorna None se o arquivo não existir

def salvar_mes_atual(mes): # Função para salvar o mês atual em um arquivo
    with open("mes_anterior.txt", "w") as file:
        file.write(str(mes))

def Aguarde_a_Imagem(image):
    while True:
        try:
            location = py.locateOnScreen(image)  # Tenta localizar a imagem na tela
            if location is not None:  # Se a imagem foi encontrada, retorna a localização
                return location
            
        except py.ImageNotFoundException: # Se a imagem não for encontrada, apenas continue o loop
            
            py.sleep(1)  # Aguarda 1 segundo antes de tentar novamente

image_path = r'C:\Users\juliopc\Desktop\Robos\AutoDownloadBases\SalvarComo.png'  # Altere para o caminho correto da sua imagem
ManualBoletim = r"https://docs.google.com/document/d/1x09s2GnO6r7hODoH6tZRA9zlzfaT0F_v/edit#heading=h.gjdgxs"
lista = [1,2,3,4,5,6,7,8,9]

def WhatsSales():
    py.sleep(10)
    py.hotkey('ctrl', 'w')
    py.click(x=199, y=56) 
    py.typewrite(ManualBoletim)
    py.press('enter'), py.sleep(3)
    py.click(x=136, y=483), py.sleep(1) # Clicando na posição do whatssales
    py.click(x=709, y=282), py.click(x=755, y=303), py.sleep(15) # Clicando no link do relatório
    py.click(x=1746, y=242), py.sleep(1) # Clicar no filtro
    py.click(x=1725, y=378), py.sleep(1) # Clica em Periodo de tempo 
    py.click(x=1412, y=432), py.sleep(1) # Clica em Personalizar
    py.click(x=1413, y=468) # Clicar no campo para digitar a data atual
    py.typewrite(f"{dia_atual_str}/{mes_atual_str}/{ano_atual_str}") # Digitar data atual (Diário)
    py.click(x=1440, y=525)
    py.typewrite(f"{dia_atual_str}/{mes_atual_str}/{ano_atual_str}")
    py.click(x=1618, y=565), py.sleep(5)
    py.click(x=1870, y=248), py.sleep(1) # Clicando na setinha de config
    py.click(x=1812, y=341), py.sleep(2) # Clicando em Exportar
    py.click(x=959, y=523) # Clicando nas opções corretas de download
    py.click(x=818, y=667), py.sleep(1)
    py.click(x=781, y=742), py.sleep(1)
    py.click(x=1197, y=744), py.sleep(1)
    Aguarde_a_Imagem(image_path)
    for num in lista:
        if dia_atual and mes_atual == num: # Selecionando pasta de destino - Criar condição para mes com '0'
            caminho = rf"G:\CSC\Atendimento\Algar\Planejamento\01.BOLETIM\BASES\WHATSSALES\0{mes_atual_str}-{ano_atual_str}-sales\0{dia_atual_str}-0{mes_atual_str}-{ano_atual_str}-sales"
        elif dia_atual == num:
            caminho = rf"G:\CSC\Atendimento\Algar\Planejamento\01.BOLETIM\BASES\WHATSSALES\{mes_atual_str}-{ano_atual_str}-sales\0{dia_atual_str}-{mes_atual_str}-{ano_atual_str}-sales"
        elif mes_atual == num:
            caminho = rf"G:\CSC\Atendimento\Algar\Planejamento\01.BOLETIM\BASES\WHATSSALES\0{mes_atual_str}-{ano_atual_str}-sales\{dia_atual_str}-0{mes_atual_str}-{ano_atual_str}-sales"
        else:
            caminho = rf"G:\CSC\Atendimento\Algar\Planejamento\01.BOLETIM\BASES\WHATSSALES\{mes_atual_str}-{ano_atual_str}-sales\{dia_atual_str}-{mes_atual_str}-{ano_atual_str}-sales"
    py.typewrite(caminho)
    py.sleep(1)
    for hora in listanovehoras:
        if hora == hora_atual_str: # Salavando em diferentes horários
            py.press('enter')
            break
        else:
            py.press('enter'), py.sleep(2), py.press('tab'), py.sleep(1), py.press('enter')
            break

WhatsSales()