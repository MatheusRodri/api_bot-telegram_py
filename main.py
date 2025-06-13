import os
import pyTelegramBotAPI as telebot  # type: ignore # Importa a biblioteca do bot do Telegram
from dotenv import load_dotenv

# Importa as funções dos módulos que criaremos
from handlers import register_handlers
from utils import get_welcome_message

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()
CHAVE_API = os.getenv("CHAVE_BOT")

# Verifica se a chave da API foi carregada. É importante!
if not CHAVE_API:
    raise ValueError("CHAVE_API não encontrada no arquivo .env. Verifique se o arquivo .env existe e a chave está definida.")

# Inicializa o bot com a sua chave da API
bot = telebot.TeleBot(CHAVE_API)

# --- Registro dos Handlers ---
# Chama a função que registra todos os handlers de comandos do bot
register_handlers(bot)

# Handler para qualquer mensagem que não seja um comando específico
# Ele vai usar a função get_welcome_message() do utils.py
@bot.message_handler(func=lambda message: True) # Captura todas as mensagens
def default_response(message):
    bot.reply_to(message, get_welcome_message())

# --- Início do Bot ---
print("Bot do Telegram iniciado! Pressione Ctrl+C para parar.")
bot.polling() # Inicia o loop de recebimento de mensagens