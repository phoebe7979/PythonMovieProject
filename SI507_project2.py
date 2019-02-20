from flask import Flask, render_template
from movies_tools import *

# Set up application
app = Flask(__name__)

# Routes

@app.route('/')
def frontpage():
    total_mov = numberofmovies
    return '<h1>{} movies recorded.</h1>'.format(total_mov)
#routing the ratings
@app.route('/movies/ratings/')
def htmlcontent():
    return '<p>{}</p>'.format(moviestr)



if __name__ == "__main__":
    app.run()
