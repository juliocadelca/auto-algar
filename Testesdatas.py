from datetime import datetime, timedelta

# Obtém a hora atual
hora_atual = datetime.now()

# Adiciona 1 hora
nova_hora = hora_atual + timedelta(hours=1)

# Formata a nova hora como string no formato HH:MM
nova_hora_str = nova_hora.strftime("%H:%M")

# Exibe a nova hora
print(f'Hora atual: {hora_atual.strftime("%H:%M")}')
print(f'Nova hora (com 1 hora a mais): {nova_hora_str}')