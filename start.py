import json


def descr(bot, event):
    '''
    функция описывает что делает бот и отправляет сообщение в чат
    :param bot:
    :param event:
    :return: text_description
    метод send_text принимает: chat_id - идентификатор чата из которого будет получено смс
                             и text - текст который увидит user
    '''
    text_description = "Я бот Джон 🤗, и ввиду вас в курсе дело📄. Хорошего Дня! 😇" \
                       "I'm a bot John 🤗, and in view of you in the course of the matter📄. Have a good day! 😇"

    bot.send_text(chat_id=event.from_chat, text=text_description)

    startup(bot, event)


def startup(bot, event):
    '''
    функция отправялет в чат смс текст и кнопки для нажатия
    callbackData - поле которое будет возвращено сервером в событии нажатия на кнопку
    text = first_message_text — строка, текст которой будет отправлен пользователю
    inline_keyboard_markup = выводит текст из переменной markup в формате json
    '''
    markup = [
        [{"text": "🇷🇺 Русский", "callbackData": "ru"},
         {"text": "🇬🇧 English", "callbackData": "en"}]
    ]
    first_message_text = "Выберите язык / Choose language"

    bot.send_text(chat_id=event.from_chat,
                  text=first_message_text,
                  inline_keyboard_markup=json.dumps(markup))


def ru(bot, event):
    info = [
        [{"text": "🌐 Википедия", "url": "https://ru.wikipedia.org/wiki/" },
         {"text": "Сведения", "callbackData": "ru_data", "style": "attention"},
         {"text": "Контакты", "callbackData": "contacts", "style": "primary"}]
    ]

    bot.send_text(chat_id=event.from_chat,
                  text="Сведения",
                  inline_keyboard_markup=info)


def ru_button_answer(bot, event):
    '''
    функция описывает ответ нажатия на кнопок
    answer_callback_query - влияет на результат нажатия кнопки
    text - текст будет показан всплывающием уведомлении
    show_alert - если равно True то юзер увидит текст в чате
    '''
    if event.data['callbackData'] == 'ru_data':
        bot.answer_callback_query(query_id=event.data['queryId'],
                                  text="Приветствую 🤝",
                                  show_alert=False)
    elif event.data['callbackData'] == 'contacts':
        bot.answer_callback_query(query_id=event.data['queryId'],
                                  text='123456789',
                                  show_alert=True)


def ru_data(bot, event):
    bot.send_text(chat_id=event.data['message']['chat']['chatId'],
                  text="язык восточнославянской группы славянской ветви индоевропейской языковой семьи, "
                       "национальный язык русского народа. Является одним из наиболее распространённых языков мира")
    ru(bot, event)


def en(bot, event):
    info = [
        [{"text": "🌐 Wikipedia", "url": "https://en.wikipedia.org/wiki/English_language"},
         {"text": "Information", "callbackData": "en_data", "style": "attention"},
         {"text": "Contacts", "callbackData": "contacts", "style": "primary"}]
    ]

    bot.send_text(chat_id=event.from_chat,
                  text="Information",
                  inline_keyboard_markup=info)


def en_button_answer(bot, event):
    if event.data['callbackData'] == 'en_data':
        bot.answer_callback_query(query_id=event.data['queryId'],
                                  text="Welcome 🤝",
                                  show_alert=False)
    elif event.data['callbackData'] == 'contacts':
        bot.answer_callback_query(query_id=event.data['queryId'],
                                  text='123456789',
                                  show_alert=True)


def en_data(bot, event):
    bot.send_text(chat_id=event.data['message']['chat']['chatId'],
                  text="English is a West Germanic language in the Indo-European language family, "
                       "with it's earliest forms spoken by the inhabitants of early medieval England.")
    en(bot, event)