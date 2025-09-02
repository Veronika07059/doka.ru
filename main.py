import telebot

# Токен вашего бота
TOKEN = '8201216385:AAEB5IyJsI6ZcTjbl9plUiYE9QIcRWMtiPc'

bot = telebot.TeleBot(TOKEN)

# Команда /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Используйте команду /webapp для открытия сайта.")

# Команда /webapp
@bot.message_handler(commands=['webapp'])
def send_webapp(message):
    # URL вашего сайта на GitHub Pages
    website_url = 'https://veronika07059.github.io/doka.ru/'
    # Отправляем кнопку для открытия сайта
    markup = telebot.types.InlineKeyboardMarkup()
    btn = telebot.types.InlineKeyboardButton(text="Открыть Web Mini App", url=website_url)
    markup.add(btn)
    bot.send_message(message.chat.id, "Нажмите кнопку ниже, чтобы открыть сайт:", reply_markup=markup)

bot.polling()