from flask import Flask
from extension import db
from models import Book
import click

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db.init_app(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.cli.command()
def create():
    db.drop_all()
    db.create_all()
    Book.init_db()
    click.echo('Create Done')

if __name__ == '__main__':
    app.run(debug=True)