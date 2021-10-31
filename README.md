python default image

in de root:
de repo clonen
python -m venv env
env\Scripts\activate 

cd ninjagame-backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

DOCKER:
docker build --tag ninjagame-backend .
docker run --publish 8000:8000 ninjagame-backend

API CALLS:

VOOR FRONT-END:
register: http://127.0.0.1:8000/api/v1/auth/register/ username="USERNAME" password="PASSWORD" password2="PASSWORD"
get auth token/login: http://127.0.0.1:8000/api/v1/auth/token/ username="username" password="password"
	return: refresh & acces token
new auth token: http://127.0.0.1:8000/api/v1/auth/token/refresh/ refresh="REFRESH TOKEN"

add game: http://127.0.0.1:8000/api/v1/games/ "Authorization: Bearer {YOUR_TOKEN}" title="Ant Man and The Wasp" genre="Action" year=2018
get all games: http://127.0.0.1:8000/api/v1/games/ "Authorization: Bearer {YOUR_TOKEN}"

VOOR BACK-END:
update game score: http://127.0.0.1:8000/api/v1/game/{game_id}/ "Authorization: Bearer {YOUR_TOKEN}" score="SCORE"