from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:sensedata@localhost:5432/tg'

db = SQLAlchemy(app)

class Vaga_geral(db.Model):
    geral_url = db.Column(db.String(255), primary_key=True)
    geral_titulo = db.Column(db.String)
    geral_cargo = db.Column(db.String)
    geral_desc = db.Column(db.Text)
    geral_data = db.Column(db.DateTime)
    curso_id = db.Column(db.Integer, db.ForeignKey('curso.id'))

class Curso(db.Model):
    curso_id = db.Column(db.String, primary_key=True)
    curso_titulo = db.Column(db.String(50))


@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')


@app.route('/vagas', methods=['GET', 'POST'])
def vagas():
    vagas = Vaga_geral.query.filter().all()
    return render_template('vagas.html', vagas=vagas)


if __name__ == '__main__':
    app.run(port='9090', debug=True)
