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