# 🤖 BOT-TELEGRAM

Este projeto é um bot para o Telegram desenvolvido com o objetivo de aprendizado e criação de bots de forma simples e rápida, utilizando a biblioteca python-telegram-bot.

## 🚀 Tecnologias Utilizadas
### Back-end
- Python
    - python-telegram-bot

## ⚙️ Como Executar o Projeto

Siga os passos abaixo para configurar e rodar o bot:

 - Clone o repositório ou baixe o repositório como um arquivo ZIP e extraia-o.
 - Entre na pasta do projeto
 - Crie e ative o ambiente virtual no terminal:
    - Para Linux/macOS:
        - ```python -m venv .venv```
        - ```source .venv/bin/activate```
    - Para Windows:
        - ```python -m venv .venv```
        - ```.venv\Scripts\activate```
- `pip install -r requirements.txt`
- Configure o token do bot:
    - Crie um novo bot no Telegram usando o BotFather para obter o seu token.
    - Em seguida, renomeie o arquivo .env.example para .env e adicione o token do seu bot, conforme o exemplo:TOKEN=SEU_TOKEN_AQUI
- Rode o seguinte o comando ```python main.py```