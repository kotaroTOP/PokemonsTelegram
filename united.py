#Config.py
from random import randint
import telebot
import requests
ApiKey = '' # Токен котов
bot = telebot.TeleBot("") # Токен бота
pickabuto = f'https://cdn.discordapp.com/attachments/1195402813287710820/1219654204541636628/kabuto.jpg?ex=660c167e&is=65f9a17e&hm=2a9b057e31c4b136000bcc85f8c5c09bebf18ae1ab9d22a539906cd29674da83&' #Kabuto pic
kabutoHP = 785
kabutoClass = "Tank"
kabutoPower = 75
#Limit.py#
def Cat1(message):
    msg = bot.send_message(message.chat.id, 'привет, введи кол-во фоток которое тебе надо!')
    return limit
def Cat2(message):
    pokemon = Pokemon(message.from_user.username)
    bot.send_photo(message.chat.id, pokemon.caty)
def Cat3(message):
    limit = bot.register_next_step_handler(Cat1.msg, Cat2)
limit = Cat3
#test.py#
class Ninja:
    # Атрибут класса для хранения общего количества ниндзя
    total_ninjas = 0

    def __init__(self, name, village, jutsu):
        self.name = name      # Имя ниндзя
        self.village = village  # Деревня принадлежности 
        self.jutsu = jutsu    # Способности 
        Ninja.total_ninjas += 1

    def get_info(self):
        return f"Имя: {self.name}, Деревня: {self.village}, Способности: {self.jutsu}"

# Создаем объекты класса Ninja для нескольких ниндзя
ninja1 = Ninja("Наруто Узумаки", "Коноха", "Расенган")
ninja2 = Ninja("Саске Учиха", "Коноха", "Чидори")

# Используем методы и атрибуты
print(ninja1.get_info())  # Выводит: "Имя: Наруто Узумаки, Деревня: Коноха, Способности: Расенган"
print(ninja2.get_info())  # Выводит: "Имя: Саске Учиха, Деревня: Коноха, Способности: Чидори"
print(f"Всего ниндзя: {Ninja.total_ninjas}")  # Выводит: "Всего ниндзя: 2"

class Car:

    # Инициализация объекта (конструктор)
    def __init__(self, make, model, year):
        self.make = make    # Поле или атрибут класса
        self.model = model  # Поле или атрибут  класса
        self.year = year    # Поле или атрибут класса

    # Метод класса для получения информации о машине
    def info(self):
        return f"{self.year} {self.make} {self.model}"

# Создаем объекты класса Car
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2022)

# Используем методы и атрибуты
print(car1.info())  # Выводит: "2020 Toyota Camry"
print(car2.info())  # Выводит: "2022 Honda Civic"

#logic.py#

class Pokemon:
    pokemons = {}
    # Инициализация объекта 
    def __init__(self, pokemon_trainer):
        hp = randint(50, 1000)
        power = randint(10, 100)
        self.hp = hp
        self.power = power
        self.limit = limit
        self.Api = ApiKey
        self.pokemon_trainer = pokemon_trainer   
        self.pokemon_number = randint(1,1000)
        Pokemon.pokemons[pokemon_trainer] = self
        self.img = self.get_img()
        self.name = self.get_name()
        self.caty = self.cat  
#aipom
        self.aipomid = (190)
        self.aipomname = self.aipom_name 
        self.aipomimg = self.aipom_photo
    def aipom_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/190'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Aipom"
    def aipom_photo(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.aipomid}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['front_shiny'])
        else:
            return "Aipom"
#pokemons
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['front_shiny'])
        else:
            return "Nothing"
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Nothing"
    def cat(self):
        url = f'https://api.thecatapi.com/v1/images/search?limit={self.limit}&api_key={self.Api}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data[f'{url}'])
        else:
            return "Nothing"
    #info
    def info(self):
        return f"Имя твоего покеомона: {self.name}, ХП твоего покемона: {self.hp} Сила твоего покемона: {self.power}"
    #image
    def show_img(self):
        return self.img
#aipom
    def aipom(self):
        return self.aipomname
    def aipomphoto(self):
        return self.aipomimg
    def attack(self, enemy):
        if isinstance(enemy, Wizard):
            chance = randint(1,5)
            if chance == 1:
                return "Покемон-волшебник применил щит в сражении"
        if enemy.hp > self.attack:
            enemy.hp -= self.attack
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
        else:
            enemy.hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "
#Types
class Wizard(Pokemon):
    def attack(self, enemy):
        if isinstance(enemy, Wizard):
            chance = randint(1,5)
            if chance == 1:
                return "Покемон-волшебник применил щит в сражении"
class Fighter(Pokemon):
    def attack(self, enemy):
        super_power = randint(60, 150)
        self.power += super_power
        result = super().attack(enemy)
        self.power -= super_power
        return f"{result}\nПокемон применил супер атаку с силой: {super_power}"
#test
#'if __name__ == '__main__':
    #wizard = Wizard("username1")
    #fighter = Fighter("username2")
    #print(wizard.info())
    #print()
    #print(fighter.info())
    #print()
    #print(fighter.attack(wizard))
#main.py
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Это бот с покемонами просто пон')
@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        chance = randint(1,3)
        if chance == 1:
            pokemon = Pokemon(message.from_user.username)
        elif chance == 2:
            pokemon = Wizard(message.from_user.username)
        elif chance == 3:
            pokemon = Fighter(message.from_user.username)
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
@bot.message_handler(commands=['info'])
def MyPokemon(message):
    if message.from_user.username in Pokemon.pokemons.keys():
        pokemon = Pokemon(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.name)
        bot.send_message(message.chat.id, pokemon.img)
@bot.message_handler(commands=['cat'])
def cats(message):
    Cat1()
@bot.message_handler(commands=['attack'])
def attack_pok(message):
    if message.reply_to_message:
        if message.reply_to_message.from_user.username in Pokemon.pokemons.keys() and message.from_user.username in Pokemon.pokemons.keys():
            enemy = Pokemon.pokemons[message.reply_to_message.from_user.username]
            pok = Pokemon.pokemons[message.from_user.username]
            res = pok.attack(enemy)
            bot.send_message(message.chat.id, res)
        else:
            bot.send_message(message.chat.id, "Сражаться можно только с покемонами")
    else:
            bot.send_message(message.chat.id, "Чтобы атаковать, нужно ответить на сообщения того, кого хочешь атаковать")

# Запуск бота        
bot.infinity_polling(print('Bot Started'), none_stop=True)


