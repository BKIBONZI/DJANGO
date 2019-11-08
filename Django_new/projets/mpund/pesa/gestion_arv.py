import psycopg2 

if __name__ == '__main__' :
    conn = psycopg2.connect(
            database = 'mpund',
            host = 'localhost',
            user = 'mpund_user',
            password = 'sekele'
            )

    curr = conn.cursor()

 


    conn.commit()
    conn.close()
