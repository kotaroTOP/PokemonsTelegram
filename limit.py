import telebot
from config import token
from logic import Pokemon
bot = telebot.Telebot(token)
def Cat1(message):
    msg = bot.send_message(message.chat.id, 'привет, введи кол-во фоток которое тебе надо!')
    return limit
def Cat2(message):
    pokemon = Pokemon(message.from_user.username)
    bot.send_photo(message.chat.id, pokemon.caty)
def Cat3(message):
    limit = bot.register_next_step_handler(Cat1.msg, Cat2)
limit = Cat3