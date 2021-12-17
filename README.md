## NinjaGame-Backend
This is the back-end web server for my school project.

### Docker
```
docker build --tag ninjagame-backend .
```
```
docker run --publish 8000:8000 ninjagame-backend
```

### Dev setup
##### clone this repo
##### Setup a python virtual enviroment
```
python -m venv env
```
##### Activate the enviroment
```
env\Scripts\activate
```
##### Change to the ninjagame-backend directory
```
cd ninjagame-backend
```
##### Install requirements
```
pip install -r requirements.txt
```
##### Migrate the database
```
python manage.py migrate
```
##### Run the development server
```
python manage.py runserver
```

### API CALLS:

register: http://127.0.0.1:8000/auth/register/ username="USERNAME" password="PASSWORD" password2="PASSWORD"

get token: http://127.0.0.1:8000/auth/token/ username="username" password="password"
	return: refresh & acces token

refresh token: http://127.0.0.1:8000/auth/token/refresh/ refresh="REFRESH TOKEN"

add game: http://127.0.0.1:8000/games/ "Authorization: Bearer {YOUR_TOKEN}" title="Ant Man and The Wasp" genre="Action" year=2018

get all games: http://127.0.0.1:8000/games/ "Authorization: Bearer {YOUR_TOKEN}"

update game score: http://127.0.0.1:8000/game/{game_id}/ "Authorization: Bearer {YOUR_TOKEN}" score="SCORE"