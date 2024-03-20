from telebot import TeleBot
from telebot.types import Message
from keyboards import *

from config import *

bot = TeleBot(TOKEN)

user_info = {}


@bot.message_handler(commands=['start'])
def reaction_start(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Iltimos, tilni tanlang\nПожалуйста, выберите язык ️", reply_markup=main_btn())


@bot.message_handler(func=lambda message: message.text == "🇺🇿 O'zbekcha")
def start(message):
    user_info[message.chat.id] = {}
    bot.send_message(message.chat.id, "Ismingizni kiriting:", reply_markup=ReplyKeyboardRemove())
    bot.register_next_step_handler(message, save_name)


def save_name(message):
    user_id = message.chat.id
    user_info[user_id]["name"] = message.text
    bot.send_message(user_id, "Raqamingizni jo'nating", reply_markup=send_contact())
    bot.register_next_step_handler(message, save_phone)


def save_phone(message):
    user_id = message.chat.id
    if user_id in user_info:
        user_info[user_id]['phone'] = message.contact.phone_number
        bot.send_message(PRIVATE_CHANNEL_ID,
                         f"Ism Familyasi: {user_info[user_id]['name']}\nRaqami: {user_info[user_id]['phone']}")

        bot.send_message(user_id, "Saqlandi!", reply_markup=keys())


@bot.message_handler(func=lambda message: message.text == 'Kontaktlarimiz ☎️')
def reaction_contact(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id,
                     "Bizning Instagram: https://www.instagram.com/totrans_logistics/\nBizning Telegram:@totrans\nBizning Facebook:https://www.facebook.com/totrans.uz/\nBizning Pochtamiz:info@totrans.com")


@bot.message_handler(func=lambda message: message.text == "🇷🇺 Русский")
def start(message):
    user_info[message.chat.id] = {}
    bot.send_message(message.chat.id, "Введите ваше имя:", reply_markup=ReplyKeyboardRemove())
    bot.register_next_step_handler(message, save_name1)


def save_name1(message):
    user_id = message.chat.id
    user_info[user_id]["name"] = message.text
    bot.send_message(user_id, "Введите ваш номер телефона:", reply_markup=send_contact1())
    bot.register_next_step_handler(message, save_phone1)


def save_phone1(message):
    user_id = message.chat.id
    if user_id in user_info:
        user_info[user_id]['phone'] = message.contact.phone_number
        bot.send_message(PRIVATE_CHANNEL_ID,
                         f"Ism Familyasi: {user_info[user_id]['name']}\nRaqami: {user_info[user_id]['phone']}")

        bot.send_message(user_id, "Сохранено!", reply_markup=keys1())


@bot.message_handler(func=lambda message: message.text == 'Наши контакты ☎️')
def reaction_contact(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id,
                     "Наш Instagram: https://www.instagram.com/totrans_logistics/\nНаш Telegram:@totrans\nНаш Facebook:https://www.facebook.com/totrans.uz/\nНаша почта: info@totrans.com")


bot.infinity_polling()
