from random import randint
from api import ApiKey
from limit import limit
import requests
class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):
        hp = randint(50, 1000)
        power = randint(10, 100)
        self.hp = hp
        self.power = power
        self.limit = limit
        self.Api = ApiKey
        self.pokemon_trainer = pokemon_trainer   
        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.caty = self.cat()
#aipom?
        self.aipomid = (190)
        self.aipomname = self.aipom_name 
        self.aipomimg = self.aipom_photo
#aipom?
        Pokemon.pokemons[pokemon_trainer] = self
#aipom?
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
#aipom
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
            return (data['url'])
        else:
            return "Nothing"
    # Метод класса для получения информации
    def info(self):
        return f"Имя твоего покеомона: {self.name}, ХП твоего покемона: {self.hp} Сила твоего покемона: {self.power}"

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
#aipom!
    def aipom(self):
        return self.aipomname
    def aipomphoto(self):
        return self.aipomimg
#aipom!
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
