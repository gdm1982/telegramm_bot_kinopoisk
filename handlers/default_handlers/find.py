from loader import bot
from keyboards.reply.button_find import button_find


@bot.message_handler(commands=['find'])
def start(message):
    button_find(message)
