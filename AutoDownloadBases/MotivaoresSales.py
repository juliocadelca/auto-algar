import pyautogui as py
from datetime import datetime

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

def MotivadoresSales():

    py.sleep(4)
    py.click(x=199, y=56) # Entrando no Manual do Boletim
    py.typewrite(r'https://docs.google.com/document/d/1x09s2GnO6r7hODoH6tZRA9zlzfaT0F_v/edit#heading=h.gjdgxs')
    py.press('enter'), py.sleep(3)
    py.click(x=127, y=546), py.sleep(1) # Clicando na posição MotivadoresSales
    py.click(x=709, y=282) # Clicando no link do relatório
    py.click(x=755, y=303), py.sleep(15)
    py.click(x=1870, y=248), py.sleep(1) # Clicando na setinha de config
    py.click(x=1812, y=341), py.sleep(2) # Clicando em Exportar
    py.click(x=959, y=523) # Clicando nas opções corretas de download
    py.click(x=818, y=667), py.sleep(1)
    py.click(x=781, y=742), py.sleep(1)
    py.click(x=1197, y=744), py.sleep(15)
    lista = [1,2,3,4,5,6,7,8,9]
    if dia_atual and mes_atual in lista: # Selecionando pasta de destino - Criar condição para mes com '0'
        py.typewrite(rf"G:\CSC\Atendimento\Algar\Planejamento\01.BOLETIM\BASES\MOTIVADOR\0{dia_atual_str}-0{mes_atual_str}-{ano_atual_str}-motivador")
    elif dia_atual in lista:
        py.typewrite(rf"G:\CSC\Atendimento\Algar\Planejamento\01.BOLETIM\BASES\MOTIVADOR\0{dia_atual_str}-{mes_atual_str}-{ano_atual_str}-motivador")
    elif mes_atual in lista:
        py.typewrite(rf"G:\CSC\Atendimento\Algar\Planejamento\01.BOLETIM\BASES\MOTIVADOR\{dia_atual_str}-0{mes_atual_str}-{ano_atual_str}-motivador")
    else:
        py.typewrite(rf"G:\CSC\Atendimento\Algar\Planejamento\01.BOLETIM\BASES\MOTIVADOR\{dia_atual_str}-{mes_atual_str}-{ano_atual_str}-motivador")
    py.sleep(1)
    if hora_atual in listanovehoras: # Salavando em diferentes horários
        py.press('enter'), py.sleep(2), py.press('tab'), py.sleep(1), py.press('enter')
    else:
        py.press('enter')
MotivadoresSales()