# BOT-TELEGRAM

> Este projeto é um bot para o Telegram desenvolvido com o objetivo de aprendizado e criação de bots de forma simples e rápida, utilizando a biblioteca python-telegram-bot.


## Sumário
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Como Rodar](#como-rodar)
  - [Pré-requisitos](#pré-requisitos)
- [Como Usar](#como-usar)
- [Como Contribuir](#como-contribuir)


## Funcionalidades
- Verificação de mensagens de texto
- Resposta automática a comandos específicos

## Tecnologias Utilizadas
- Python
    - Biblioteca python-telegram-bot
    - Biblioteca python-dotenv

## Como Rodar
### Pré-requisitos
Antes de executar o projeto, certifique-se de ter os seguintes requisitos instalados:

- Python 3.10 ou superior
- Anaconda
- Editor de texto ou IDE de sua preferência (Visual Studio Code, PyCharm, etc.)

## Como rodar
 - Clone o repositório ou baixe o repositório como um arquivo ZIP e extraia-o.
 - Entre na pasta do projeto
 - Crie e ative o ambiente virtual e baixe as dependências:
    - No terminal, navegue até a pasta do projeto e execute os seguintes comandos:
    ```bash
    conda env create -f environment.yml
    ```
- Configure o token do bot:
    - Crie um novo bot no Telegram usando o BotFather para obter o seu token.
    - Em seguida, renomeie o arquivo ``.env.example`` para `.env` e adicione o token do seu bot, conforme o exemplo:TOKEN=SEU_TOKEN_AQUI
- Rode o seguinte o comando ```python main.py```


## Como Contribuir

- Entre em contato comigo pelo [LinkedIn](https://www.linkedin.com/in/matheus-rodrigues-mrj/)
- Faço fork do repositório