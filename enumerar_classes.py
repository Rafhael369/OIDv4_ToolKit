import os


def replace_numbers_in_lines(file_path, replacements):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        for line in lines:
            words = line.split()
            if words:
                try:
                    first_word = int(words[0])
                    if first_word in replacements:
                        replacement_number = replacements[first_word]
                        line = line.replace(
                            str(first_word), str(replacement_number), 1)
                except ValueError:
                    pass
            file.write(line)


def main(directory_path, replacements):
    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory_path, filename)
            replace_numbers_in_lines(file_path, replacements)


if __name__ == "__main__":
    # Substitua pelo caminho do diretório que contém os arquivos .txt
    directory_path = "/home/rafhael/Projetos/SMA/mi-sma-testes/OIDv4_ToolKit/OID/Dataset/teste"

    # Substitua os números que deseja alterar pelos números correspondentes
    replacements = {
        0: 8,
        # Adicione mais pares de substituição conforme necessário
    }

    main(directory_path, replacements)
