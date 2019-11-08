import psycopg2

if __name__ == '__main__' :
    conn = psycopg2.connect(
            database = 'mpund',
            host = 'localhost',
            user = 'mpund_user',
            password = 'sekele'
            )

    curr = conn.cursor()

    curr.execute(""" CREATE TABLE pesa_compte_24 (
            id serial PRIMARY KEY,
            chmp24 char(8),
            comptet integer,
            sommmet integer
            )
            """)

    conn.commit()
    conn.close()



