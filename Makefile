install:
	poetry install
	poetry add prompt
lint:
	poetry install
	poetry run flake8 brain_games
	