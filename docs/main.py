from model import Filme, Sala
from repository import SessaoRepository
from service import SessaoService
from datetime import datetime

# Simulação da View e Controller
def cadastrar_sessao_fluxo():
    repo = SessaoRepository()
    service = SessaoService(repo)
    
    # Dados vindos da View
    filme = Filme(1, "Inception", 148)
    sala = Sala(1, "Sala IMAX")
    horario_inicio = datetime(2026, 5, 20, 14, 0) # 14:00
    
    try:
        sessao = service.agendar_sessao(filme, sala, horario_inicio, 35.00)
        print(f"Sucesso! Sessão {sessao.id} agendada.")
        print(f"Fim da sessão (com limpeza): {sessao.fim}")
    except ValueError as e:
        print(f"Erro de Negócio: {e}")

if __name__ == "__main__":
    cadastrar_sessao_fluxo()
