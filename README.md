# Github user repo stats to Postgres

Цель проекта заключается в сборе статистики по репозиториям заданного пользователя на Github и сохранении ее в базу данных Postgres.

## Установка и использование

Для работы программы необходимо установить зависимости, указанные в файле `requirements.txt`

```
pip install -r requirements.txt
```

Для работы с базой данных необходимо создать файл `.env` с параметрами доступа к базе данных PostgresSQL. Пример содержимого файла:

```
POSTGRES_HOST=localhost
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
POSTGRES_PORT=5432
POSTGRES_DB=postgres

```

## Описание файлов



- `main.py` содержит функцию `main`, которая запускает цепочку действий по сбору статистики по репозиториям на Github и записи ее в базу данных PostgresSQL.



- `functions.py` содержит функцию `get_repos_stats`, которая собирает статистику по репозиториям заданного пользователя на Github.



- `postgres_db.py` содержит класс `PostgresDB`, который позволяет работать с базой данных PostgresSQL.