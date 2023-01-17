import os

pasta = "/home/rafhael/Projetos/darknet/treinamento4/test"
i = 1
for diretorio, subpastas, arquivos in os.walk(pasta):
    for arquivo in arquivos:
        if arquivo[-1] == 'g':
            caminho = "/home/rafhael/Projetos/darknet/treinamento4/test/"+arquivo
            f = open("test.txt", "a")
            f.write(f"\n{caminho}")
            f.close()