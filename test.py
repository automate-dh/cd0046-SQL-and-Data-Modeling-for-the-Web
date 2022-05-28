from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres@localhost:5432/fyyur'

db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Integer, nullable=False)

db.create_all()

@app.route('/')
def index():
    return "hello, world"

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
