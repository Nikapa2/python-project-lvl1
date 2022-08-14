install: #установка зависимостей
	poetry install
	poetry add prompt

brain-games: #запуск игры
	poetry run brain-games

brain-even: #чётные числа 1 игра
	poetry run brain-even

brain-calc: #калькулятор 2 игра
	poetry run brain-calc

brain-gcd: # НОД 3 игра
	poetry run brain-gcd

brain-progression: #прогрессия 4 игра 
	poetry run brain-progression

brain-prime: # простое число 5 игра
	poetry run brain-prime

build: #сборка
	poetry build

publish: #публикация без добавления в индекс
	poetry publish --dry-run

package-install: #установка сборки
	python3 -m pip install --user dist/hexlet_code-0.1.0-py3-none-any.whl

lint: #тесты
	poetry run flake8 brain_games

