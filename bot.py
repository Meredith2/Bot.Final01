import telebot
from telebot import types  # для указание типов

bot = telebot.TeleBot('6184270382:AAF2euCz_zLj9UL7n64ROGM7dfgXiDcE_Kw')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Словарь финансовых терминов")
    btn2 = types.KeyboardButton("Темы финансовой грамотности")
    markup.add(btn1, btn2, )
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Я бот для изучения основ финансовой грамотности".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def main1(message):
    if message.text == "Словарь финансовых терминов":
        bot.send_message(message.chat.id, text="Словарь:)")
    elif message.text == "Темы финансовой грамотности":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn3 = types.KeyboardButton("Что такое деньги?")
        btn4 = types.KeyboardButton("Инфляция и её виды")
        back1 = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn3, btn4, back1)
        bot.send_message(message.chat.id, text="Какая тема тебя интересует?", reply_markup=markup)

    elif message.text == "Что такое деньги?":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn5 = types.KeyboardButton("Классы денег ")
        btn6 = types.KeyboardButton('История денег')
        back2 = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn5, btn6, back2)
        bot.send_message(message.chat.id, text="Деньги это", reply_markup=markup)

    elif message.text == "Классы денег":
        bot.send_message(message.chat.id, text="Деньги делятся")

    elif message.text == "История денег":
        bot.send_message(message.chat.id, text="Деньги были")

    elif message.text == "Инфляция и её виды":
        bot.send_message(message.chat.id, text="Инфляция бывает")

    elif message.text == "Вернуться в главное меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Словарь финансовых терминов")
        button2 = types.KeyboardButton("Темы финансовой грамотности")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммирован..")


bot.polling(none_stop=True)