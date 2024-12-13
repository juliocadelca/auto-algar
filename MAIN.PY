import pyautogui as py
import pymsgbox as msg
from datetime import datetime, timedelta
import os

### VARIÁVEIS DE DATETIME ###
data_atual = datetime.now() # Obtém a data e hora atuais
dia_atual = data_atual.day # Extrai o dia, mês e ano
mes_atual = data_atual.month
ano_atual = data_atual.year
#---------------------------------------------------------------------------------------------------------------------------------------------------------
dia_atual_str = str(dia_atual) # Converte para string
mes_atual_str = str(mes_atual)
ano_atual_str = str(ano_atual)

dia_formatado = str(dia_atual_str).zfill(2)  # Formata o dia com zero à esquerda
mes_formatado = str(mes_atual_str).zfill(2)  # Formata o mês com zero à esquerda
#---------------------------------------------------------------------------------------------------------------------------------------------------------

### VARIÁVEIS DE LINKS E CAMINHOS ###

class Caminhos:
    def __init__(self):

        base_path = os.path.expanduser(r"~/Desktop/Robos/AutoDownloadBases/img") ### Usando os.path.expanduser para garantir que funcione em qualquer máquina
        
        self.manual_boletim = r"https://docs.google.com/document/d/1x09s2GnO6r7hODoH6tZRA9zlzfaT0F_v/edit#heading=h.gjdgxs"
        self.setinha_exportar = os.path.join(base_path, "SetinhaExportar.png")
        self.login_sales_image = os.path.join(base_path, "LoginSalesIMG.png")
        self.backlog_image = os.path.join(base_path, "BackLogSalesIMG.png")
        self.whats_sales_image = os.path.join(base_path, "WhatsSalesIMG.png")
        self.Motivadores_image = os.path.join(base_path, "MotivadoresSalesIMG.png")
        self.chatprov_image = os.path.join(base_path, "ChatProvIMG.png")
        self.filtrodata_asc = os.path.join(base_path, "FiltrarDataASC.png")
        self.fundo_sales = os.path.join(base_path, "FundoSales.png")
        self.hora_asc = os.path.join(base_path, "HoraAsc.png")
        self.detalhes_apenas = os.path.join(base_path, "DetalhesApenas.png")
        self.formato_csv = os.path.join(base_path, "FormatoCSV.png")
        self.formato_antigo = os.path.join(base_path, "FormatoExcelAntigo.png")
        self.botao_exportar = os.path.join(base_path, "BotãoExportar.png")
        self.exportar = os.path.join(base_path, "Exportar.png")
        self.image_path = os.path.join(base_path, "SalvarComo.png")
        self.image_filter = os.path.join(base_path, "FiltroAguarde.png")
        self.image_data_e_id = os.path.join(base_path, "CodSeg-EHC.png")
        self.image_sem_titulo = os.path.join(base_path, "SemTitulo.png")
        self.periodo_integral = os.path.join(base_path, "PeríodoIntegral.png")
        self.personalizar = os.path.join(base_path, "Personalizar.png")
        self.botao_sim = os.path.join(base_path, "BotãoSim.png")
        self.filtro_asc = os.path.join(base_path, "FiltrarASC.png")
        self.filtro_sales = os.path.join(base_path, "Filtro.png")
        self.servico_selecione = os.path.join(base_path, "ServiçoSelecione.png")
        self.filtro_avancado = os.path.join(base_path, "FiltroAvançadoASC.png")
        self.exportar_asc = os.path.join(base_path, "ExportarASC.png")
        self.exportar_whats_asc = os.path.join(base_path, "ExportarWhatsASC.png")
        self.manual_boletim_img = os.path.join(base_path, "ManualBoletim.png")
        self.login_sales_img = os.path.join(base_path, "LoginSales.png")
        self.login_asc_img = os.path.join(base_path, "LoginAsc.png")
        self.whats_sales_img = os.path.join(base_path, "WhatsSales.png")
        self.backlog_img = os.path.join(base_path, "BackLog.png")
        self.motivadores_img = os.path.join(base_path, "Motivador.png")
        self.whats_asc_img = os.path.join(base_path, "WhatsAsc.png")
        self.chat_mensal_img = os.path.join(base_path, "ChatMensal.png")
        self.link = os.path.join(base_path, "link.png")
        self.link_dois = os.path.join(base_path, "link2.png")
        self.https = os.path.join(base_path, "https.png")
        self.data_inicio_ehc = os.path.join(base_path, "DataInicioEHC.png")
        self.caixa_flegada = os.path.join(base_path, "CaixaFlegada.png")
        self.caixa_nao_flegada = os.path.join(base_path, "CaixaNãoFlegada.png")
        self.vazio = os.path.join(base_path, "Vazio.png")
        self.para_mover_o_mouse_ehc = os.path.join(base_path, "ParaMoverOMouse.png")
        self.tres_pontinhos = os.path.join(base_path, "TresPontinhos.png")
        self.tres_pontinhos_dois = os.path.join(base_path, "TresPontinhosDois.png")
        self.exportar_lokker = os.path.join(base_path, "ExportarLooker.png")
        self.aguarde_export_como = os.path.join(base_path, "ImagemExpotLooker.png")
        self.data_entrada = os.path.join(base_path, "DataEntradaLooker.png")
        self.caixa_flegada_live_chat = os.path.join(base_path, "CaixaFlegadaLiveChat.png")
        self.caixa_nao_flegada_live_chat = os.path.join(base_path, "CaixaNãoFlegadaLiveChat.png")
        self.aguarde_live_chat = os.path.join(base_path, "AguardeLiveChat.png")
        self.aguarde_chat_assinc = os.path.join(base_path, "AguardeChatAssinc.png")
        self.ano_mes = os.path.join(base_path, "Ano-Mes.png")
        self.tres_pontinhos_tres = os.path.join(base_path, "TresPontinhosTres.png")
        self.chrome = os.path.join(base_path, "Chrome.png")
        self.redefinir_zoom = os.path.join(base_path, "RedefinirZoom.png")
#----------------------------------------------------------------------------------------------------------------------------------------------------------

# Listas e Dicionários
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

lista = [1,2,3,4,5,6,7,8,9]
ListaDeErros = []
#---------------------------------------------------------------------------------------------------------------------------------------------------------
# Funções de horas incrementos
hora_atual = data_atual.strftime("%H:%M") # Pega a hora atual
hora_atual_str = str(hora_atual) # Converte para string
hora_atual_maisum = datetime.now() # Obtém a hora atual
nova_hora = hora_atual_maisum + timedelta(hours=1) # Adiciona 1 hora
nova_hora_str = nova_hora.strftime("%H:%M") # Formata a nova hora como string no formato HH:MM

#---------------------------------------------------------------------------------------------------------------------------------------------------------

# Funções de suporte
class SaidaException(Exception):
    pass

def mes_atual_abreviado():
    # Obtém o mês atual
    mes_atual = data_atual.month
    # Retorna a abreviação do mês atual
    return meses[mes_atual]

def ler_mes_anterior(): # Função para ler o mês anterior de um arquivo
    if os.path.exists("mes_anterior.txt"):
        with open("mes_anterior.txt", "r") as file:
            return int(file.read().strip())
    return None  # Retorna None se o arquivo não existir

def salvar_mes_atual(mes): # Função para salvar o mês atual em um arquivo
    with open("mes_anterior.txt", "w") as file:
        file.write(str(mes))

def Aguarde_a_Imagem(image, tempo_espera=50):
    tempo = 0
    tentar = 0
    ultima_palavra = image.split("\\")[-1]
    
    while tempo <= tempo_espera:
        try:
            location = py.locateOnScreen(image)  # Tenta localizar a imagem na tela
            if location is not None:  # Se a imagem foi encontrada, retorna a localização
                return location
        except py.ImageNotFoundException:  # Se a imagem não for encontrada, apenas continue o loop
            if tempo == tempo_espera:
                mensagemErro = msg.alert(f"Ops, está demorando muito...'{ultima_palavra}' ", title="Erro", button="Tentar Novamente")
                print(mensagemErro)
                if mensagemErro == "Tentar Novamente":
                    tempo_espera = 30
                    tempo = 0
                    tentar += 1
                    if tentar == 5:
                        msg.alert(text=f"O robô não conseguiu localizar o item: {ultima_palavra}\nContate o adm do sistema. \nIndo para próxima base.",
                                title="ERRO? AH NÃO", button="OK")
                        raise SaidaException  # Lança a exceção
            py.sleep(1)  # Aguarda 1 segundo antes de tentar novamente
            tempo += 1

def Aguarde_imagem_sumir(image, tempo_espera=50):
    tentar = 0
    ultima_palavra = image.split("\\")[-1]
    tempo = 0  # Contador de tentativas
    try:
        while tempo < tempo_espera:
            location = py.locateOnScreen(image)  # Tenta localizar a imagem na tela
            if location is None:  # Se a imagem não foi encontrada
                return  # Sai da função sem erro
    except py.ImageNotFoundException:
            if tempo == tempo_espera:
                mensagemErro = msg.alert(f"Ops, está demorando muito...'{ultima_palavra}' ", title="Erro", button="Tentar Novamente")
                print(mensagemErro)
                if mensagemErro == "Tentar Novamente":
                    tempo_espera = 10
                    tempo = 0
                    tentar += 1
                    if tentar == 5:
                        msg.alert(text=f"A pagina está presa no o item: {ultima_palavra}\nContate o adm do sistema. \nIndo para próxima base.",
                                title="ERRO? AH NÃO", button="OK")
                        raise SaidaException  # Lança a exceção
            py.sleep(1)  # Aguarda 1 segundo antes de tentar novamente
            tempo += 1

def localizar_e_clicarRápido(image, tempo_espera=3):

    tempo = 0
    tentar = 0
    ultima_palavra = image.split("\\")[-1]
    while tempo <= tempo_espera:
        try:
            location = py.locateOnScreen(image)  # Tenta localizar a imagem na tela
            if location is not None:  # Se a imagem foi encontrada, retorna a localização e clica
                return py.click(location)
        except py.ImageNotFoundException: # Se a imagem não for encontrada, apenas continue o loop
            if tempo == tempo_espera:
                tempo_espera = 2
                tempo = 0
                tentar += 1
                if tentar == 5:
                    break
            tempo += 1

def AbrirChromeAberto():
    
    py.keyDown('win'), py.press('tab'), py.keyUp('win')
    localizar_e_clicar(rota.chrome)
    py.hotkey('ctrl', 't'), py.sleep(3) # Abrir uma nova aba

def localizar_e_clicar(image, tempo_espera=30):
    tempo = 0
    tentar = 0
    ultima_palavra = image.split("\\")[-1]
    while tempo <= tempo_espera:
        try:
            location = py.locateOnScreen(image)  # Tenta localizar a imagem na tela
            if location is not None:  # Se a imagem foi encontrada, retorna a localização e clica
                return py.click(location)
        except py.ImageNotFoundException: # Se a imagem não for encontrada, apenas continue o loop
            if tempo == tempo_espera:
                mensagemErro = msg.alert(f"Hmm, não encontrei o item: '{ultima_palavra}' ", title="Erro", button="Tente Novamente")
                print(mensagemErro)
                if mensagemErro == "Tente Novamente":
                    tempo_espera = 10
                    tempo = 0
                    tentar += 1
                    if tentar == 5:
                        msg.alert(text=f"Eu não consegui localizar o item: {ultima_palavra}" , title="AH NÃO", button="OK")
                        break
            tempo += 1

### VARIÁVEIS DE CONTROLE ###
rota = Caminhos()
salvar_mes_atual(mes_atual) # Salva o mês atual para a próxima execução
abreviacao = mes_atual_abreviado()
mes_anterior = ler_mes_anterior() # Lê o mês anterior do arquivo
#---------------------------------------------------------------------------------------------------------------------------------------------------------



# Iniciando os downloads

def LoginSales():

    AbrirChromeAberto()

    '''py.sleep(2)
    py.press('win'), py.sleep(0.5)
    py.typewrite('chrome'), py.sleep(0.5)
    py.press('enter')'''

    py.sleep(3)
    py.click(x=199, y=56) 
    py.typewrite(rf"https://grupoboticario.lightning.force.com/one/one.app#eyJjb21wb25lbnREZWYiOiJvbW5pOnN1cGVydmlzb3JQYW5lbCIsImF0dHJpYnV0ZXMiOnt9LCJzdGF0ZSI6e319")
    py.press('enter') # Entrando no SalesForce

    localizar_e_clicar(rota.login_sales_image), py.sleep(5) # Clicando na posição Login Sales
    localizar_e_clicar(rota.setinha_exportar) # Clicando na setinha de config
    localizar_e_clicar(rota.exportar) # Clicando em Exportar
    localizar_e_clicar(rota.detalhes_apenas) # Clicando nas opções corretas de download
    localizar_e_clicar(rota.formato_antigo)
    localizar_e_clicar(rota.formato_csv)
    localizar_e_clicar(rota.botao_exportar)

    try:
        Aguarde_a_Imagem(rota.image_path)
    except SaidaException:
        return
    
    caminho = (rf"G:\CSC\Atendimento\Algar\Planejamento\01.BOLETIM\BASES\AGENTESALES\{ano_atual_str}\{mes_formatado}-{ano_atual_str}-agtsales")
    py.typewrite(caminho), py.sleep(1)

    if mes_atual != mes_anterior: # Verifica se o mês atual é diferente do mês anterior
        py.press('enter'), py.sleep(1)
    else:
        py.press('enter')
        localizar_e_clicar(rota.botao_sim), py.sleep(1)

def LoginAsc():
    
    py.hotkey("ctrl", "w")
    py.click(x=199, y=56) 
    py.typewrite(rf"https://sac-boticario.ascbrazil.com.br/relatorio-agentes/relatorio-login")# Entrando no LoginASC
    py.press('enter') 
    localizar_e_clicar(rota.filtrodata_asc), py.sleep(1) # Clicar no filtro de data e selecionar a data 01 do mês atual (NÃO TEVE JEITO DE COLOCAR IMAGEM, POR ISSO ESTÁ COMO X E Y)
    py.typewrite(f"01/{mes_atual_str}/{ano_atual_str}")
    py.press('enter')
    localizar_e_clicar(rota.filtro_asc) # Clicando no botão filtrar
    localizar_e_clicar(rota.exportar_asc) # Clicando no botão exportar

    try:
        Aguarde_a_Imagem(rota.image_path)
    except SaidaException:
        return
    
    caminho = (rf"G:\CSC\Atendimento\Algar\Planejamento\01.BOLETIM\BASES\AGENTESASC\{ano_atual_str}\{mes_formatado}-{ano_atual_str}-agtasc")
    py.typewrite(caminho)

    if mes_atual != mes_anterior: # Verifica se o mês atual é diferente do mês anterior
        py.press('enter'), py.sleep(1)
    else:
        py.press('enter')
        localizar_e_clicar(rota.botao_sim), py.sleep(1)

def WhatsSales():

    py.hotkey("ctrl", "w")
    localizar_e_clicar(rota.whats_sales_image), py.sleep(1) # Clicando na posição WhatsSales
    localizar_e_clicar(rota.filtro_sales), py.sleep(0.5) # Clicar no filtro
    localizar_e_clicar(rota.periodo_integral), py.sleep(0.5) # Clica em Periodo integral
    localizar_e_clicar(rota.personalizar), py.sleep(1) # Clica em Personalizar
    py.press('tab') # Entrar no campo para digitar a data atual
    py.typewrite(f"{dia_atual_str}/{mes_atual_str}/{ano_atual_str}") # Digitar data atual (Diário)
    py.press('tab'), py.sleep(0.5), py.press('tab')
    py.typewrite(f"{dia_atual_str}/{mes_atual_str}/{ano_atual_str}")
    py.press('tab'), py.sleep(0.5), py.press('tab'), py.sleep(0.5), py.press('tab'), py.press('enter'), py.sleep(3)
    localizar_e_clicar(rota.setinha_exportar), py.sleep(1) # Clicando na setinha de config
    localizar_e_clicar(rota.exportar), py.sleep(2) # Clicando em Exportar
    localizar_e_clicar(rota.detalhes_apenas) # Clicando nas opções corretas de download
    localizar_e_clicar(rota.formato_antigo), py.sleep(0.5)
    localizar_e_clicar(rota.formato_csv), py.sleep(0.5)
    localizar_e_clicar(rota.botao_exportar), py.sleep(0.5)

    try:
        Aguarde_a_Imagem(rota.image_path)
    except SaidaException:
        return
    
    caminho = rf"G:\CSC\Atendimento\Algar\Planejamento\01.BOLETIM\BASES\WHATSSALES\{mes_formatado}-{ano_atual_str}-sales\{dia_formatado}-{mes_formatado}-{ano_atual_str}-sales"
    py.typewrite(caminho), py.sleep(1)

    if '09:00' <= hora_atual_str < '10:00':  # Verifica se a hora está entre 9:00 e 9:59
        py.press('enter'), py.sleep(1)
    else:
        py.press('enter')
        localizar_e_clicar(rota.botao_sim), py.sleep(1)  # Salavando em diferentes horários clicando no botão sim
  
def BacklogSales():
    
    py.hotkey("ctrl", "w")
    localizar_e_clicar(rota.backlog_image), py.sleep(1) # Clicando na posição BackLog Sales
    localizar_e_clicar(rota.setinha_exportar), py.sleep(1) # Clicando na setinha de config
    localizar_e_clicar(rota.exportar), py.sleep(2) # Clicando em Exportar
    localizar_e_clicar(rota.detalhes_apenas) # Clicando nas opções corretas de download
    localizar_e_clicar(rota.formato_antigo), py.sleep(0.5)
    localizar_e_clicar(rota.formato_csv), py.sleep(0.5)
    localizar_e_clicar(rota.botao_exportar), py.sleep(0.5)

    try:
        Aguarde_a_Imagem(rota.image_path)
    except SaidaException:
        return
    
    caminho = (rf"G:\CSC\Atendimento\Algar\Planejamento\01.BOLETIM\BASES\BKO\{mes_formatado}_{ano_atual_str}-bkbklog")
    py.typewrite(caminho)

    if mes_atual != mes_anterior: # Verifica se o mês atual é diferente do mês anterior
        py.press('enter'), py.sleep(1)
    else:
        py.press('enter')
        localizar_e_clicar(rota.botao_sim), py.sleep(1)

def MotivadoresSales():
    
    py.hotkey("ctrl", "w")
    localizar_e_clicar(rota.Motivadores_image), py.sleep(1) # Clicando na posição Login Sales
    localizar_e_clicar(rota.setinha_exportar), py.sleep(1) # Clicando na setinha de config
    localizar_e_clicar(rota.exportar), py.sleep(2) # Clicando em Exportar
    localizar_e_clicar(rota.detalhes_apenas) # Clicando nas opções corretas de download
    localizar_e_clicar(rota.formato_antigo), py.sleep(0.5)
    localizar_e_clicar(rota.formato_csv), py.sleep(0.5)
    localizar_e_clicar(rota.botao_exportar), py.sleep(0.5)

    try:
        Aguarde_a_Imagem(rota.image_path)
    except SaidaException:
        return
    
    caminho = rf"G:\CSC\Atendimento\Algar\Planejamento\01.BOLETIM\BASES\MOTIVADOR\{dia_formatado}-{mes_formatado}-{ano_atual_str}-motivador"
    py.typewrite(caminho), py.sleep(1)

    if '09:00' <= hora_atual_str < '10:00':  # Verifica se a hora está entre 9:00 e 9:59
        py.press('enter'), py.sleep(1)
    else:
        py.press('enter')
        localizar_e_clicar(rota.botao_sim), py.sleep(1)  # Salavando em diferentes horários clicando no botão sim

def WhatsAsc():
    
    py.hotkey("ctrl", "w")
    py.click(x=199, y=56) 
    py.typewrite(rf"https://sac-boticario.ascbrazil.com.br/relatorio-atendimento/relatorio-atendimento-analitico")# Entrando no LoginASC
    py.press('enter') 
    localizar_e_clicar(rota.hora_asc), py.sleep(1) # Colcando hora atual + 1 hora na configuração
    py.typewrite(f"{nova_hora_str}"), py.sleep(1)
    localizar_e_clicar(rota.filtro_avancado), py.sleep(1) # abrindo o filtro
    localizar_e_clicar(rota.servico_selecione), py.sleep(1) # clicando no filtro de nomes

    listadenomes = ['Resolva agora VDF', 'VDF', 'VDF - Atendimento GB', 'Venda Direta - CAR VDF', 'Resolva Agora', 'Venda Direta - CAR', 'N', 'CAR - Intera']

    for nome in listadenomes: # Digitar nomes da lista para filtrar
        py.typewrite(nome)
        py.press('enter'), py.sleep(0.4)
    localizar_e_clicar(rota.filtro_asc) # Clicando em filtrar
    py.sleep(1)

    try:
        Aguarde_imagem_sumir(rota.image_filter)
    except SaidaException:
        return 
    
    py.keyDown('down'), py.keyDown('down'), py.keyDown('down'), py.keyDown('down'), py.keyDown('down')
    localizar_e_clicar(rota.exportar_whats_asc)  # Clicando em exportar
     
    try:
        Aguarde_a_Imagem(rota.image_path)
    except SaidaException:
        return
    
    caminho = rf"G:\CSC\Atendimento\Algar\Planejamento\01.BOLETIM\BASES\WHATSASC\{mes_formatado}-{ano_atual_str}-asc\{dia_formatado}-{mes_formatado}-{ano_atual_str}-asc"
    py.typewrite(caminho)

    if '09:00' <= hora_atual_str < '10:00':  # Verifica se a hora está entre 9:00 e 9:59
        py.press('enter'), py.sleep(1)
    else:
        py.press('enter')
        localizar_e_clicar(rota.botao_sim), py.sleep(1)  # Salavando em diferentes horários clicando no botão sim

def ChatMensalSales():
    
    py.hotkey("ctrl", "w")
    localizar_e_clicar(rota.chatprov_image), py.sleep(1) # Clicando na posição ChatMensalSales
    localizar_e_clicar(rota.setinha_exportar), py.sleep(1) # Clicando na setinha de config
    localizar_e_clicar(rota.exportar), py.sleep(2) # Clicando em Exportar
    localizar_e_clicar(rota.detalhes_apenas) # Clicando nas opções corretas de download
    localizar_e_clicar(rota.formato_antigo), py.sleep(0.5)
    localizar_e_clicar(rota.formato_csv), py.sleep(0.5)
    localizar_e_clicar(rota.botao_exportar), py.sleep(0.5)

    try:
        Aguarde_a_Imagem(rota.image_path)
    except SaidaException:
        return
    
    caminho = (rf"G:\CSC\Atendimento\Algar\Planejamento\01.BOLETIM\BASES\CHAT\CHAT_LOOKER\{ano_atual_str}-{mes_formatado}-prov_chat_assinc")
    py.typewrite(caminho), py.sleep(1)

    if mes_atual != mes_anterior: # Verifica se o mês atual é diferente do mês anterior
        py.press('enter'), py.sleep(1)
    else:
        py.press('enter')
        localizar_e_clicar(rota.botao_sim), py.sleep(1)

def EHCTelefone():
    py.sleep(2)
    py.hotkey("ctrl", "w")
    py.click(x=199, y=56) # Clicando na barra de pesquisa
    py.typewrite(r'https://lookerstudio.google.com/u/0/reporting/bbdcca5b-e387-4caf-ac84-e45308a0179b/page/p_hg5cs3kecd') # Digitando o endereço da base EHC
    py.press('enter')

    try:
        Aguarde_a_Imagem(rota.image_data_e_id) # Aguardando a pagina carregar por completo
    except SaidaException:
        return
    
    localizar_e_clicar(rota.data_inicio_ehc) # Clicando no data_inicio para filtrar data
    localizar_e_clicar(rota.caixa_flegada), py.press('tab'), py.sleep(1) # Clicando na caixa de selção
    py.typewrite(f"{mes_atual_str}/{ano_atual_str}")
    py.moveTo(x=1686, y=785)
    localizar_e_clicar(rota.caixa_nao_flegada) # Clicando na caixa de selção novamente para selecionar todos do mês atual
    py.sleep(8) # Aguardar o filtro carregar as informações
    localizar_e_clicar(rota.vazio), py.sleep(1) # Clicando fora para prosseguir
    py.moveTo(x=361, y=832) # Movendo o mouse para aparecer os 3 pontos
    localizar_e_clicar(rota.tres_pontinhos) # Clicando nos 3 potinhos
    localizar_e_clicar(rota.exportar_lokker)

    try:
        Aguarde_a_Imagem(rota.aguarde_export_como) # Cliando em exportar
    except SaidaException:
        return
    
    py.press('tab'), py.press('down'), py.press('tab'), py.press('space'), py.sleep(1)
    py.press('tab'), py.press('tab'), py.press('enter')

    try:
        Aguarde_a_Imagem(rota.image_path)
    except SaidaException:
        return

    caminho = (rf"G:\CSC\Atendimento\Algar\Planejamento\01.BOLETIM\BASES\ECH - VOZ\ECH_CMS_{mes_formatado}.{ano_atual_str}")
    py.typewrite(caminho), py.sleep(1) # Testar sem o sleep
    
    if mes_atual != mes_anterior: # Verifica se o mês atual é diferente do mês anterior
        py.press('enter')
    else:
        py.press('enter')
        localizar_e_clicar(rota.botao_sim)

def LiveChat():

    try:
        Aguarde_imagem_sumir(rota.image_sem_titulo)
    except SaidaException:
        return
    
    py.click(x=199, y=56) # Clicando na barra de pesquisa
    py.typewrite(r'https://lookerstudio.google.com/u/0/reporting/bbdcca5b-e387-4caf-ac84-e45308a0179b/page/p_dtaeqs9zbd') # Digitando o endereço da base LiveChat
    py.press('enter')

    try:
        Aguarde_a_Imagem(rota.aguarde_live_chat) # Aguardando a pagina carregar por completo
    except SaidaException:
        return
    
    localizar_e_clicar(rota.data_entrada) # Clicando no data_inicio para filtrar data
    localizar_e_clicar(rota.caixa_flegada_live_chat), py.press('tab'), py.sleep(1) # Clicando na caixa de selção
    py.typewrite(f"{abreviacao}. de {ano_atual_str}")
    py.moveTo(x=1686, y=785)
    localizar_e_clicar(rota.caixa_nao_flegada_live_chat) # Clicando na caixa de selção novamente para selecionar todos do mês atual
    py.sleep(8) # Aguardar o filtro carregar as informações
    localizar_e_clicar(rota.vazio), py.sleep(1) # Clicando fora para prosseguir
    py.moveTo(x=361, y=832) # Movendo o mouse para aparecer os 3 pontos
    localizar_e_clicar(rota.tres_pontinhos_dois) # Clicando nos 3 potinhos
    localizar_e_clicar(rota.exportar_lokker)

    try:
        Aguarde_a_Imagem(rota.aguarde_export_como) # Cliando em exportar
    except SaidaException:
        return
    
    py.press('tab'), py.press('down'), py.press('tab'), py.press('space'), py.sleep(1)
    py.press('tab'), py.press('tab'), py.press('enter')

    try:
        Aguarde_a_Imagem(rota.image_path)
    except SaidaException:
        return

    caminho = (rf"G:\CSC\Atendimento\Algar\Planejamento\01.BOLETIM\BASES\CHAT\CHAT_LOOKER\{ano_atual_str}-{mes_formatado}-chat")
    py.typewrite(caminho), py.sleep(1) # Testar sem o sleep
    
    if mes_atual != mes_anterior: # Verifica se o mês atual é diferente do mês anterior
        py.press('enter'), py.sleep(1)
    else:
        py.press('enter')
        localizar_e_clicar(rota.botao_sim), py.sleep(1)

def ChatAssinc():
    
    py.click(x=199, y=56) # Clicando na barra de pesquisa
    py.typewrite(r'https://lookerstudio.google.com/u/0/reporting/bbdcca5b-e387-4caf-ac84-e45308a0179b/page/p_ocu83j7edd') # Digitando o endereço da base ChatAssinc
    py.press('enter')

    try:
        Aguarde_a_Imagem(rota.aguarde_chat_assinc) # Aguardando a pagina carregar por completo
    except SaidaException:
        return
    
    localizar_e_clicar(rota.ano_mes) # Clicando no data_inicio para filtrar data
    localizar_e_clicar(rota.caixa_flegada_live_chat), py.press('tab'), py.sleep(1) # Clicando na caixa de selção
    py.typewrite(f"{abreviacao}. de {ano_atual_str}")
    py.moveTo(x=1686, y=785)
    py.press('tab'), py.press('tab'), py.press('space') # Selecionando o mes atual
    py.sleep(8) # Aguardar o filtro carregar as informações
    localizar_e_clicar(rota.vazio), py.sleep(1) # Clicando fora para prosseguir
    py.moveTo(x=361, y=832) # Movendo o mouse para aparecer os 3 pontos
    localizar_e_clicar(rota.tres_pontinhos_tres) # Clicando nos 3 potinhos
    localizar_e_clicar(rota.exportar_lokker)

    try:
        Aguarde_a_Imagem(rota.aguarde_export_como)
    except SaidaException:
        return
    
    py.press('tab'), py.press('down'), py.press('tab'), py.press('space'), py.sleep(1)
    py.press('tab'), py.press('tab'), py.press('enter')

    try:
        Aguarde_a_Imagem(rota.image_path)
    except SaidaException:
        return

    caminho = (rf"G:\CSC\Atendimento\Algar\Planejamento\01.BOLETIM\BASES\CHAT\CHAT_LOOKER\{ano_atual_str}-{mes_formatado}-chat_assinc")
    py.typewrite(caminho), py.sleep(1) # Testar sem o sleep
    
    if mes_atual != mes_anterior: # Verifica se o mês atual é diferente do mês anterior
        py.press('enter'), py.sleep(1)
    else:
        py.press('enter')
        localizar_e_clicar(rota.botao_sim), py.sleep(1)
 

# ENCAPSULAMENTO E TRATAMENTO DE ERROS:

def executar_funcao(funcao):
    try:
        funcao()
    except Exception as e:
        ListaDeErros.append(f"Erro em {funcao.__name__}: {str(e)}")

def main():

    executar_funcao(LoginSales)
    executar_funcao(WhatsSales)
    executar_funcao(BacklogSales)
    executar_funcao(MotivadoresSales)
    executar_funcao(ChatMensalSales)
    executar_funcao(LoginAsc)
    executar_funcao(WhatsAsc)
    executar_funcao(EHCTelefone)
    executar_funcao(LiveChat)
    executar_funcao(ChatAssinc)

    if len(ListaDeErros) > 0:
        mensagem_erros = "\n".join(ListaDeErros)
        msg.alert(text=mensagem_erros, title='ERRO', button="OK")  # Exibe cada erro em uma caixa de diálogo
    else:
        msg.alert(text="Bases baixadas com sucesso!", title="SUCESSO", button="OK")  # Exibe uma mensagem de sucesso

if __name__ == "__main__":
    main()