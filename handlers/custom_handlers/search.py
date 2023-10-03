from handlers.default_handlers.start import bot_start
from loader import bot
from utils.send_movie_info import send_movie_info
from utils.send_person_info import send_person_info


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Поиск фильма или сериала':
        bot.send_message(message.chat.id, "Введите название")
        bot.register_next_step_handler_by_chat_id(message.chat.id, send_movie_info)

    elif message.text == 'Поиск медийной личности':
        bot.send_message(message.chat.id, "Введите Имя и Фамилию")
        bot.register_next_step_handler_by_chat_id(message.chat.id, send_person_info)
