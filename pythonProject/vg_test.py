import psycopg2
import sqlite3
import datetime


int_ref_num = 0
ext_ref_num = 0
vltn_dt = None
new_inc1 = 0
#new_inc_dt1 = None
#new_inc_date1 = None

connection = psycopg2.connect(user="user",
                              password="password",
                              host="localhost",
                              port="5432",
                              database="RushTest")
cursor = connection.cursor()
new_inc_dt1 = "select vltn_dt from arch14_incr.if_capital_valuation where ext_ref_num = '" + str(int_ref_num) + ("' order by "
                                                                                                           "vltn_dt")
Query1 = "select *  from arch14_incr.account_dtls where int_ref_num = '" + str(int_ref_num) + "'"
while new_inc_date1:
        new_inc_date1 = new_inc1.str(vltn_dt)
datetime.datetime.now().isoformat()

#cursor.execute(new_inc_date1)
#records = cursor.fetchall()
cursor.executemany(new_inc_dt1)
print(new_inc_date1)