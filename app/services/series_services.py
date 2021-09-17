import psycopg2
from psycopg2 import sql
from app.services.configs import configs
from app.exc.exc import IdNotFound


def create_table():
    conn = psycopg2.connect(**configs)
    cur = conn.cursor()

    query = sql.SQL(
        """
        CREATE TABLE IF NOT EXISTS ka_series(
            id BIGSERIAL PRIMARY KEY,
            serie VARCHAR(100) NOT NULL UNIQUE,
            seasons INTEGER NOT NULL,
            released_date DATE NOT NULL,
            genre VARCHAR(50) NOT NULL,
            imdb_rating FLOAT NOT NULl
        );
        """
    )
    cur.execute(query)
    conn.commit()
    cur.close()
    conn.close()


class Series():
    def __init__(
            self, serie, seasons, released_date, genre, imdb_rating
            ) -> None:
        self.serie = serie.title()
        self.seasons = seasons
        self.released_date = released_date
        self.genre = genre.title()
        self.imdb_rating = imdb_rating

    def save(self):
        create_table()

        conn = psycopg2.connect(**configs)
        cur = conn.cursor()

        keys = [
            "id", "serie", "seasons", "released_date", "genre", "imdb_rating"
        ]
        columns = [sql.Identifier(key) for key in self.__dict__.keys()]
        values = [sql.Literal(value) for value in self.__dict__.values()]

        query = sql.SQL(
            """
                INSERT INTO
                    ka_series (id, {columns})
                VALUES
                    (DEFAULT, {values})
                RETURNING *;
            """
        ).format(
            columns=sql.SQL(',').join(columns),
            values=sql.SQL(',').join(values)
        )

        cur.execute(query)
        fetch_result = cur.fetchone()

        conn.commit()
        cur.close()
        conn.close()

        serialized_data = dict(zip(keys, fetch_result))

        return serialized_data

    def get_all():
        conn = psycopg2.connect(**configs)
        cur = conn.cursor()

        columns = [
            "id", "serie", "seasons", "released_date", "genre", "imdb_rating"
        ]

        cur.execute(""" SELECT * FROM ka_series; """)

        fetch_result = cur.fetchall()

        conn.commit()
        cur.close()
        conn.close()

        serialized_data = [
            dict(zip(columns, serie_data)) for serie_data in fetch_result
        ]

        return {"data": serialized_data}

    def get_by_id(series_id: int):

        conn = psycopg2.connect(**configs)
        cur = conn.cursor()

        columns = [
            "id", "serie", "seasons", "released_date", "genre", "imdb_rating"
        ]

        cur.execute(
            """
                SELECT
                    *
                FROM
                    ka_series
                WHERE
                    id=(%s);
            """, (series_id, ))

        fetch_result = cur.fetchone()

        if not fetch_result:
            raise IdNotFound("Not found.")

        conn.commit()
        cur.close()
        conn.close()

        serialized_data = {"data": dict(zip(columns, fetch_result))}

        return serialized_data
