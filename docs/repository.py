import sqlite3
from datetime import datetime

class CinemaRepository:
    def __init__(self, db_name="cinema_sistema.db"):
        self.db_name = db_name
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_name) as conn:
            # Criação das tabelas baseadas nos RFs
            conn.execute("CREATE TABLE IF NOT EXISTS cinemas (id INTEGER PRIMARY KEY, nome TEXT, cidade TEXT, endereco TEXT)")
            conn.execute("CREATE TABLE IF NOT EXISTS salas (id INTEGER PRIMARY KEY, cinema_id INTEGER, identificacao TEXT, capacidade INTEGER)")
            conn.execute("CREATE TABLE IF NOT EXISTS filmes (id INTEGER PRIMARY KEY, titulo TEXT, genero TEXT, duracao INTEGER)")
            conn.execute("CREATE TABLE IF NOT EXISTS sessoes (id INTEGER PRIMARY KEY AUTOINCREMENT, filme_id INTEGER, sala_id INTEGER, inicio TIMESTAMP, fim TIMESTAMP, publico INTEGER DEFAULT 0)")

    def buscar_sessoes_por_sala(self, sala_id):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.execute("SELECT inicio, fim FROM sessoes WHERE sala_id = ?", (sala_id,))
            return [{"inicio": datetime.fromisoformat(row[0]), "fim": datetime.fromisoformat(row[1])} for row in cursor]

    def salvar_sessao(self, sessao):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.execute(
                "INSERT INTO sessoes (filme_id, sala_id, inicio, fim, publico) VALUES (?, ?, ?, ?, ?)",
                (sessao.filme_id, sessao.sala_id, sessao.inicio.isoformat(), sessao.fim.isoformat(), sessao.publico)
            )
            sessao.id = cursor.lastrowid
            return sessao

    def atualizar_publico(self, sessao_id, qtd):
        with sqlite3.connect(self.db_name) as conn:
            conn.execute("UPDATE sessoes SET publico = ? WHERE id = ?", (qtd, sessao_id))

    def relatorio_ocupacao(self):
        # RF04 e RF09 - SQL para calcular ocupação
        query = """
            SELECT f.titulo, s.publico, sa.capacidade, (CAST(s.publico AS FLOAT) / sa.capacidade) * 100 as ocupacao
            FROM sessoes s
            JOIN filmes f ON s.filme_id = f.id
            JOIN salas sa ON s.sala_id = sa.id
        """
        with sqlite3.connect(self.db_name) as conn:
            return conn.execute(query).fetchall()
