import telebot

import BBButtons

bot = telebot.TeleBot('6599104464:AAGijMftMh4KHflBhO5Vo31SiFXH-jztSWE')

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    bot.send_message(user_id, f'{message.from_user.first_name} Enter your name:')
    return start

@bot.message_handler(commands=['text'])
def registration_number(message):
    user_id = message.from_user.id
    bot.send_message(user_id, f'{message.from_user.first_number}Enter number')
    return registration_number
@bot.message_handler(commands=['text'])
def registration_location(message):
    user_id = message.from_user.id
    bot.send_message(user_id, f'{message.from_user.first_location}send location')

    return registration_location
@bot.message_handler(commands=['text'])
def registration_id(message):
    user_id = message.from_user.id
    bot.send_message(user_id, f'{message.from_user.first_id} enter your own id')
    return registration_id
@bot.message_handler(commands=['text'])
def end_of_registration(message):
    user_id = message.from_user.id
    bot.send_message(user_id, f'The end!')
    return end_of_registration
