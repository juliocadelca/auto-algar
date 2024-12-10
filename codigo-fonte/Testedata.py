from datetime import datetime, timedelta

# Obtém a data e hora atuais
data_atual = datetime.now()

# Extrai o dia, mês e ano
dia_atual = data_atual.day
mes_atual = data_atual.month
ano_atual = data_atual.year

# Converte para string
"""dia_atual_str = str(dia_atual)
mes_atual_str = str(mes_atual)
ano_atual_str = str(ano_atual)"""

# Exibe os resultados como strings
"""print(f'Dia: {dia_atual_str}')
print(f'Mês: {mes_atual_str}')
print(f'Ano: {ano_atual_str}')"""

"""data_formatada = f"{dia_atual_str}/{mes_atual_str}/{ano_atual_str}"
print(f'Data formatada: {data_formatada}')"""




# Obtém a data e hora atuais
data_atual = datetime.now()

# Extrai a hora e os minutos
hora_atual = data_atual.strftime("%H:%M")  # Formato de 24 horas
# hora_atual = data_atual.strftime("%I:%M %p")  # Formato de 12 horas com AM/PM
# Converter para string
hora_atual_str = str(hora_atual)

# Exibe a hora atual
"""print(f'Hora atual: {hora_atual}')
print(data_atual)
print(hora_atual_str)"""
"""hora_um_a_mais = hora_atual + timedelta(hours=1)
print(hora_um_a_mais)"""
dia_formatado = str(dia_atual).zfill(2)  # Formata o dia com zero à esquerda
mes_formatado = str(mes_atual).zfill(2)  # Formata o mês com zero à esquerda
print(dia_formatado)
print(mes_formatado)