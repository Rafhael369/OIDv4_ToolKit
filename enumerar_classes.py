import os


def replace_first_number_in_lines(file_path, replacement):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        for line in lines:
            words = line.split()
            if words:
                try:
                    first_word = int(words[0])
                    new_line = line.replace(str(first_word), str(replacement), 1)
                    file.write(new_line)
                except ValueError:
                    file.write(line)


def main(directory_path, replacement):
    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory_path, filename)
            replace_first_number_in_lines(file_path, replacement)


if __name__ == "__main__":
    # Substitua pelo caminho do diretório que contém os arquivos .txt
    directory_path = '/home/rafa/Documentos/yolov8/OIDv4_ToolKit/OID/Dataset/train/Vehicle registration plate'

    # Substitua o número pelo valor desejado
    replacement_number = 1

    main(directory_path, replacement_number)