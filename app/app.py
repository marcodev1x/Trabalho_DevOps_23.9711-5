from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

# Configuração do Banco de Dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://devops_user:devops_password@db:3306/devops'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo de Dados
class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    ra = db.Column(db.String(20), unique=True, nullable=False)

    def to_dict(self):
        return {"id": self.id, "nome": self.nome, "ra": self.ra}

# Rota de cadastro de alunos
@app.route('/alunos', methods=['GET'])
def get_alunos():
    alunos = Aluno.query.all()
    return jsonify([aluno.to_dict() for aluno in alunos])

@app.route('/alunos', methods=['POST'])
def add_aluno():
    data = request.get_json()
    if not data or not data.get('nome') or not data.get('ra'):
        return jsonify({"error": "Dados inválidos!"}), 400

    novo_aluno = Aluno(nome=data['nome'], ra=data['ra'])
    try:
        db.session.add(novo_aluno)
        db.session.commit()
        return jsonify(novo_aluno.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Erro ao salvar aluno. RA já existente?"}), 400

# Configuração para rodar antes da primeira requisição
@app.before_first_request
def setup_database():
    db.create_all()

# Criar um aluno automaticamente durante o inicialização
@app.before_first_request
def create_random_student():
    random_ra = str(random.randint(100000, 999999))
    aluno = Aluno(nome="Aluno Teste", ra=random_ra)
    db.session.add(aluno)
    db.session.commit()
    print(f"Aluno {aluno.nome} com RA {aluno.ra} criado.")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
