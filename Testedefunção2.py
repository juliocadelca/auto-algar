import datetime
import pyautogui
# SOLUÇÃO PARA AUTOMATIZAR BASES LOOKER
# Cria um dicionário que associa as 3 primeiras letras dos meses ao número do mês
meses = {
    1: 'jan',
    2: 'fev',
    3: 'mar',
    4: 'abr',
    5: 'mai',
    6: 'jun',
    7: 'jul',
    8: 'ago',
    9: 'set',
    10: 'out',
    11: 'nov',
    12: 'dez'
}

def mes_atual_abreviado():
    # Obtém o mês atual
    mes_atual = datetime.datetime.now().month
    # Retorna a abreviação do mês atual
    return meses[mes_atual]
abreviacao = mes_atual_abreviado()

# Usa o pyautogui para digitar a abreviação do mês atual
print(abreviacao)