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
                mensagemErro = msg.alert(f"Seu robo não localizou a imagem '{ultima_palavra}' ", title="Erro", button="Tentar Novamente")
                print(mensagemErro)
                if mensagemErro == "Tentar Novamente":
                    tempo_espera = 10
                    tempo = 0
                    tentar += 1
                    if tentar == 5:
                        msg.alert(text=f"O robô  não conseguiu localizar a imagem {ultima_palavra}", title="AH NÃO", button="OK")
                        break
            py.sleep(1) # Aguarda 1 segundo antes de tentar novamente
            tempo += 1

def ler_mes_anterior(): # Função para ler o mês anterior de um arquivo
    if os.path.exists("mes_anterior.txt"):
        with open("mes_anterior.txt", "r") as file:
            return int(file.read().strip())
    return None  # Retorna None se o arquivo não existir

def salvar_mes_atual(mes): # Função para salvar o mês atual em um arquivo
    with open("mes_anterior.txt", "w") as file:
        file.write(str(mes))

def Aguarde_a_Imagem(image, tempo_espera=60):
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

### VARIÁVEIS DE CONTROLE ###
abreviacao = mes_atual_abreviado()
mes_anterior = ler_mes_anterior() # Lê o mês anterior do arquivo
#---------------------------------------------------------------------------------------------------------------------------------------------------------


### VARIÁVEIS DE LINKS ###
ManualBoletim = r"https://docs.google.com/document/d/1x09s2GnO6r7hODoH6tZRA9zlzfaT0F_v/edit#heading=h.gjdgxs"
SetinhaExportar = r"C:\Users\juliopc\Desktop\Robos\AutoDownloadBases\img\SetinhaExportar.png"
DetalhesApenas = r"C:\Users\juliopc\Desktop\Robos\AutoDownloadBases\img\DetalhesApenas.png"
FormatoCSV = r"C:\Users\juliopc\Desktop\Robos\AutoDownloadBases\img\FormatoCSV.png"
FormatoAntigo = r"C:\Users\juliopc\Desktop\Robos\AutoDownloadBases\img\FormatoExcelAntigo.png"
BotãoExportar = r"C:\Users\juliopc\Desktop\Robos\AutoDownloadBases\img\BotãoExportar.png"
Exportar = r"C:\Users\juliopc\Desktop\Robos\AutoDownloadBases\img\Exportar.png"
image_path = r"C:\Users\juliopc\Desktop\Robos\AutoDownloadBases\img\SalvarComo.png"
image_filter = r"C:\Users\juliopc\Desktop\Robos\AutoDownloadBases\img\FiltroAguarde.png"
image_dataeID = r"C:\Users\juliopc\Desktop\Robos\AutoDownloadBases\img\CodSeg-EHC.png"
image_sem_titulo = r"C:\Users\juliopc\Desktop\Robos\AutoDownloadBases\img\SemTitulo.png"
PeriodoIntegral = r"C:\Users\juliopc\Desktop\Robos\AutoDownloadBases\img\PeríodoIntegral.png"
Persnalizar = r"C:\Users\juliopc\Desktop\Robos\AutoDownloadBases\img\Personalizar.png"
BotãoSim = r"C:\Users\juliopc\Desktop\Robos\AutoDownloadBases\img\BotãoSim.png"
FiltroASC = r"C:\Users\juliopc\Desktop\Robos\AutoDownloadBases\img\FiltrarASC.png"
FiltroSales = r"C:\Users\juliopc\Desktop\Robos\AutoDownloadBases\img\Filtro.png"
ServiçoSelecione = r"C:\Users\juliopc\Desktop\Robos\AutoDownloadBases\img\ServiçoSelecione.png"
FiltroAvançado = r"C:\Users\juliopc\Desktop\Robos\AutoDownloadBases\img\FiltroAvançadoASC.png"
ExportarASC = r"C:\Users\juliopc\Desktop\Robos\AutoDownloadBases\img\ExportarASC.png"
ExportarWhatsASC = r"C:\Users\juliopc\Desktop\Robos\AutoDownloadBases\img\ExportarWhatsASC.png"
ManualBoletimIMG = r"C:\Users\juliopc\Desktop\Robos\AutoDownloadBases\img\ManualBoletim.png"
LoginSalesIMG = r"C:\Users\juliopc\Desktop\Robos\AutoDownloadBases\img\LoginSales.png"
LoginAscIMG = r"C:\Users\juliopc\Desktop\Robos\AutoDownloadBases\img\LoginAsc.png"
WhatsSalesIMG = r"C:\Users\juliopc\Desktop\Robos\AutoDownloadBases\img\WhatsSales.png"
BackLogIMG = r"C:\Users\juliopc\Desktop\Robos\AutoDownloadBases\img\BackLog.png"
MotivadoresIMG = r"C:\Users\juliopc\Desktop\Robos\AutoDownloadBases\img\Motivador.png"
WhatsAscIMG = r"C:\Users\juliopc\Desktop\Robos\AutoDownloadBases\img\WhatsAsc.png"
ChatMensalIMG = r"C:\Users\juliopc\Desktop\Robos\AutoDownloadBases\img\ChatMensal.png"
Link = r"C:\Users\juliopc\Desktop\Robos\AutoDownloadBases\img\link.png"
LinkDois = r"C:\Users\juliopc\Desktop\Robos\AutoDownloadBases\img\link2.png"
https = r"C:\Users\juliopc\Desktop\Robos\AutoDownloadBases\img\https.png"
DataInicioEHC = r"C:\Users\juliopc\Desktop\Robos\AutoDownloadBases\img\DataInicioEHC.png"
CaixaFlegada = r"C:\Users\juliopc\Desktop\Robos\AutoDownloadBases\img\CaixaFlegada.png"
CaixaNãoFlegada = r"C:\Users\juliopc\Desktop\Robos\AutoDownloadBases\img\CaixaNãoFlegada.png"
Vazio = r"C:\Users\juliopc\Desktop\Robos\AutoDownloadBases\img\Vazio.png"
ParaMoverOMouseEHC = r"C:\Users\juliopc\Desktop\Robos\AutoDownloadBases\img\ParaMoverOMouse.png"
TresPontinhos = r"C:\Users\juliopc\Desktop\Robos\AutoDownloadBases\img\TresPontinhos.png"
TresPontinhosDois = r"C:\Users\juliopc\Desktop\Robos\AutoDownloadBases\img\TresPontinhosDois.png"
ExportarLokker = r"C:\Users\juliopc\Desktop\Robos\AutoDownloadBases\img\ExportarLooker.png"
AguardeExportComo = r"C:\Users\juliopc\Desktop\Robos\AutoDownloadBases\img\ImagemExpotLooker.png"
DataEntrada = r"C:\Users\juliopc\Desktop\Robos\AutoDownloadBases\img\DataEntradaLooker.png"
CaixaFlegadaLiveChat = r"C:\Users\juliopc\Desktop\Robos\AutoDownloadBases\img\CaixaFlegadaLiveChat.png"
CaixaNãoFlegadaLiveChat = r"C:\Users\juliopc\Desktop\Robos\AutoDownloadBases\img\CaixaNãoFlegadaLiveChat.png"
AguardeLiveChat = r"C:\Users\juliopc\Desktop\Robos\AutoDownloadBases\img\AguardeLiveChat.png"
AguardeChatAssinc = r"C:\Users\juliopc\Desktop\Robos\AutoDownloadBases\img\AguardeChatAssinc.png"
AnoMes = r"C:\Users\juliopc\Desktop\Robos\AutoDownloadBases\img\Ano-Mes.png"
TresPontinhosTres = r"C:\Users\juliopc\Desktop\Robos\AutoDownloadBases\img\TresPontinhosTres.png"

def ChatAssinc():

    try:
        Aguarde_imagem_sumir(image_sem_titulo)
    except SaidaException:
        return
    
    py.click(x=199, y=56) # Clicando na barra de pesquisa
    py.typewrite(r'https://lookerstudio.google.com/u/0/reporting/bbdcca5b-e387-4caf-ac84-e45308a0179b/page/p_ocu83j7edd') # Digitando o endereço da base ChatAssinc
    py.press('enter')

    try:
        Aguarde_a_Imagem(AguardeChatAssinc) # Aguardando a pagina carregar por completo
    except SaidaException:
        return
    
    localizar_e_clicar(AnoMes) # Clicando no data_inicio para filtrar data
    localizar_e_clicar(CaixaFlegadaLiveChat), py.press('tab'), py.sleep(1) # Clicando na caixa de selção
    py.typewrite(f"{abreviacao}. de {ano_atual_str}")
    py.moveTo(x=1686, y=785)
    py.press('tab'), py.press('tab'), py.press('space') # Selecionando o mes atual
    py.sleep(10) # Aguardar o filtro carregar as informações
    localizar_e_clicar(Vazio), py.sleep(1) # Clicando fora para prosseguir
    py.moveTo(x=1686, y=785) # Movendo o mouse para aparecer os 3 pontos
    localizar_e_clicar(TresPontinhosTres) # Clicando nos 3 potinhos
    localizar_e_clicar(ExportarLokker)

    try:
        Aguarde_a_Imagem(AguardeExportComo) # Cliando em exportar
    except SaidaException:
        return
    
    py.press('tab'), py.press('down'), py.press('tab'), py.press('space'), py.sleep(1)
    py.press('tab'), py.press('tab'), py.press('enter')

    try:
        Aguarde_a_Imagem(image_path)
    except SaidaException:
        return

    for num in lista:
        if mes_atual == num:
            caminho = (rf"G:\CSC\Atendimento\Algar\Planejamento\01.BOLETIM\BASES\CHAT\CHAT_LOOKER\{ano_atual_str}-0{mes_atual_str}-chat_assinc")
        else:
            caminho = (rf"G:\CSC\Atendimento\Algar\Planejamento\01.BOLETIM\BASES\CHAT\CHAT_LOOKER\{ano_atual_str}-{mes_atual_str}-chat_assinc")
    py.typewrite(caminho), py.sleep(1) # Testar sem o sleep
    
    if mes_atual != mes_anterior: # Verifica se o mês atual é diferente do mês anterior
        py.press('enter')
    else:
        py.press('enter')
        localizar_e_clicar(BotãoSim)
    salvar_mes_atual(mes_atual) # Salva o mês atual para a próxima execução
ChatAssinc()