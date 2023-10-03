from telebot import types
from loader import bot


def button_find(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Поиск фильма или сериала")
    btn2 = types.KeyboardButton("Поиск медийной личности")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Что будем искать? фильм или сериал / информацию о человеке",
                     reply_markup=markup)
