# 1. Levantamento de Requisitos e Regras de Negócio
### Requisitos Funcionais (RF)
- RF01 - Manter Filmes: O sistema deve permitir o cadastro de filmes com título, gênero, diretor, elenco e duração.

- RF02 - Manter Sessões: O sistema deve permitir criar sessões vinculando um filme a uma sala em um horário específico.

- RF03 - Registrar Público: O sistema deve permitir o registro da quantidade de espectadores presentes em cada sessão realizada.

- RF04 - Totalização de Público: O sistema deve gerar relatórios de público total por filme e por unidade de cinema.

- RF05 - Manter Unidades de Cinema: O sistema deve permitir o cadastro de unidades físicas (complexos), contendo nome, cidade e endereço.

- RF06 - Manter Salas: O sistema deve permitir o cadastro de salas para cada cinema, definindo identificação e capacidade de assentos.

- RF07 - Consulta de Programação: O sistema deve listar os filmes em cartaz e seus respectivos horários filtrados por unidade.

-  RF08 - Manter Elenco e Diretores: O sistema deve permitir o cadastro detalhado de profissionais (atores/diretores) para compor a ficha técnica dos filmes.

-   RF09 - Relatório de Ocupação: O sistema deve calcular a porcentagem de ocupação das salas com base no público registrado e na capacidade total.

- RF10 - Filtro por Gênero: O sistema deve permitir a busca e filtragem de sessões baseadas no gênero do filme (Ação, Drama, Terror, etc.).
### Requisitos Não Funcionais (RNF)
- RNF01 - Persistência: O sistema deve utilizar o banco de dados SQLite para garantir a persistência dos dados de forma local e leve.

- RNF02 - Arquitetura: O desenvolvimento deve seguir o padrão MVC (Model-View-Controller) com as camadas Service e Repository para separação de responsabilidades.

- RNF03 - Desempenho: A geração de relatórios de totalização não deve exceder o tempo de 2 segundos de processamento.

- RNF04 - Confiabilidade: O sistema deve garantir que dados de sessões passadas não sejam alterados após o fechamento do relatório diário.

- RNF05 - Portabilidade: O sistema deve ser executável em ambientes Windows e Linux sem necessidade de alteração no código-fonte.

- RNF06 - Integridade: O sistema deve validar que nenhuma sessão seja criada sem um filme ou sala previamente existentes.

- RNF07 - Usabilidade: A interface deve ser projetada para que o registro de público de uma sessão seja concluído em menos de 1 minuto.

- RNF08 - Escalabilidade: A modelagem do banco de dados deve suportar o crescimento do número de salas e cinemas sem perda de performance.

- RNF09 - Padronização: O código deve seguir as diretrizes de estilo da linguagem (PEP 8 para Python) para facilitar a manutenção.

- RNF10 - Segurança: O sistema deve exigir autenticação para acesso às funcionalidades de gerenciamento e relatórios financeiros.
