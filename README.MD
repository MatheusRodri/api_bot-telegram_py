# 🚀 BOT-TELEGRAM

Este projeto é um bot para o Telegram desenvolvido com o objetivo de aprendizado e criação de bots de forma simples e rápida, utilizando a biblioteca python-telegram-bot.

---

## ✅ Requisitos

Antes de executar o projeto, certifique-se de ter os seguintes requisitos instalados:

- Python 3.7 ou superior
- Anaconda
- Editor de texto ou IDE de sua preferência (Visual Studio Code, PyCharm, etc.)

---
## 🛠 Tecnologias Utilizadas

O projeto foi construído com as seguintes tecnologias:

- 🔙 Back-end
    - Python
        - python-telegram-bot
        - python-dotenv

## ⚙️ Como Executar o Projeto

Siga os passos abaixo para configurar e rodar o bot:

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