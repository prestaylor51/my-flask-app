Important scripts
Write dependencies to requirements
    pip freeze > requirements.txt

Install requirements
    pip install -r requirements

Run app
    flask run

Create .env file with the following env vars
    DATABASE_URL

for local create a postgresql user with password

connect to localhost:3000/

Start front end with npm run start





EC2 Ubuntu

install postgresql
    sudo apt update
    sudo apt install postgresql postgresql-contrib

login to postgres
    sudo -u postgres psql

install npm 
    sudo apt install nodejs npm

install flask
    sudo apt install python3-venv
    Run inside repo root -> create and select venv to use
        python3 -m venv venv
        source venv/bin/activate
    Install flask
        pip install Flask
        Use 'flask run' in root to run backend
    Install additional needed lib (some are not included on reqirements. My dependency skills are lacking)

Create .env file with following vars
    DATABASE_URL=<url>

Set up postgresql
    login (se above)
    run sql file with
        \i <path to sql>
    
    Set password for postgres to 'postgres'


Systemd
    /etc/systemd/system/secret-santa/secret-santa.service


Run backend
    'flask run'
Run frontend
    'npm i'
    'npm run start'
