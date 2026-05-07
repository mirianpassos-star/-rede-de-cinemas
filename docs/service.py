from datetime import datetime, timedelta

class CinemaService:
    def __init__(self, repository):
        self.repo = repository
        self.MINUTOS_LIMPEZA = 20 # RN02

    def criar_sessao(self, filme, sala, inicio):
        # RN07: Sessões Retroativas
        if inicio < datetime.now():
            raise ValueError("Não é permitido cadastrar sessões no passado.")

        # RN04: Cálculo de Término
        fim = inicio + timedelta(minutes=filme.duracao_minutos)
        
        # RN01 e RN02: Choque de Horários e Limpeza
        sessoes = self.repo.buscar_sessoes_por_sala(sala.id)
        for s in sessoes:
            bloqueio_inicio = s['inicio'] - timedelta(minutes=self.MINUTOS_LIMPEZA)
            bloqueio_fim = s['fim'] + timedelta(minutes=self.MINUTOS_LIMPEZA)
            
            if (inicio < bloqueio_fim) and (fim > bloqueio_inicio):
                raise ValueError("Conflito de horário ou intervalo de limpeza insuficiente.")

        from model import Sessao
        nova_sessao = Sessao(filme_id=filme.id, sala_id=sala.id, inicio=inicio, fim=fim)
        return self.repo.salvar_sessao(nova_sessao)

    def registrar_publico(self, sessao_id, qtd_espectadores, capacidade_sala):
        # RN03: Limite de Capacidade
        if qtd_espectadores > capacidade_sala:
            raise ValueError(f"Público excede a capacidade da sala ({capacidade_sala}).")
        
        self.repo.atualizar_publico(sessao_id, qtd_espectadores)
