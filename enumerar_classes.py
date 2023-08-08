import os
import re


def replace_tags_in_lines(file_path, replacements):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        for line in lines:
            for tag, replacement in replacements.items():
                pattern = r'\b{}\b'.format(re.escape(tag))
                line = re.sub(pattern, replacement, line)
            file.write(line)


def main(directory_path, replacements):
    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory_path, filename)
            replace_tags_in_lines(file_path, replacements)


if __name__ == "__main__":
    # Substitua pelo caminho do diretório que contém os arquivos .txt
    directory_path = "/home/rafa/Documentos/yolov8/OIDv4_ToolKit/OID/Dataset/train/Vehicle registration plate/Label"

    # Substitua as tags pelas palavras correspondentes (incluindo tags compostas)
    replacements = {
        '4':'Truck',  # Substitui "Car red" por "3"
        '3':'Car',
        '0':'Person',
        '5':'Bus',
        '1':'Vehicle registration plate'
        # Adicione mais pares de substituição conforme necessário
    }

    main(directory_path, replacements)
