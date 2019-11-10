import scrapy, html2text, re, random
from PokemonWebSpider.pokemon import Pokemon
from configparser import ConfigParser
parser = ConfigParser()
parser.read('scrapy.cfg')


class PokemonTeam(scrapy.Spider):
    name = parser.get('spider', 'name')
    allowed_domains = [parser.get('url', 'allowed_domains')]
    start_urls = [parser.get('url', 'start_urls')]

    def parse(self, response):
        pokedex = response.css(parser.get('response', 'pokedex')).extract()
        name = response.css(parser.get('response', 'name')).extract()
        lenType = response.css(parser.get('response', 'type')).extract()
        sprite = response.css(parser.get('response', 'sprite')).extract()

        def check(value, list):
            valid = 0
            if value not in list:
                valid = 1
                return valid
            else:
                return valid

        items = []
        namePokemons = []
        typesList = []
        for i in range(6):
            nombre = random.choice(name)

            typesLen = lenType[name.index(nombre)].split(" · ")
            currentType = lenType[name.index(nombre)]
            validType = check(currentType, typesList)

            while nombre in map(lambda x: x, namePokemons) or len(typesLen) == 1 or validType == 0:
                nombre = random.choice(name)

                typesLen = lenType[name.index(nombre)].split(" · ")
                currentType = lenType[name.index(nombre)]
                validType = check(currentType, typesList)

            namePokemons.append(nombre)
            typesList.append(currentType)

        print("My Team")
        print(namePokemons)