#...http://cafe.naver.com/gubass/2086
import sqlite3
def select_b(number):
    conn=sqlite3.connect("testdb.db")
    cur=conn.cursor()
    #cur.execute('select * from test where title="한국사"')
    cur.execute('select * from test where pus="a"')
    print('[2] 일부 데이터 출력하기')
    rs=cur.fetchmany(number)
    for book in rs:
        print(book)
    conn.close()

if __name__=="__main__":
    #...select_b(n) 에서 n 은 조회할 데이터의 갯수임.
    #   현재 데이터에서 출판사가 "a" 인 데이터는 2개임.
    select_b(1)

