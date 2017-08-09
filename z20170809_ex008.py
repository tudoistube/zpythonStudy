import sqlite3
def delete_b():
    conn=sqlite3.connect("testdb.db")
    cur=conn.cursor()
    del_sql='delete from test where title=?'
    # ...튜플형태가 되기 위해 '중국사' 다음에 쉼표(,)를 써야함.
    cur.execute(del_sql,('중국사',))
    conn.commit()
    conn.close()

if __name__=="__main__":
    delete_b()