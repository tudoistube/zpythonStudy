#...파이썬 파일 읽고 쓰기. http://cafe.naver.com/gubass/4349

#파일생성하기

f=open("파일명",'w')
"""
파일모드
r -> 읽기모드
w -> 쓰기모드
a -> 추가모드
"""

#파일닫기
f.close()

"""
파일에 값 출력하기
1번째
2번째
3번째
4번째
5번째
6번째
7번째
----------------------------------
"""

f=open('aaa.txt','w')
for i in range(1,8):
    f.write('%d번째 \n'%i)
f.close()

#readline()함수 이용하여 파일에 값 읽어오기
f=open('aaa.txt','r')
while True:
    line=f.readline()
    if not line:break
    print(line)
f.close()

#readlines()함수 이용하여 파일에 값 읽어오기

f=open('aaa.txt','r')

line=f.readlines()
for i in line:
    print(i)
f.close()

#read()함수 이용하여 파일에 값 읽어오기

f=open('aaa.txt','r')
line=f.read()
print(line)
f.close()