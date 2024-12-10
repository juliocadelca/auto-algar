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

# Variável para armazenar o mês anterior
mes_anterior = None

def ler_mes_anterior(): # Função para ler o mês anterior de um arquivo
    if os.path.exists("mes_anterior.txt"):
        with open("mes_anterior.txt", "r") as file:
            return int(file.read().strip())
    return None  # Retorna None se o arquivo não existir

# Lê o mês anterior do arquivo
mes_anterior = ler_mes_anterior()

def salvar_mes_atual(mes): # Função para salvar o mês atual em um arquivo
    with open("mes_anterior.txt", "w") as file:
        file.write(str(mes))

def BacklogSales():

    py.sleep(4)
    py.click(x=199, y=56) # Entrando no Manual do Boletim
    py.typewrite(r'https://docs.google.com/document/d/1x09s2GnO6r7hODoH6tZRA9zlzfaT0F_v/edit#heading=h.gjdgxs')
    py.press('enter'), py.sleep(3)
    py.click(x=149, y=515), py.sleep(1) # Clicando na posição BacklogSales
    py.click(x=709, y=282) # Clicando no link do relatório
    py.click(x=755, y=303), py.sleep(10)
    py.click(x=1870, y=248), py.sleep(1) # Clicando na setinha de config
    py.click(x=1812, y=341), py.sleep(1) # Clicando em Exportar
    py.click(x=959, y=523), py.sleep(1) # Clicando nas opções corretas de download
    py.click(x=818, y=667), py.sleep(1)
    py.click(x=781, y=742), py.sleep(1)
    py.click(x=1197, y=744), py.sleep(20)
    lista = [1,2,3,4,5,6,7,8,9]
    if mes_atual_str in lista: # Selecionando pasta de destino e salvando arquivo corretamente
        caminho = (rf"G:\CSC\Atendimento\Algar\Planejamento\01.BOLETIM\BASES\BKO\0{mes_atual_str}_{ano_atual_str}-bkbklog")
    else:
        caminho = (rf"G:\CSC\Atendimento\Algar\Planejamento\01.BOLETIM\BASES\BKO\{mes_atual_str}_{ano_atual_str}-bkbklog")
    py.typewrite(caminho)
    if mes_anterior is None or mes_atual != mes_anterior: # Verifica se o mês atual é diferente do mês anterior
        py.press('enter')
    else:
        py.press('enter'), py.sleep(3), py.press('tab'), py.sleep(1), py.press('enter')
    salvar_mes_atual(mes_atual) # Salva o mês atual para a próxima execução
BacklogSales()