# Sistema de Gestão Escolar
## Objetivo
Criar um sistema de gestão escolar (customizado), para oferecer a um administrador e/ou professor a opção de adicionar e remover alunos, lançar frequência, gerar relatórios de frequência, adicionar eventos & documentos dos eventos escolares.

## Principais features:
- Cadastrar e remover alunos
- Adicionar datas de aulas, datas de feriados e datas sem aula
- Adicionar sistema de controle de frequência de alunos
- Adicionar atividade/evento, descrição do evento, lista de presença assinada, documentos e fotos do evento

## Tecnologias
### _Backend_
- Flask
- SQLAlchemy
- PostgreSQL
- Python
### _Frontend_
- React
- Material UI
- Typescript
### Infraestrutura
- Docker

## Membros e papéis
- Daniel: Frontend
- Fábio: Backend
- Misael: Backend
- Thiago: Frontend


## Arquitetura do sistema: Hexagonal
- Por que o sistema está adotando essa arquitetura?
  - A arquitetura adotada permite implementar a parte principal do sitema, independente da tecnologia utilizada.
    Dessa maneira, a lógica do negócio, como criar e editar alunos, adicionar faltas, adicionar eventos, etc, pode ser
    implementada de forma independente.
- Quais são as portas e adaptadores? Qual o objetivo deles?
  - As portas de saída estão implementadas usando uma interface em Python, que é implementada pelo adaptador de banco de dados. Dessa maneira, a lógica do negócio não precisa saber qual banco de dados está sendo utilizado.
  - As portas de entrada estão implementadas usando uma classe Controller, que encapsula o acesso dos serviços pelo adaptador do frontend.
  - O adaptador do backend implementa a interface (porta de saída). Ele é responsável por acessar o banco de dados e retornar os dados para o controller.
  - O adaptador do frontend implementa a API utilizada para comunicar com o frontend. Ele é responsável por receber os dados do frontend e repassar para o controller. Também é responsável por receber os dados do controller e repassar para o frontend.

- TODO: Pode-se dar pequenos exemplos de código e diagramas
  - Exemplo de código:
    - Controller
    ```python
    class AlunoController:
      def __init__(self, aluno_repository: AlunoRepository):
        self.aluno_repository = aluno_repository

      def cadastrar_aluno(self, nome: str, email: str, telefone: str):
        aluno = Aluno(nome=nome, email=email, telefone=telefone)
        self.aluno_repository.cadastrar_aluno(aluno)
    ```
    - Repositório
    ```python
    class AlunoRepository:
      def __init__(self, db: Database):
        self.db = db

      def cadastrar_aluno(self, aluno: Aluno):
        self.db.add(aluno)
        self.db.commit()
    ```
    - Adaptador do backend
    ```python
    class AlunoAdapter:
      def __init__(self, aluno_controller: AlunoController):
        self.aluno_controller = aluno_controller

      def cadastrar_aluno(self, nome: str, email: str, telefone: str):
        self.aluno_controller.cadastrar_aluno(nome, email, telefone)
    ```
    - Adaptador do frontend
    ```python
    class AlunoAdapter:
      def __init__(self, aluno_controller: AlunoController):
        self.aluno_controller = aluno_controller

      def cadastrar_aluno(self, nome: str, email: str, telefone: str):
        self.aluno_controller.cadastrar_aluno(nome, email, telefone)
    ```

## Backlog do Produto
<details>
<summary>Clique aqui para expandir</summary>

1. Como professor, eu gostaria de cadastrar um aluno
2. Como professor, eu gostaria de atualizar a informação de um aluno ou removê-lo
3. Como professor, eu gostaria de adicionar o período letivo ao sistema
4. Como professor, eu gostaria de adicionar datas de feriado no calendário letivo
5. Como professor, eu gostaria de adicionar datas em que não haverá aulas (avulsa, de última hora)
6. Como professor, gostaria de lançar presença e faltas de alunos em uma determinada turma
7. Como professor, gostaria de acompanhar a frequência e infrequência dos meus alunos
8. Como professor, gostaria de adicionar documentos para justificar a ausência de um aluno
9. Como professor, gostaria de acessar um relatório para saber os principais motivos de ausência dos alunos
10. Como professor, gostaria de adicionar um evento no calendário
11. Como professor, gostaria de adicionar documentos e fotos de um evento
12. Como professor, gostaria de fazer o download das fotos e documentos de um evento
13. Como professor, gostaria de logar no sistema de gestão escolar
</details>


## Backlog da Sprint
<details>
<summary>Clique aqui para expandir</summary>

#### História #1: Configuração de ambiente
- Tarefas e responsáveis:
  - Iniciar projeto Django [Misael]
  - Configurar PostgreSQL [Fábio]
  - Configurar Django Rest framework [Misael]
  - Iniciar o projeto em React [Thiago, Daniel]

#### História #2: Como professor, eu gostaria de cadastrar um aluno
- Tarefas e responsáveis: 
  - Criar tabelas relacionadas ao aluno [Misael]
  - Criar API de cadastro do aluno [Misael]
  - Criar telas de cadastro do aluno [Daniel]
  - Integrar as telas com o backend [Daniel]

#### História #3: Como professor, eu gostaria de atualizar a informação de um aluno ou removê-lo
- Tarefas e responsáveis:
  - Criar API de edição e deleção do aluno [Misael]
  - Criar telas de editar aluno [Daniel]
  - Integrar as telas com o backend [Daniel]

#### História #4: Como professor, eu gostaria de adicionar um evento no calendário
- Tarefas e responsáveis: 
  - Criar tabelas relacionadas ao evento [Fábio]
  - Criar API de cadastro de evento [Fábio]
  - Criar telas de cadastro do evento [Daniel]
  - Integrar as telas com o backend [Daniel]

#### História #5: Como professor, eu gostaria de adicionar documentos e fotos de um evento
- Tarefas e responsáveis:
  - Criar estrutura para salvar fotos e documentos no servidor [Misael]
  - Criar API de cadastro de fotos e documentos [Misael]
  - Criar telas de cadastro de fotos e documentos [Daniel]
  - Integrar as telas com o backend [Daniel]

#### História #6: Como professor, eu gostaria de adicionar datas em que não haverá aulas (avulsa, de última hora)
- Tarefas e responsáveis: 
  - Criar tabelas relacionados ao calendário letivo [Fábio]
  - Criar APIs para adicionar datas especiais [Fábio]
  - Criar interfaces no calendário para adicionar datas especiais [Thiago]
  - Integrar tela do calendário com o backend [Thiago]

#### História #7: Como professor, eu gostaria de lançar presença e faltas de alunos em uma determinada turma
- Tarefas e responsáveis:
  - Criar APIs para lançar faltas de alunos [Fábio]
  - Criar interfaces no calendário para adicionar faltas [Thiago]
  - Integrar tela do calendário com o backend [Thiago]

#### História #8: Como professor, eu gostaria de adicionar o período letivo ao sistema
- Tarefas e responsáveis: 
  - Criar tabelas relacionados ao período letivo [Misael]
  - Criar APIs para adicionar adicionar período letivo [Misael]
  - Criar interfaces no calendário para adicionar período letivo [Thiago]
  - Integrar tela do calendário com o backend [Thiago]

</details>
