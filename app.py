from flask import Flask
app = Flask(__name__)
app.run(host='0.0.0.0', port='25734')

from xkcdpass import xkcd_password as xp
import fileinput
import random
import sys
import os
import codecs
from flask import render_template


base = os.path.dirname(os.path.abspath(__file__))
wordfile_places = os.path.join(base, 'lowernocommas')
wordfile_nb_no = os.path.join(base, 'nor-nb')

place_names = xp.generate_wordlist(
        wordfile=wordfile_places,
        min_length=3,
        max_length=10)

weird_places = xp.generate_wordlist(
        wordfile=wordfile_places,
        min_length=3,
        max_length=20)

words = xp.generate_wordlist(
        wordfile=wordfile_nb_no,
        min_length=4,
        max_length=8)




SYMBOLS = [
    "!", "#", "$", "%", "&", "(", ")", "*", "+", "-",
    ",", "-", ".", ":", ";", "<", "=", ">", "?", "@",
    "[", "]", "^", "_", "{", "}", "|", "~", "'"
]
DELIMITORS = ['.', ',', '-', "'", '<']
NUMBERS = ['2', '3', '4', '5', '6', '7', '8', '9']
CHANCE = 0.5


def rng_delimitor(password):
    d = random.choice(DELIMITORS)
    password = [p.title() for p in password.split(' ')]
    #password = password.split(' ') +[
    #    '{}'.format(random.choice(NUMBERS))
    #]

    return d.join(password)


def generate_password(word_class):
    password = xp.generate_xkcdpassword(word_class, numwords=3, case='random')
    return rng_delimitor(password)

@app.route("/")
def hello():
    pw = generate_password(words)
    pw2 = generate_password(place_names)
    return render_template('main.html', pw=pw, pw2=pw2)

@app.route('/weird')
def weird():
    pw = generate_password(weird_places)
    return render_template('main.html', pw=pw, pw2='')

