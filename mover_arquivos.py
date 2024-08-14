import os
import shutil

def mover_arquivos(diretorio, nomes_arquivos, nova_pasta):
    # Cria a nova pasta, se não existir
    if not os.path.exists(nova_pasta):
        os.makedirs(nova_pasta)

    # Procura e move os arquivos especificados
    for nome_arquivo in nomes_arquivos:
        for raiz, _, arquivos in os.walk(diretorio):
            for arquivo in arquivos:
                if nome_arquivo in arquivo:
                    caminho_arquivo = os.path.join(raiz, arquivo)
                    destino = os.path.join(nova_pasta, arquivo)

                    # Move o arquivo para a nova pasta
                    shutil.move(caminho_arquivo, destino)
                    print(f"Arquivo {arquivo} movido para {nova_pasta}")

# Parâmetros
diretorio_para_pesquisar = "C:/Users/SMALL-PC/Downloads/3dLutGenerate"
nomes_dos_arquivos = ["k72qxcqxvyxuqfbx29q450pfh4yf.jpg", "k72qxcqxvyxuqfbx29q450pfh4yf.webp"]  # Lista de nomes de arquivos
nova_pasta = "C:/Users/SMALL-PC/Downloads/3dLutGenerate/script_meu"

# Executa o script
mover_arquivos(diretorio_para_pesquisar, nomes_dos_arquivos, nova_pasta)