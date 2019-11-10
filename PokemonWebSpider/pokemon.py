from scrapy.item import Item, Field


class Pokemon(Item):
    pokedex = Field()
    name = Field()
    type = Field()
    sprite = Field()