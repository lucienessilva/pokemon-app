# pokemon-app
Aplicação Django de integração com a API PokéAPI.<br><br>
Desenvolvido utlizando Python 3.8 e Django 3.1.2<br><br>

## Requisitos
 - Python 3.8
 - PostgreSQL 9.6

## Configurações necessárias
- No diretório ```settings```, deve ser criado um arquivo ```.env```, de acordo com o arquivo de exemplo ```.env.example```:
```
SECRET_KEY = '#-%))sevt%qw!rpa_m74=53bo0ryo_4t!vhe-a4&b)vhm1p(w#'
DB_NAME =pokemon_db
DB_USER=pokemonapp_db_user
DB_HOST=localhost
DB_PASSWORD=teste1234
ALLOWED_HOSTS=localhost,mysite.com
```

- Instalar os pacotes necessários para execução do projeto:
```
pip3 install -r requirements.txt
```
## Executar
A aplicação tem como configuração padrão o ambiente de desenvolvimento, sendo assim não é necessário passar o parâmetro ```settings```.
### desenvolvimento
```
python3 manage.py runserver
```
### produção
```
python3 manage.py runserver --settings=pokemonapp.settings.production
```
## Testes
