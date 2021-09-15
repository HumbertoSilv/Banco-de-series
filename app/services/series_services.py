import psycopg2
from psycopg2 import sql
from app.services.configs import configs


def create_table():
    conn = psycopg2.connect(**configs)

    cur = conn.cursor()

    query = sql.SQL(
        """
        CREATE TABLE IF NOT EXISTS ka_series(
            id BIGSERIAL PRIMARY KEY,
            serie VARCHAR(100) NOT NULL UNIQUE,
            seasons INTEGER NOT NULL,
            released_data DATE NOT NULL,
            genre VARCHAR(50) NOT NULL,
            imbd_rating FLOAT NOT NULl
        );
        """
    )
    cur.execute(query)


class Series():
    def __init__(self) -> None:
        pass
