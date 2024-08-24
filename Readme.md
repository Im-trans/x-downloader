# X Video Downloader -  Versão 1.0

### O objetivo desse programa é executar o download de vídeos incorporados em postagens no X.

Apesar da informação de que somente usuários com **selo azul** podem fazer download de vídeos postados na plataforma, esse programa consegue mesmo que você não tenha o selo. 

Como? 

Eu não tenho a mínima ideia!

Talvez o motivo seja a bliblioteca **yt_dlp**.

É preciso ter o python instalado para executar, versão acima da 3.8 e de preferência a 3.11.3.

Também recomendo que seja executado em um virtual enviroment do python e usar o PIP para instalar as bibliotecas e dependências necessárias!

Mas se você está com pressa, dá uma olhada na pasta DIST, onde tem dois executáveis para Windows e que não precisa de instalação nenhuma.

Os arquivos são:

- x_downloader.exe : é uma CLI de linha de comando e funciona com a sintaxe abaixo:
```
    x_downloader.exe [-h] -l LINK_URL [-f FOLDER]

    LINK_URL = link da postagem do vídeo
    FOLDER = pasta onde o vídeo será salvo (opcional) que se não for informada, vai salvar na pasta corrente

    EX: .\x_downloader.exe -l https://x.com/i/status/1827009852536738223 -f .\videos\
```

- UI_x_downloader.exe : interface gráfica, que como é um executável, só funciona em Windows. Dê dois cliques para executar...

### O código fonte acompanham o repositório e a licença é APACHE, então faça e use do jeito que quiser e não me responsabilize por qualquer merda que aconteça! Então é por sua conta e risco

Para execução dos scripts a partir do fonte ou no Linux... Segue o passo a passo a seguir:

1. Instalar o Python, prefencialmente versão 3.11.3 para cima
2. Clonar o repositório
3. Acessar a pasta do repositório (cd x-downloader)
4. Instalar os pacotes do Python necessários: pip install -r .\requirements.txt 
   1. Novamente... recomendo a utilização de virtual env do Python pois a instalação acima vai inchar a instalação padrão do python no seu SO.
5. Está pronto para executar...
   1. Ex:  python .\x_downloader.py -l https://x.com/i/status/1827009852536738223 -f .\videos\
   

### Divirta-se
