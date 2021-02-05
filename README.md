# Projeto SRALE - Sistema de Registro de Ano Letivo em Escolas
Este projeto é um sistema web desenvolvido usando Python com Django. O mesmo conta com o cadastro de Escolas, Turmas, Disciplinas, Professores, Alunos, e Habilidades. Para rodar o projeto em sua máquina é necessária a instalação de algumas bibliotecas python, todas elas estão listadas nos arquivos "requirements-dev.txt" e "requirements.txt". Sendo que o requirements.txt é voltado para o servidor Heroku.

## Como rodar o projeto em sua máquina
* Faça o clone deste repositório usando o comando: git clone https://github.com/jorge-junio/SIGE.git
* Crie uma virtual env e ative ela
* Com a virtual env ativada instale as dependências usando o comando: pip install nomeDaDependencia
* Agora dentro da pasta do projeto rode o comando aeguir para gerar as migrations que serão usadas para gerar o banco de dados: python manage.py makemigrations
* Depois de gerar as migrations é hora de executá-las usando o comando: python manage.py migrate
* Agora o banco de dados já foi criado e só é necessário rodar a aplicação usando o comando: python manage.py runserver

## Banco de dados
O banco de dados contém 10 tabelas. Sendo elas: Escola, Turma, Aluno, Disciplina, Professor, Habilidade, Matricula, Ministra, Promove, e Contem. As 6 primeiras tabelas são tabelas primarias e as 4 restantes são tabelas que representam relações entre as outras 6 tabelas.
* Matricula - representa a relação entre as tabelas Turma e Aluno
* Ministra - representa a relação entre as tabelas Professor e Disciplina
* Promove - representa a relação entre as tabelas Disciplina e Habilidade
* Contem - representa a relação entre as tabelas Turma e Disciplina

As 4 tabelas listadas acima surgiram após a palicação das 5 formas de normalização de dados.

## A aplicação
O sistema é simples, sem login e nem autenticação. O usuário tem acesso a um Menu na parte superior da página com as seguintes opções:
* Escola
* Turma
* Aluno
* Professor
* Disciplina
* Habilidades
* Matriculas
* Discipinas em turmas
* Habilidades em disciplinas
* Ministragem

Em cada uma das opções acima o usuário pode selecionar "Cadastrar" ou "Listar", sendo que ao escolher listar é possível editar ou excluir itens já cadastrados na lista. Ou seja, o usuário pode inserir, excluir, editar, listar, e até mesmo buscar pelo id em cada tabela já citada. E além disso, na listagem de disciplinas é possível ver quais as Habilidades necessárias para passar em uma disciplina clicando no botão ciano com o ícone de lista no lado direito de cada disciplina. 

## Problemas e dificuldades encontradas
No momento de fazer o deploy do código para o servidor ocorreu um problema. Ao rodar o "migrate" no servidor para gerar o banco de dados, por algum motivo desconhecido o servidor não está gerando as tabelas que têm referência a outra tabela, e devido a isso algumas das funcionalidades comentadas acima não estão funcionando no servidor.

* Link da aplicação rodando no servidor Heroku: https://srale.herokuapp.com/
