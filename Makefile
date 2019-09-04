install:
	poetry install
	poetry add prompt
lint:
	poetry run flake8 brain_games
	