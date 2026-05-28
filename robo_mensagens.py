import telebot

# Seu Token Oficial do Telegram
TOKEN = "8615638167:AAHlJZAkrDHXFf-nrklJXGjo9SuOtnO0_lI"

# Inicializa o robô
bot = telebot.TeleBot(TOKEN)

print("🚀 O robô de monitoramento de mensagens está online e aguardando comandos...")

# Função que responde automaticamente quando você digita algo para o robô
@bot.message_handler(func=lambda message: True)
def responder_mensagem(message):
    texto_recebido = message.text.lower()
    id_do_chat = message.chat.id
    nome_usuario = message.from_user.first_name
    
    print(f"📥 Mensagem recebida de {nome_usuario}: '{texto_recebido}' (ID do Chat: {id_do_chat})")
    
    if "oi" in texto_recebido or "olá" in texto_recebido:
        resposta = f"Hello {nome_usuario}! I am your Python assistant. How can I help your business today?"
    elif "status" in texto_recebido:
        resposta = "📊 SYSTEM STATUS: All servers running smoothly. Python robot is 100% active!"
    else:
        resposta = "🤖 Command not recognized. Try typing 'oi' or 'status' to test my integration."
        
    bot.reply_to(message, resposta)

# Mantém o robô rodando continuamente sem parar
bot.infinity_polling()
