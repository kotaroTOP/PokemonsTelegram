import telebot 
from config import token
from logic import Pokemon
from logic import Fighter, Wizard

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Это бот с покемонами просто пон')
@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in pokemon.pokemons.keys():
        pokemon = Pokemon(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")
@bot.message_handler(commands=['aipom'])
def Aipom(message):
    if message.from_user.username not in pokemon.pokemons.keys():
        pokemon = Pokemon(message.from_user.username)
        bot.send_message(message.chat.id, 'Эйпом')
        bot.send_photo(message.chat.id, pokemon.aipom_photo())
    else:
        bot.reply_to(message, "Ты уже взял себе покемона")
@bot.message_handler(commands=['MyPokemon'])
def MyPokemon(message):
    pokemon = Pokemon(message.from_user.username)
    bot.send_message(message.chat.id, pokemon.name)
    bot.send_message(message.chat.id, pokemon.img)
@bot.message_handler(commands=['RandomCat'])
def Cat1(message):
    msg = bot.send_message(message.chat.id, 'привет, введи кол-во фоток которое тебе надо!')
    return Cat3
def Cat2(message):
    pokemon = Pokemon(message.from_user.username)
    bot.send_photo(message.chat.id, pokemon.caty)
def Cat3(message):
    limit = bot.register_next_step_handler(Cat1.msg, Cat2)
if __name__ == "__main__":
    wizard = Wizard("username1")
    fighter = Fighter("username2")

    print(wizard.info())
    print("#"*10)
    print(fighter.info())
    print("#"*10)
    print(wizard.attack(fighter))
    print(fighter.attack(wizard))
@bot.message_handler(commands=['Atack'])
def atack(message):
    if message.reply_to_message:
        bot.send_message(message.from_user.username, "Сражается с", message.reply_to_message.from_user.username)
        
bot.infinity_polling(print('Bot Started'), none_stop=True)

