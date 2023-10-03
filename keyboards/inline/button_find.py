from telebot import types
from loader import bot


def button_find(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Поиск фильма или сериала", callback_data='find_movie')
    btn2 = types.InlineKeyboardButton("Поиск медийной личности", callback_data='find_person')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "Нажмите на кнопку для выбора тематик",
                     reply_markup=markup)
