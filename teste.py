import os

diretorio_base = os.path.expanduser("~/Documentos")
caminho_arquivo = os.path.join(diretorio_base, "app", "img")
if not os.path.exists(caminho_arquivo):
    print(f"O diretório não foi encontrado: {caminho_arquivo}")
else:
    print(f"O diretório foi encontrado: {caminho_arquivo}")