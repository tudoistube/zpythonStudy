#...http://cafe.naver.com/gubass/2085
import sqlite3
def insert_b():
    conn=sqlite3.connect("testdb.db")
    cur=conn.cursor()
    #...데이터 추가.1번째 방법.
    cur.execute("insert into test values('개발자의 코드','2017-08-09','a',200,0)")

    #...데이터 추가.2번째 방법.PreparedStatement.
    ins_sql='insert into test values(?,?,?,?,?)'
    cur.execute(ins_sql,('클린코드','2016-04-04','b',300,1)) #...튜플형.

    #...데이터 추가.3번재 방법.리스트 안에 튜플을 담고 있는 형태로 책3권을 한번에 생성함.
    #...요건 맘에 든다.
    books=[ ('한국사','2016-02-02','c',330,1),('물리개론','2015-01-04','a',130,0),
            ('건축학','2013-10-14','e',150,0)]
    cur.executemany(ins_sql,books) #...여러건을 처리함.

    conn.commit()
    conn.close()

if __name__=="__main__":
    insert_b()