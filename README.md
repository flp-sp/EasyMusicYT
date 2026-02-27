# EasyMusicYT

Baixe todas as músicas de URLs listadas em um arquivo `.txt` usando yt-dlp.

## Descrição

EasyMusicYT é um script Python simples que:

- Abre uma janela para selecionar arquivo
- Permite escolher um arquivo `.txt` contendo URLs do YouTube
- Baixa o melhor áudio disponível (formato m4a)
- Salva todos os arquivos dentro da pasta `musics`

Cada URL deve estar em uma linha separada no arquivo de texto.

---

## Requisitos

- Python 3.8 ou superior
- Instalar a dependência:

pip install yt-dlp

Tkinter geralmente já vem instalado com o Python.  
Se não, instale conforme o seu sistema operacional.

---

## Estrutura do Projeto

EasyMusicYT/
│
├── main.py
├── filedialog.py
└── musics/

A pasta `musics` será criada automaticamente se não existir.

---

## Como Usar

1. Crie um arquivo `.txt` com as URLs do YouTube(urls de playlist são compativeis).
Exemplo:

https://www.youtube.com/watch?v=exemplo1  
https://www.youtube.com/watch?v=exemplo2  
https://www.youtube.com/watch?v=exemplo3  

2. Execute o script:

python main.py

3. Selecione seu arquivo `.txt` quando a janela abrir.

4. Aguarde o término do download.

Todos os arquivos de áudio serão salvos na pasta `musics`.

---

## Configurações de Download

O script utiliza a seguinte configuração:

- Formato: bestaudio (m4a)  
- Modelo de saída: musics/%(title)s.%(ext)s

---

## Licença

MIT License
