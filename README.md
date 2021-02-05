# Projeto SRALE - Sistema de Registro de Ano Letivo em Escolas
Este projeto é um sistema web desenvolvido usando Python com Django. Para rodar o projeto em sua máquina é necessária a instalação de algumas bibliotecas python, todas elas estão listadas nos arquivos "requirements-dev.txt" e "requirements.txt". Sendo que o requirements.txt é voltado para o servidor Heroku.

## Como rodar o projeto em sua máquina
* Faça o clone deste repositório usando o comando: git clone https://github.com/jorge-junio/SIGE.git
* Crie uma virtual env e ative ela
* Com a virtual env ativada instale as dependências usando o comando: pip install nomeDaDependencia
* Agora dentro da pasta do projeto rode o comando aeguir para gerar as migrations que serão usadas para gerar o banco de dados: python manage.py makemigrations
* Depois de gerar as migrations é hora de executá-las usando o comando: python manage.py migrate
* Agora o banco de dados já foi criado e só é necessário rodar a aplicação usando o comando: python manage.py runserver

## Como rodar o projeto em sua máquina