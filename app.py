from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:sensedata@localhost:5432/tg'

db=SQLAlchemy(app)

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/vagas', methods=['GET', 'POST'])
def vagas():
    return render_template('vagas.html')

if __name__ == '__main__':
    app.run(port='9090', debug=True)