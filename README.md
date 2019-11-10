# Reto Pokémon Web Spider <img src="https://image.flaticon.com/icons/svg/1752/1752813.svg" alt="Snorlax" height="40" width="40"> <img src="https://image.flaticon.com/icons/svg/1752/1752867.svg" alt="Teddiursa" height="40" width="40"> <img src="https://image.flaticon.com/icons/svg/1752/1752682.svg" alt="Duskull" height="40" width="40"> <img src="https://image.flaticon.com/icons/svg/1752/1752713.svg" alt="Jigglypuff" height="40" width="40"> <img src="https://image.flaticon.com/icons/svg/1752/1752633.svg" alt="Aaron" height="40" width="40"> <img src="https://image.flaticon.com/icons/svg/1752/1752695.svg" alt="Gloom" height="40" width="40">
El 2n reto antes de la HackEPS 2019, consistirá en un pokémon scrapper que tendrá que mostrar los resultados en formato html.

## Explicación <img src="https://image.flaticon.com/icons/svg/1180/1180260.svg" alt="Explanation Icon" height="40" width="40">
Este reto consiste en conseguir crear un equipo de 6 pokémon de doble tipo, a partir de la información de [PokemonDB](https://pokemondb.net/). 
Para generar nuestro equipo Pokémon, tenemos que hacer lo siguiente:

Abrimos un terminal dentro de nuestro proyecto PokemonWebSpider, y ejecutamos el siguiente comando:
```
  scrapy crawl pokemonteam --nolog -o data.json
```
En el caso de que queramos sobreescribir los datos del fichero JSON, ejecutamos el siguiente comando:
```
  rm data.json; scrapy crawl pokemonteam --nolog -o data.json
```
Esto lo que va hacer es:
- 1) Obtener los datos desde [PokemonDB](https://pokemondb.net/).
- 2) Exportar el resultado en un archivo JSON.
```
  [
{"pokedex": "#043", "name": "Oddish", "type": "Grass/Poison", "sprite": "https://img.pokemondb.net/sprites/omega-ruby-alpha-sapphire/dex/normal/oddish.png"},
{"pokedex": "#227", "name": "Skarmory", "type": "Steel/Flying", "sprite": "https://img.pokemondb.net/sprites/omega-ruby-alpha-sapphire/dex/normal/skarmory.png"},
{"pokedex": "#228", "name": "Houndour", "type": "Dark/Fire", "sprite": "https://img.pokemondb.net/sprites/omega-ruby-alpha-sapphire/dex/normal/houndour.png"},
{"pokedex": "#281", "name": "Kirlia", "type": "Psychic/Fairy", "sprite": "https://img.pokemondb.net/sprites/omega-ruby-alpha-sapphire/dex/normal/kirlia.png"},
{"pokedex": "#373", "name": "Salamence", "type": "Dragon/Flying", "sprite": "https://img.pokemondb.net/sprites/omega-ruby-alpha-sapphire/dex/normal/salamence.png"},
{"pokedex": "#758", "name": "Salazzle", "type": "Poison/Fire", "sprite": "https://img.pokemondb.net/sprites/ultra-sun-ultra-moon/small/salazzle.jpg"}
]
```
Estos datos los mostraremos en una plantilla HTML (template.html). Para obtener los datos de JSON y mostrarlos en la plantilla se ha utilizado [getJSON() de la libreria JQuery](https://api.jquery.com/jQuery.getJSON/).

## Resultado
El resultado es una tabla con nuestro equipo Pokémon:
![image](https://drive.google.com/file/d/1xgOvPcGCJOR9FGkHMYXw7AXWbi5PsznG/view?usp=sharing)

## Requisitos <img src="https://image.flaticon.com/icons/svg/2132/2132377.svg" alt="Explanation Icon" height="40" width="40"> 

### Lenguaje de programación
Para realizar este reto se ha utilizado:
- Python 3.6.8 [JetBrains PyCharm](https://www.jetbrains.com/pycharm/)
- [Scrapy 1.8.0](https://scrapy.org/)
- HTML + CSS
- [JQuery](https://jquery.com/)
- JSON

### Sistema operativo
Durante el reto se ha utilizado Ubuntu 18.04.3 (64 bits).

## Información
- Group name: [Joaquim Codina](https://github.com/joaquimcodina)
