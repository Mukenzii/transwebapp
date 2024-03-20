from telebot.types import ReplyKeyboardRemove, KeyboardButton, ReplyKeyboardMarkup, WebAppInfo


def main_btn():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("🇺🇿 O'zbekcha"), KeyboardButton(" 🇷🇺 Русский"))

    return markup


def send_contact():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("Raqam jo'natish", request_contact=True))

    return markup


def keys():
    markup = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    webbutton = WebAppInfo('https://logistics.totrans.uz/uz/calculator')
    loginbutton = WebAppInfo('https://logistics.totrans.uz/en/login')

    markup.add(KeyboardButton("Kalkulyator 📱", web_app=webbutton), KeyboardButton("Shaxsiy Kabinet", web_app=loginbutton),
               KeyboardButton("Kontaktlarimiz ☎️"))

    return markup


def keys1():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    webbutton = WebAppInfo('https://logistics.totrans.uz/uz/calculator')
    loginbutton = WebAppInfo('https://logistics.totrans.uz/en/login')

    markup.add(KeyboardButton("Калькулятор 📱", web_app=webbutton), KeyboardButton("Личный кабинет",web_app=loginbutton),
               KeyboardButton("Наши контакты ☎️"))

    return markup


def send_contact1():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("Отправить номер", request_contact=True))

    return markup
