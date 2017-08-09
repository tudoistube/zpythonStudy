#...http://cafe.naver.com/gubass/2086
import sqlite3
def select_b():
    conn=sqlite3.connect("testdb.db")
    cur=conn.cursor()
    cur.execute('select * from test')
    print('[1] 전체 데이터 출력하기')

    rs=cur.fetchall()
    print(type(rs)) #...리스트이므로 슬라이스로 잘라낼 수 있음.
    print('--->',rs[2][1]) #...2016-02-02
    for book in rs:
        print(book)
    """
    ('개발자의 코드', '2017-08-09', 'a', 200, 0)
    ('클린코드', '2016-04-04', 'b', 300, 1)
    ('한국사', '2016-02-02', 'c', 330, 1)
    ('물리개론', '2015-01-04', 'a', 130, 0)
    ('건축학', '2013-10-14', 'e', 150, 0)
    """
    conn.close()


if __name__=="__main__":
    select_b()