from tkinter import *
from PIL import Image, ImageTk  # Certifique-se de ter a biblioteca Pillow instalada

def continuar():
    resultado_label.config(text="Você escolheu continuar!")

def encerrar():
    exit()

# Criação da janela principal
tela = Tk()
tela.title("TioPrime")
tela.geometry("700x400")  # Tamanho da tela do cartão

# Definindo o ícone da janela
caminho_icone = r'C:\Users\juliopc\Desktop\Robos\AutoDownloadBases\img\Transformers.ico'
tela.iconbitmap(caminho_icone)  # Substitua pelo caminho do seu arquivo .ico

# Caminho da imagem para o título
caminho_imagem = r'C:\Users\juliopc\Desktop\Robos\AutoDownloadBases\img\Trasnftitle.png'  # Substitua pelo caminho da sua imagem

imagem = Image.open(caminho_imagem)
imagem = imagem.resize((80, 80), Image.LANCZOS)  # Redimensiona a imagem para 50x50 pixels
imagem_tk = ImageTk.PhotoImage(imagem)  # Converte a imagem para um formato que Tkinter pode usar

# Título com ícone
titulo_frame = Frame(tela)
titulo_frame.pack(pady=20)

if imagem_tk:  # Verifica se a imagem foi carregada corretamente
    icone_label = Label(titulo_frame, image=imagem_tk)
    icone_label.pack(side=LEFT)  # Adiciona a imagem à esquerda
titulo = Label(titulo_frame, text="Iniciando Automação...", font=("Helvetica", 16))
titulo.pack(side=LEFT, padx=10)  # Adiciona o texto à direita da imagem



# Descrição
descricao = Label(tela, text="Seu Chrome está aberto?", font=("Helvetica", 12))
descricao.pack(pady=10)

# Botões
botao_sim = Button(tela, text="Sim", command=continuar, width=12)
botao_sim.pack(side=LEFT, padx=100, pady=100)

botao_nao = Button(tela, text="Não", command=encerrar, width=12)
botao_nao.pack(side=RIGHT, padx=100, pady=100)

botao_Cancelar = Button(tela, text="Cancelar", command=encerrar, width=12)
botao_Cancelar.pack(side=RIGHT, padx=10, pady=10)

# Label para mostrar o resultado da escolha
resultado_label = Label(tela, text="", font=("Helvetica", 12))
resultado_label.pack(pady=10)

# Iniciar o loop da interface
tela.mainloop()