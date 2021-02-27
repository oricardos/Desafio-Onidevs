# Desafio-Onidevs
A empresa MusicOni Ltda é uma empresa fictícia de distribuição de música
digital que está entrando para o mercado. Para ser bem-sucedida, esta empresa
precisa de um sistema interno bem estruturado, que atenda às suas demandas, e às de
seus artistas. Para isto, o CEO Oten Noslen contratou um programador, com o seguinte
problema: “Tenho vários artistas em minha empresa. Cada um desses artistas pode ter
várias músicas, e mensalmente, eu preciso recolher um relatório com todas estas
músicas de cada artista, para uma análise de crescimento. Preciso que este sistema
seja o mais automatizado possível, e disponível em uma página web.”

![alt text](https://github.com/oricardos/Desafio-Onidevs/blob/master/media/screenshot2.png)
###### Tela Inicial do Projeto

## 🚀 Tecnologias Utilizadas
- Python 3.9
- Django 3.1
- Django-Cripsy-Forms 1.1

## Como Executar
- Acesse a pasta do projeto através do Terminal
- Crie um Ambiente Virtual na raiz do projeto com o seguinte comando: `python3 -m venv venv`
- Ative o Ambiente Virtual `cd venv\Scripts\` e insira o comando `activate`. Certifique-se de executar com o cmd
- Uma vez ativada, volte a raiz do projeto e instale o Django com o seguinte comando `pip install django`
- É necessário instalar também o Crispy Forms com o comando `pip install django-crispy-forms`
- Crie o banco de dados com: `python manage.py makemigrations` e depois `python manage.py migrate`
- Crie um superuser para ter acesso ao admin com `python manage.py createsuperuser` com nome e senha ( email não é necessário)
- Pra finalizar, vamos rodar o servidor com `python manage.py runserver`.
- O Projeto está pronto para uso! 😁




## Funcionamento do Projeto
### Login Admin
Em seu navegador, vá até: [localhost:8000/admin](http://localhost:8000/admin)
Para acessar, basta inserir as informações que você criou no `python manage.py createsuperuser`


![alt text](https://github.com/oricardos/Desafio-Onidevs/blob/master/media/login-admin.gif)

### Cadastrar Artistas
Após logar, basta clicar em ```Artists >> ADD ARTIST +``` e adicionar o artista desejado.

![alt text](https://github.com/oricardos/Desafio-Onidevs/blob/master/media/cadastrar-artista.gif)

### Cadastrar Música
Na página inicial [localhost:8000](http://localhost:8000), basta clicar em ``` Adicionar Nova Música ``` e inserir todas as informações.

![alt text](https://github.com/oricardos/Desafio-Onidevs/blob/master/media/cadastrar-musica.gif)

### Editar Música
É possível também editar as informações das músicas através do link na parte direita da tabela.

![alt text](https://github.com/oricardos/Desafio-Onidevs/blob/master/media/Editar.gif)

### Excluir Música
Caso queira excluir uma música, basta acessar ```Editar Música >> Deletar ```

![alt text](https://github.com/oricardos/Desafio-Onidevs/blob/master/media/excluir.gif)

