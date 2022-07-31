install: #установка зависимостей
	poetry install
brain-games: #запуск игры
	poetry run brain-games
build: #сборка
	poetry build
publish: #публикация без добавления в индекс
	poetry publish --dry-run
package-install: #установка сборки
	python3 -m pip install --user dist/hexlet_code-0.1.0-py3-none-any.whl

