from re import search
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
    curso_id = db.Column(db.Integer, db.ForeignKey('curso.curso_id'))

class Curso(db.Model):
    curso_id = db.Column(db.String, primary_key=True)
    curso_titulo = db.Column(db.String(50))


#home page route
@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')


#ads route / curso_id = 1
@app.route('/ads', methods=['GET', 'POST'], defaults={"page": 1})
@app.route('/ads_<int:page>', methods=['GET', 'POST'])
def ads(page):
    page = page
    itens = 10
    vagas = Vaga_geral.query.filter(Vaga_geral.curso_id == '1').paginate(page,itens,error_out=False)
    return render_template('ads.html', vagas=vagas)


#comex route / curso_id = 2
@app.route('/comex', methods=['GET', 'POST'], defaults={"page": 1})
@app.route('/comex_<int:page>', methods=['GET', 'POST'])
def comex(page):
    page = page
    itens = 10
    vagas = Vaga_geral.query.filter(Vaga_geral.curso_id == '2').paginate(page,itens,error_out=False)
    return render_template('comex.html', vagas=vagas)


#Gestão Empresarial / route curso_id = 3
@app.route('/ge', methods=['GET', 'POST'], defaults={"page": 1})
@app.route('/ge_<int:page>', methods=['GET', 'POST'])
def ge(page):
    page = page
    itens = 10
    vagas = Vaga_geral.query.filter(Vaga_geral.curso_id == '3').paginate(page,itens,error_out=False)
    return render_template('ge.html', vagas=vagas)


#Gestão de Serviços / route curso_id = 4
@app.route('/gs', methods=['GET', 'POST'], defaults={"page": 1})
@app.route('/gs_<int:page>', methods=['GET', 'POST'])
def gs(page):
    page = page
    itens = 10
    vagas = Vaga_geral.query.filter(Vaga_geral.curso_id == '4').paginate(page,itens,error_out=False)
    return render_template('gs.html', vagas=vagas)


#Logistica route / curso_id = 5
@app.route('/log', methods=['GET', 'POST'], defaults={"page": 1})
@app.route('/log_<int:page>', methods=['GET', 'POST'])
def log(page):
    page = page
    itens = 10
    vagas = Vaga_geral.query.filter(Vaga_geral.curso_id == '5').paginate(page,itens,error_out=False)
    return render_template('log.html', vagas=vagas)


#Redes de Computadores / route curso_id = 6
@app.route('/redes', methods=['GET', 'POST'], defaults={"page": 1})
@app.route('/redes_<int:page>', methods=['GET', 'POST'])
def redes(page):
    page = page
    itens = 10
    vagas = Vaga_geral.query.filter(Vaga_geral.curso_id == '6').paginate(page,itens,error_out=False)
    return render_template('redes.html', vagas=vagas)


#todas as vagas / route 
@app.route('/todos', methods=['GET', 'POST'], defaults={"page": 1})
@app.route('/todos_<int:page>', methods=['GET', 'POST'])
def todos(page):
    page = page
    itens = 10
    vagas = Vaga_geral.query.paginate(page,itens,error_out=False)
    return render_template('todos.html', vagas=vagas)

if __name__ == '__main__':
    app.run(port='9090', debug=True)
