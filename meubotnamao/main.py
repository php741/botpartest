import telebot
from constants import *
from coingeckoeth_price import eth_price



bot = telebot.TeleBot(CHAVE_API)

user_states = {}
language_menu = {
    "English 🇺🇸": "Select your preferred option:\n/opcao1 One Month $15.00\n/opcao2 Three Months $35.00\n/opcao3 Lifetime access $100.00",
    "中文 🇨🇳": "选择您的首选选项：\n/opcao1 一个月 $15.00\n/opcao2 三个月 $35.00\n/opcao3 终身访问 $100.00",
    "हिन्दी 🇮🇳": "अपना पसंदीदा विकल्प चुनें:\n/opcao1 एक महीना $15.00\n/opcao2 तीन महीने $35.00\n/opcao3 लाइफटाइम एक्सेस $100.00",
    "Español 🇪🇸": "Seleccione su opción preferida:\n/opcao1 Un mes $15.00\n/opcao2 Tres meses $35.00\n/opcao3 Acceso de por vida $100.00",
    "Français 🇫🇷": "Sélectionnez votre option préférée :\n/opcao1 Un mois $15.00\n/opcao2 Trois mois $35.00\n/opcao3 Accès à vie $100.00",
    "Português 🇧🇷": "Selecione sua opção preferida:\n/opcao1 Um mês R$ 15,00\n/opcao2 Três meses R$ 35,00\n/opcao3 Acesso vitalício R$ 100,00",
    "عربى 🇸🇦": "اختر الخيار المفضل لديك:\n/opcao1 شهر واحد $15.00\n/opcao2 ثلاثة أشهر $35.00\n/opcao3 دخول مدى الحياة $100.00"
}

language_messages = {
    "English 🇺🇸": "Please send:",
    "中文 🇨🇳": "请发送：",
    "हिन्दी 🇮🇳": "कृपया भेजें:",
    "Español 🇪🇸": "Por favor, envíe:",
    "Français 🇫🇷": "Veuillez envoyer:",
    "Português 🇧🇷": "Por favor, envie:",
    "عربى 🇸🇦": "يرجى إرسال:"
}












@bot.message_handler(commands=['start'])
def start(message):
    user = message.from_user
    text = "Select your preferred language:"
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add("English 🇺🇸", "中文 🇨🇳", "हिन्दी 🇮🇳")
    keyboard.add("Español 🇪🇸", "Français 🇫🇷", "Português 🇧🇷", "عربى 🇸🇦")
    bot.send_message(user.id, text, reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text in language_menu.keys())
def language_selected(message):
    user = message.from_user
    selected_language = message.text
    menu_text = language_menu[selected_language]
    bot.send_message(user.id, menu_text)


@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    user_id = mensagem.from_user.id
    selected_language = user_states.get(user_id)  # Retrieve the user's selected language
    valor_plano = 15 / eth_price
    bot.send_message(mensagem.chat.id, language_messages[selected_language])
    bot.send_message(mensagem.chat.id, valor_plano)
    if selected_language == "English 🇺🇸":
        bot.send_message(mensagem.chat.id, "Eth To the following address")
        bot.send_message(mensagem.chat.id, "After sending the requested amount, please paste the hash transaction here.")
    elif selected_language == "中文 🇨🇳":
        bot.send_message(mensagem.chat.id, "将 ETH 发送到以下地址")
        bot.send_message(mensagem.chat.id, "发送所需金额后，请在此处粘贴哈希交易。")
    elif selected_language == "हिन्दी 🇮🇳":
        bot.send_message(mensagem.chat.id, "निम्नलिखित पते पर ईथ भेजें")
        bot.send_message(mensagem.chat.id, "अनुरोधित राशि भेजने के बाद, कृपया यहाँ हैश लेन-देन पेस्ट करें।")
    elif selected_language == "Español 🇪🇸":
        bot.send_message(mensagem.chat.id, "Envíe ETH a la siguiente dirección")
        bot.send_message(mensagem.chat.id,
                         "Después de enviar la cantidad solicitada, por favor pegue aquí el hash de la transacción.")
    elif selected_language == "Français 🇫🇷":
        bot.send_message(mensagem.chat.id, "Envoyez de l'ETH à l'adresse suivante")
        bot.send_message(mensagem.chat.id,"Après avoir envoyé le montant demandé, veuillez coller le hachage de la transaction ici.")
    elif selected_language == "Português 🇧🇷":
        bot.send_message(mensagem.chat.id, "Envie ETH para o seguinte endereço")
        bot.send_message(mensagem.chat.id, "Após enviar a quantia solicitada, por favor cole o hash da transação aqui.")

@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    user_id = mensagem.from_user.id
    selected_language = user_states.get(user_id)  # Retrieve the user's selected language
    valor_plano = 35 / eth_price
    bot.send_message(mensagem.chat.id, language_messages[selected_language])
    bot.send_message(mensagem.chat.id, valor_plano)
    if selected_language == "English 🇺🇸":
        bot.send_message(mensagem.chat.id, "Eth To the following address")
        bot.send_message(mensagem.chat.id, "After sending the requested amount, please paste the hash transaction here.")
    elif selected_language == "中文 🇨🇳":
        bot.send_message(mensagem.chat.id, "将 ETH 发送到以下地址")
        bot.send_message(mensagem.chat.id, "发送所需金额后，请在此处粘贴哈希交易。")
    elif selected_language == "हिन्दी 🇮🇳":
        bot.send_message(mensagem.chat.id, "निम्नलिखित पते पर ईथ भेजें")
        bot.send_message(mensagem.chat.id, "अनुरोधित राशि भेजने के बाद, कृपया यहाँ हैश लेन-देन पेस्ट करें।")
    elif selected_language == "Español 🇪🇸":
        bot.send_message(mensagem.chat.id, "Envíe ETH a la siguiente dirección")
        bot.send_message(mensagem.chat.id,
                         "Después de enviar la cantidad solicitada, por favor pegue aquí el hash de la transacción.")
    elif selected_language == "Français 🇫🇷":
        bot.send_message(mensagem.chat.id, "Envoyez de l'ETH à l'adresse suivante")
        bot.send_message(mensagem.chat.id,"Après avoir envoyé le montant demandé, veuillez coller le hachage de la transaction ici.")
    elif selected_language == "Português 🇧🇷":
        bot.send_message(mensagem.chat.id, "Envie ETH para o seguinte endereço")
        bot.send_message(mensagem.chat.id, "Após enviar a quantia solicitada, por favor cole o hash da transação aqui.")

@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    user_id = mensagem.from_user.id
    selected_language = user_states.get(user_id)  # Retrieve the user's selected language
    valor_plano = 100 / eth_price
    bot.send_message(mensagem.chat.id, language_messages[selected_language])
    bot.send_message(mensagem.chat.id, valor_plano)
    if selected_language == "English 🇺🇸":
        bot.send_message(mensagem.chat.id, "Eth To the following address")
        bot.send_message(mensagem.chat.id, "After sending the requested amount, please paste the hash transaction here.")
    elif selected_language == "中文 🇨🇳":
        bot.send_message(mensagem.chat.id, "将 ETH 发送到以下地址")
        bot.send_message(mensagem.chat.id, "发送所需金额后，请在此处粘贴哈希交易。")
    elif selected_language == "हिन्दी 🇮🇳":
        bot.send_message(mensagem.chat.id, "निम्नलिखित पते पर ईथ भेजें")
        bot.send_message(mensagem.chat.id, "अनुरोधित राशि भेजने के बाद, कृपया यहाँ हैश लेन-देन पेस्ट करें।")
    elif selected_language == "Español 🇪🇸":
        bot.send_message(mensagem.chat.id, "Envíe ETH a la siguiente dirección")
        bot.send_message(mensagem.chat.id,
                         "Después de enviar la cantidad solicitada, por favor pegue aquí el hash de la transacción.")
    elif selected_language == "Français 🇫🇷":
        bot.send_message(mensagem.chat.id, "Envoyez de l'ETH à l'adresse suivante")
        bot.send_message(mensagem.chat.id,"Après avoir envoyé le montant demandé, veuillez coller le hachage de la transaction ici.")
    elif selected_language == "Português 🇧🇷":
        bot.send_message(mensagem.chat.id, "Envie ETH para o seguinte endereço")
        bot.send_message(mensagem.chat.id, "Após enviar a quantia solicitada, por favor cole o hash da transação aqui.")






try:
    bot.polling()
except Exception as e:
    print("An error occurred while polling the bot:", e)





