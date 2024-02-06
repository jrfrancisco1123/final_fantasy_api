from flask_app import app
from flask import render_template
import requests

ff_char = requests.get("https://www.moogleapi.com/api/v1/characters")
results_char = ff_char.json()
ff_games = requests.get("https://www.moogleapi.com/api/v1/games")
results_games = ff_games.json()

def get_game(game_title):
    all_games = []
    for row in results_games:
        if row['title'] == game_title:
            all_games.append(row)
    return all_games

def get_char(title):
    all_characters = []
    for row in results_char:
        if row['origin'] == title:
            character = {
                'name': row['name'],
                'age': row['age'],
                'job': row['job'],
                'origin': row['origin'],
                'description': row['description'],
                'pictures': row['pictures'][0]['url']
            }
            all_characters.append(character)
    return all_characters

@app.get('/')
def index():
    print(get_char('Final Fantasy 02'))
    return render_template('index.html')

@app.get('/view/<game>/<char>')
def game_info(game, char):
    game_info = get_game(game)
    char_info = get_char(char)
    return render_template('game.html', game_info=game_info, char_info=char_info)