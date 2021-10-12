# PokeApi App
Aplicação Django de integração com a API PokeAPI.<br><br>
Desenvolvido utlizando Python 3.8, Django 3.1.2, Django Rest Framework e Postgres 13.*<br><br>
Como é uma aplicação de teste, não houve inclusão de login para acessar a nossa API.

## Funcionamento
Após a configuração da aplicação, o usuário pode executar um comando seed para recarregar a base com os 20 primeiros pokemons retornados pela PokeApi.

Cada Pokemon pode ter vários Tipos.

Ao excluir um Pokemon, tanto via API como via Painel Admistrativo, nenhum dos seus tipos são afetados.

Já ao excluir um Tipo, todos os Pokemons associados serão excluídos.

*** A não ser que seja dito expressamente, os comandos seguintes devem ser executados a partir da pasta pokemon-app/pokemonapp ***.

*** A aplicação tem como configuração padrão o ambiente de desenvolvimento, sendo assim não é necessário passar o parâmetro ```settings```. ***

## Requisitos Básicos
 - Python 3.8
 - PostgreSQL 13

## Configurações necessárias
- No diretório ```settings```, deve ser criado um arquivo ```.env```, de acordo com o arquivo de exemplo ```.env.example```:
```
SECRET_KEY = '#-%))sevt%qw!rpa_m74=53bo0ryo_4t!vhe-a4&b)vhm1p(w#'
DB_NAME =database1234
DB_USER=user1234
DB_HOST=localhost
DB_PASSWORD=teste1234
ALLOWED_HOSTS=localhost,mysite.com
```

- Instalar os pacotes necessários para a execução do projeto:
```
pip3 install -r requirements.txt
```
- Migrar o banco de dados e criar usuário para o painel administrativo<br><br>
  ambiente desenvolvimento
    ```
    python3 manage.py migrate
    python3 manage.py createsuperuser --email admin@example.com --username admin
    ```
    ambiente produção

    ```
    python3 manage.py migrate --settings=pokemonapp.settings.production
    python3 manage.py createsuperuser --email admin@example.com --username admin --settings=pokemonapp.settings.production
    ```

- Excluir todos Pokemons<br><br>
    ambiente desenvolvimento
    ```
    python3 manage.py seed --mode=clear
    ```
    ambiente produção
    ```
    python3 manage.py seed --mode=clear --settings=pokemonapp.settings.production
    ```

- Incluir 20 Pokemons<br><br>
    ambiente desenvolvimento
    ```
    python3 manage.py seed --mode=refresh
    ```
    ambiente produção
    ```
    python3 manage.py seed --mode=refresh --settings=pokemonapp.settings.production
    ```
- Executar aplicação:
    ambiente desenvolvimento
    ```
    python3 manage.py runserver
    ```
    ambiente produção
    ```
    python3 manage.py runserver --settings=pokemonapp.settings.production
    ```
    
## Testes
Foram acrescentados testes apenas para verificacão do comportamento de deleção.
```
python3 manage.py test --settings=pokemonapp.settings.test
```
