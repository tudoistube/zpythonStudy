#...http://cafe.naver.com/gubass/2084
import sqlite3

def create_table():
    conn=sqlite3.connect("testdb.db")
    cur=conn.cursor()
    cur.execute('''
    create table test(title text,
    pubd text,
    pus text,
    page integer,
    re integer)
    ''')
    conn.commit()
    conn.close()


#...자바 스프링처럼 파이썬은 어떻게 자동으로 처리할지 궁금해진다.
def create_table2():
    conn = sqlite3.connect('my_db')
    cur = conn.cursor() #...DB의 포인터 개념.
    cur.execute('''create table my_books(
        title text,
        published_date text,
        publisher text,
        pages integer,
        recommendation integer)
    ''')

    conn.commit()
    conn.close()



#...만약, 이 파일이 main 으로 쓰일때, 함수를 호출함.
#   다른 파일에서 호출될 때는 "__sub__" 임.
if __name__ == "__main__":
    create_table() #...실행하면 my_db 가 프로젝트 탐색창에 생성됨.


