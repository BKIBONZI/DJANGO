import psycopg2 
from Mpund.pesa.models import Arriveesc

if __name__ == '__main__' :
    conn = psycopg2.connect(
            database = 'mpund',
            host = 'localhost',
            user = 'mpund_user',
            password = 'sekele'
            )

    curr = conn.cursor()

    for arr in Arriveesc.objects.all() :
        liste_arr = [arr.arv1c]
        liste_arr.sort()
        print(liste_arr)


    conn.commit()
    conn.close()
