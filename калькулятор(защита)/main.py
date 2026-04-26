import re
import telebot
from telebot import types
import random
import string

TOKEN = '8440565343:AAFOtGrpcsc3Q0f-gOQIriTA6jtpiTfIyTU'
bot = telebot.TeleBot(TOKEN)

user_mode = {}

def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = types.KeyboardButton("Калькулятор")
    btn2 = types.KeyboardButton("Случайное число")
    btn3 = types.KeyboardButton("Монетка")
    btn4 = types.KeyboardButton("Помощь")
    btn5 = types.KeyboardButton("Бросить кубик")
    btn6 = types.KeyboardButton("Сгенерировать пароль")

    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)

    return markup

def safe_calculate(expression):
    expression = expression.replace(',', '.').strip()

    if not re.fullmatch(r"[0-9\.\+\-\*\/\(\)\s]+", expression):
        return None

    try:
        result = eval(expression, {"builtins": {}}, {})
        return result
    except:
        return None

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@bot.message_handler(commands=['start'])
def start_message(message):
    user_mode[message.chat.id] = None
    bot.send_message(message.chat.id,"Привет! Я очень сладенькйи бот.\nВыбери что могу для тебя сделать сладенький:",reply_markup=main_menu())

@bot.message_handler(func=lambda message: message.text == "Калькулятор")
def calculator_mode(message):
    user_mode[message.chat.id] = "calculator"
    bot.send_message(message.chat.id, "Режим сладенького калькулятора\n - напиши любой пример")

@bot.message_handler(func=lambda message: message.text == "Случайное число")
def random_number(message):
    number = random.randint(1, 100)
    bot.send_message(message.chat.id, f'Случайное число: {number}')

@bot.message_handler(func=lambda message: message.text == "Монетка")
def coin(message):
    result = random.choice(["Орёл", "Решка"])
    bot.send_message(message.chat.id, f"Выпало: {result}")

@bot.message_handler(func=lambda message: message.text == "Бросить кубик")
def roll_dice(message):
    dice_result = random.randint(1, 6)
    bot.send_message(message.chat.id,f"🎲 Бросаю кубик мой сладкий... Выпало: {dice_result}")

@bot.message_handler(func=lambda message: message.text == "Сгенерировать пароль")
def password_generator(message):
    password = generate_password(12)
    bot.send_message(message.chat.id,f" Сгенерированный пароль: `{password}`\n""Храни его как зеницу ока мой сладкий!",parse_mode='Markdown')

@bot.message_handler(func=lambda message: message.text == "Помощь")
def help_button(message):
    bot.send_message(
        message.chat.id,
        "Я умею:\n"
        " - считать примеры (Калькулятор)\n"
        " - выбирать случайные числа\n"
        " - подкидывать монетку\n"
        " - бросать кубик\n"
        " - генерировать пароли"
    )

@bot.message_handler(func=lambda message: True)
def text_handler(message):
    chat_id = message.chat.id
    if user_mode.get(chat_id) == "calculator":
        try:
            result = safe_calculate(message.text)
            if result is not None:
                bot.send_message(chat_id, f"Ответ: {result}")
            else:
                bot.send_message(chat_id, "Ошибка. Научись писать правильно неуч, вот так: 5 * 5")
        except:
            bot.send_message(chat_id, "Ошибка вычисления. Проверь выражение.")
    else:
        bot.send_message(chat_id,"Не понимаю тебя мой сладкий, выбери действие в меню",reply_markup=main_menu())

bot.polling(none_stop=True)











































































