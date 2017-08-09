#...http://cafe.naver.com/gubass/2087
import sqlite3
def update_b():
    conn=sqlite3.connect("testdb.db")
    cur=conn.cursor()
    up_sql='update test set title=? where title=?'
    #...한국사를 중국사로 변경함.
    cur.execute(up_sql,('중국사','한국사')) #...튜플형.
    conn.commit()
    conn.close()

if __name__=="__main__":
    update_b()