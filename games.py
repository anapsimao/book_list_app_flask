from flask import Flask, render_template

app = Flask(__name__)

class book:
    def __init__(self, name, summary, year):
        self.name = name
        self.category = summary
        self.console = year


@app.route('/home/')
def ola():
    book1 = book('Book 1', 'summary 1', 'year')
    book2 = book('Book 2', 'summary 2', 'year')
    list = [book1, book2]
    return render_template('list.html', title='Book List', books_names='Names', books=list)

app.run()