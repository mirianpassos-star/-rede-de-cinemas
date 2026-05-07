
# Diagrama de Casos de Uso (Visão Geral)
### Cinema

- RF05

- idCinema

- nome

- cidade

- endereco

- cadastrarUnidade()

- listarSalas()

- gerarRelatorioPorUnidade()

---

### Sala

- RF06

- idSala

- identificacao

- capacidade

- tipoTela

- verificarDisponibilidade()

- alterarCapacidade()

---

### Filme

- RF01, RF08

- idFilme

- titulo

- duracaoMinutos

- genero

- diretor

- elenco

- classificacaoIndicativa

- cadastrarFilme()

- consultarFichaTecnica()

---

### Sessao

- RF02, RF04

- idSessao

- dataHora

- precoIngresso

- publicoAtual

- status

- abrirSessao()

- encerrarSessao()

- calcularHorarioTermino()

- validarChoqueHorario()

---

### RegistroPublico

- RF03, RF09

- idRegistro

- dataLancamento
  
-  quantidadeEspectadores

- registrarEntrada(qtd: int)

- estornarPublico(qtd: int)

- validarLotacao()

---

### Funcionario

- RF03

- idFuncionario

- nome

- matricula

- fazerLogin()

- registrarPublicoSessao()

---

### Administrador

- RF01, RF02, RF04, RF05, RF06

- idAdmin

- nome

- nivelAcesso

- configurarProgramacao()

- gerarRelatorioGeral()

- manterCadastroFilmes()

---

### Relatorio

- RF04, RF09

- idRelatorio

- dataGeracao

- tipo

- conteudo

- exportarPDF()

- totalizarPublico()

---

### Genero

- RF10

- idGenero

- descricao

- filtrarFilmes()

---

### Localizacao

- RF05, RF07

- idLocalizacao

- latitude

- longitude

- bairro

- calcularDistancia()

- buscarCinemasProximos()
