import psycopg2 

if __name__ == '__main__' :
    conn = psycopg2.connect(
            database = 'mpund',
            host = 'localhost',
            user = 'mpund_user',
            password = 'sekele'
            )

    curr = conn.cursor()

    curr.execute(""" CREATE TABLE mult4 (
            id  serial PRIMARY KEY,
            dater char(10),
            numr integer,
            numc integer
            )
            """)

    conn.commit()
    conn.close()
