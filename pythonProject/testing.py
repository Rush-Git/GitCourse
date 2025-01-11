import psycopg2
from psycopg2 import sql
from psycopg2._psycopg import cursor

con = psycopg2.connect("dbname=RushTest host=localhost  user=user password=password port=5432")
cur = con.cursor()

int_ref_num = None
int_ref_numarr = ["12062024"]

for n in int_ref_numarr:
    int_ref_num = n
    delete_daily_pos = "delete from test1_pp_daily_pos_attributes where int_ref_num = '" + str(int_ref_num) + "'"
    cur.execute(delete_daily_pos)





