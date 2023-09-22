from telebot import types

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

def registration(user_id):


    buttons = InlineKeyboardButton(row_width=1)

    registration = InlineKeyboardButton(text='registration', callback_data='registration')


    buttons.add(registration)
    return buttons
def registration_name(user_id):


    buttons = InlineKeyboardButton(row_width=1)

    registration_name = InlineKeyboardButton(text="Name", callback_data="registration_name")


    buttons.add(registration_name)
    return buttons
def registration_location():
    buttons = InlineKeyboardButton(row_width=1)

    registration_location = InlineKeyboardButton(text="location", callback_data="registration_location")

    buttons.add(registration_location)
    return buttons
def registration_number():
    buttons = InlineKeyboardButton(row_width=1)

    registration_number = InlineKeyboardButton(text="location", callback_data="registration_location")

    buttons.add(registration_number)

    return buttons


