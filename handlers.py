import telebot # Importa telebot para usar tipos como telebot.types.Message

def register_handlers(bot: telebot.TeleBot):
    """
    Função que registra todos os handlers (funções de resposta) no objeto bot.
    Isso mantém o main.py mais limpo.
    """

    @bot.message_handler(commands=["opcao1"])
    def opcao1(mensagem: telebot.types.Message):
        # Acessa o primeiro nome do usuário que enviou a mensagem
        nome = mensagem.from_user.first_name
        bot.reply_to(mensagem, "Você escolheu a opção 1!")
        bot.reply_to(mensagem, f"Olá, {nome}!") # Usando f-string para uma formatação mais moderna

    @bot.message_handler(commands=["opcao2"])
    def opcao2(mensagem: telebot.types.Message):
        # Envia uma mensagem para o chat, não como resposta direta à mensagem original
        bot.send_message(mensagem.chat.id, "Você escolheu a opção 2!")

    @bot.message_handler(commands=["opcao3"])
    def opcao3(mensagem: telebot.types.Message):
        bot.reply_to(mensagem, "Você escolheu a opção 3!")

    @bot.message_handler(commands=["opcao4"])
    def opcao4(mensagem: telebot.types.Message):
        bot.reply_to(mensagem, "Você escolheu a opção 4!")

    # Se você tivesse outros handlers (por exemplo, para mensagens de texto simples sem comando,
    # ou fotos, documentos), eles viriam aqui.
    # Exemplo:
    # @bot.message_handler(content_types=['text'])
    # def handle_text_messages(message):
    #     if "olá" in message.text.lower():
    #         bot.reply_to(message, "Olá! Como posso ajudar?")