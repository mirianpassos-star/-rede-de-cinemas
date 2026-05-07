from dataclasses import dataclass
from datetime import datetime

@dataclass
class Filme:
    id: int
    titulo: str
    duracao_minutos: int

@dataclass
class Sala:
    id: int
    nome: str

@dataclass
class Sessao:
    id: int = None
    filme_id: int = None
    sala_id: int = None
    inicio: datetime = None
    fim: datetime = None
    preco: float = 0.0
