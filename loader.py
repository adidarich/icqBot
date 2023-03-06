import logging

from start import *

from bot.bot import Bot
from bot.bot import MessageHandler, BotButtonCommandHandler
from bot.bot import Filter

from config import CONFIG


logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%d.%m.%Y %I:%M:%S: %p', level=logging.DEBUG)


def main():
    bot = Bot(token=CONFIG['TOKEN'])
    bot.dispatcher.add_handler(MessageHandler(callback=descr))
    bot.dispatcher.add_handler(BotButtonCommandHandler(callback=ru, filters=Filter.callback_data('ru')))
    bot.dispatcher.add_handler(BotButtonCommandHandler(callback=ru_button_answer))
    bot.dispatcher.add_handler(BotButtonCommandHandler(callback=ru_data, filters=Filter.callback_data('ru_data')))

    bot.dispatcher.add_handler(BotButtonCommandHandler(callback=en, filters=Filter.callback_data('en')))
    bot.dispatcher.add_handler(BotButtonCommandHandler(callback=en_button_answer))
    bot.dispatcher.add_handler(BotButtonCommandHandler(callback=en_data, filters=Filter.callback_data('en_data')))

    bot.start_polling()
