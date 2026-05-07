from flask import Flask, request, jsonify
from model import Filme, Sala
from repository import CinemaRepository
from service import CinemaService
from datetime import datetime

app = Flask(__name__)
repo = CinemaRepository()
service = CinemaService(repo)

@app.route('/sessao', methods=['POST'])
def post_sessao():
    data = request.json
    try:
        # RF02 e RF06 - Mock de objetos para exemplo
        filme = Filme(id=data['filme_id'], titulo="Exemplo", genero="Ação", duracao_minutos=120)
        sala = Sala(id=data['sala_id'], cinema_id=1, identificacao="Sala 01", capacidade=100)
        inicio = datetime.fromisoformat(data['inicio'])
        
        sessao = service.criar_sessao(filme, sala, inicio)
        return jsonify({"status": "sucesso", "sessao_id": sessao.id}), 201
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400

@app.route('/relatorio/ocupacao', methods=['GET'])
def get_ocupacao():
    # RF09 e RF04
    dados = repo.relatorio_ocupacao()
    return jsonify(dados)

if __name__ == "__main__":
    app.run(debug=True)
