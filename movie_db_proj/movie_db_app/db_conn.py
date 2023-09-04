
import psycopg2


class PG_CONN:

    conn = None
    DB_NAME = "movie_db_proj"
    DB_USER = "postgres"
    DB_PASSWORD = "Aruba@123"
    DB_HOST = "127.0.0.1"
    DB_PORT = "5432"

    @classmethod
    def get_db_connection(cls):
        cls.conn = psycopg2.connect(dbname=cls.DB_NAME, user=cls.DB_USER, password=cls.DB_PASSWORD)
        return cls.conn
