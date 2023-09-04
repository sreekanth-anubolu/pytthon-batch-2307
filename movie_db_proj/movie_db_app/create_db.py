


try:
    conn = PG_CONN.get_db_connection()
    schema = open("schema.sql").read()
    cur = conn.cursor()
    #cur.execute("CREATE DATABASE movie_db_proj;")
    #cur.close()
    #conn.commit()
    cur.execute(schema)
    conn.commit()
except Exception as e:
    print(f"Error while executing the schema {e}")
    conn.rollback()
finally:
    if conn:
        cur.close()
        conn.close()