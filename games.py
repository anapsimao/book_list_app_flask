from flask import Flask, render_template

app = Flask(__name__)

class game:
    def __init__(self, name, category, year):
        self.name = name
        self.category = category
        self.year = year


@app.route('/home/')
def ola():
    game1 = game('Game 1', 'category 1', 'year')
    game2 = game('Game 2', 'category 2', 'year')
    list = [game1, game2]
    return render_template('list.html', title='Game List', books_names='Names', games=list)

app.run()