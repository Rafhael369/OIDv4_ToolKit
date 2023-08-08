# 1.0 Começando

## 1.1 Instalação

Python3 é necessário.

1. Clone este repositório
   ```bash
   git clone https://github.com/Rafhael369/OIDv4_ToolKit.git
   ```
2. Instale os requisitos
   ```bash
   pip install -r requirements.txt
   ```
3. Execute o script de download
   ```bash
   python3 main.py downloader --classes Car Person --type_csv train --limit 1000
   ```

4. Converta as os arquivos de bboxs para o formato yolo
   ```bash
   python3 converter_yolo.py
   ```

5. Enumere as classes de acordo com o número delas. *_Edite o arquivo antes de usar, o caminho da pasta (Bus, Person, etc)_e o numero da classe*
   ```bash
   python3 enumerar_classes.py
   ```