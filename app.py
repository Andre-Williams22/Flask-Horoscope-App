
from flask import Flask, request, render_template
from random import choice, sample

app = Flask(__name__)

horoscopes = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely', 'tenacious', 'Pythonic']


@app.route('/horoscope')
def get_horoscope():
    """Give the user a compliment"""
    name = request.args.get('name')
    num_horoscopes = int(request.args.get('num_horoscopes'))
    show_horoscopes = request.args.get('show_horoscopes')
    nice_things = ', '.join(sample(horoscopes, num_horoscopes))
    horoscopes_to_show = sample(horoscopes, 3)

    return render_template('horoscopes.html',
        show_horoscopes=show_horoscopes,
        name=name,
        horoscope=horoscope,
        horoscopes=horoscopes_to_show)


@app.route('/')
def index():
    """Show the homepage and ask the user's name."""
    section = 'BEW section A'
    greeting = 'Good Morning'
    return render_template('index.html', 
        section=section,
        greeting=greeting) 