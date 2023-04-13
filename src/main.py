import os

from dotenv import load_dotenv

from src.functions import get_repos_stats
from src.postgres_db import PostgresDB

load_dotenv()

db_config = {
    'user': os.getenv('POSTGRES_USER'),
    'password': os.getenv('POSTGRES_PASSWORD'),
    'host': os.getenv('POSTGRES_HOST'),
    'port': os.getenv('POSTGRES_PORT'),
    'dbname': os.getenv('POSTGRES_DB')
}


def main():
    data = get_repos_stats('skypro-008')
    db = PostgresDB(**db_config)
    db.insert_data(data)

    for item in db.get_data(5, 'forks'):
        print(item)

    db.export_to_json()


if __name__ == '__main__':
    main()
