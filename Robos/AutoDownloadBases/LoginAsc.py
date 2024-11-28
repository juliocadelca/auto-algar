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
#---------------------------------------------------------------------------------------------------------------------------------------------------------

### VARIÁVEIS DE LINKS E CAMINHOS ###

class Caminhos:
    def __init__(self):

        base_path = os.path.expanduser(r"~/Desktop/Robos/AutoDownloadBases/img") ### Usando os.path.expanduser para garantir que funcione em qualquer máquina
        
        self.manual_boletim = r"https://docs.google.com/document/d/1x09s2GnO6r7hODoH6tZRA9zlzfaT0F_v/edit#heading=h.gjdgxs"
        self.setinha_exportar = os.path.join(base_path, "SetinhaExportar.png")
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

def Aguarde_a_Imagem(image, tempo_espera=20):
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

def Aguarde_imagem_sumir(image, tempo_espera=20):
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

def AbrirChromeAberto():
    
    py.keyDown('win'), py.press('tab'), py.keyUp('win')
    localizar_e_clicar(rota.chrome)
    py.hotkey('ctrl', 't'), py.sleep(3) # Abrir uma nova aba

def localizar_e_clicar(image, tempo_espera=20):
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


def LoginAsc():
    py.sleep(2)
    try:
        Aguarde_imagem_sumir(rota.image_sem_titulo)
    except SaidaException:
        return 
    
    py.hotkey("ctrl", "w")

    try:
        Aguarde_a_Imagem(rota.manual_boletim_img) # Aguarda o manual carregar por completo
    except SaidaException:
        return 
    
    localizar_e_clicar(rota.login_asc_img), py.sleep(1) # Clicando na posição Login Asc
    localizar_e_clicar(rota.link) # Clicando no link do relatório
    localizar_e_clicar(rota.https), py.sleep(4)
    py.click(x=613, y=295) # Clicar no filtro de data e selecionar a data 01 do mês atual (NÃO TEVE JEITO DE COLOCAR IMAGEM, POR ISSO ESTÁ COMO X E Y)
    py.typewrite(f"01/{mes_atual_str}/{ano_atual_str}")
    py.press('enter'), py.sleep(1)
    localizar_e_clicar(rota.filtro_asc) # Clicando no botão filtrar
    py.sleep(2)
    localizar_e_clicar(rota.exportar_asc) # Clicando no botão exportar

    try:
        Aguarde_a_Imagem(rota.image_path)
    except SaidaException:
        return
    
    for num in lista:
        if mes_atual == num:
            caminho = (rf"G:\CSC\Atendimento\Algar\Planejamento\01.BOLETIM\BASES\AGENTESASC\{ano_atual_str}\0{mes_atual_str}-{ano_atual_str}-agtasc")
        else:
            caminho = (rf"G:\CSC\Atendimento\Algar\Planejamento\01.BOLETIM\BASES\AGENTESASC\{ano_atual_str}\{mes_atual_str}-{ano_atual_str}-agtasc")
    py.typewrite(caminho)

    if mes_atual != mes_anterior: # Verifica se o mês atual é diferente do mês anterior
        py.press('enter')
    else:
        py.press('enter')
        localizar_e_clicar(rota.botao_sim)
LoginAsc()