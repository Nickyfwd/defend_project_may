import re

import telebot

TOKEN = 'ВВЕДИ СВОЙ ТОКЕН БОТА ИЗ ТЕЛЕГРАММА'
bot = telebot.TeleBot(TOKEN)


def safe_calculate(expression):
    expression = expression.replace(',', '.').strip()

    if not re.fullmatch(r"[0-9]\.\+\-\*\/\(\)\s\+",expression):
        return None


    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return result
    except:
        return None

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,
                     "Отправь пример как:\n"
                     "5+5\n"
                     "5*5\n"
                     "5/5\n"
                     "5-5\n")


@bot.message_handler(commands=['help'])
def help_dlachainika(message):
    bot.send_message(message.chat.id,'дарова мой сладке пупесек этот бот может быть кроме калькулятора будет выполнять еще какие нибудь функции если разраб окончательно не обленится')

@bot.message_handler(func=lambda message: True, content_types=['text'])
def calculate_message(message):
    text = message.text.strip()

    if text.startswith('/'):
        return

    result = safe_calculate(text)

    if result is None:
        bot.send_message(message.chat.id, "прости сладке но не получилось вычислить")
    else:
        bot.send_message(message.chat.id, result)

bot.polling(none_stop=True)












































































