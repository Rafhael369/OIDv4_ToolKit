import os
import subprocess

pasta = "/home/rafhael/Projetos/darknet/treinamento4/obj/obj/validation"

for diretorio, subpastas, arquivos in os.walk(pasta):
    for arquivo in arquivos:
        if arquivo[-1] == 't':
            caminho = os.path.join(diretorio, arquivo)
            subprocess.call([f"sed -i -e 's/^.//' {caminho}"], shell=True)
            subprocess.call([f"sed -i -e 's/^/1/' {caminho}"], shell=True)