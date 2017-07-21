'''
#...Set 형 데이터.
#...45p. Set 형은 순서대로 저장되지 않음.

b={2,4,6,8}
print(b) #{8, 2, 4, 6}
'''

'''
#...Set 형은 중복을 제거함.
    Dictionary 에서 값을 제외한 키만 가진 데이터형이 Set 임.

b={1,2,1,1,1,2,1,1,1,2}
print(b) #{1, 2}
'''


'''
#...45p.
'''
dic={'경상도':{'부산','대구','울산','공통'}
      , '전라도':{'광주', '전주', '공통'}}

'''
...key 만 출력됨.
경상도
전라도

for i in dic:
    print(i)
'''

'''
Tuple 을 출력함.
('경상도', {'대구', '울산', '공통', '부산'})
('전라도', {'공통', '광주', '전주'})
for i in dic.items():
    print(i)
'''

'''
경상도
전라도

for i in dic.items():
    print(i[0])
'''

'''
{'공통', '울산', '부산', '대구'}
{'공통', '광주', '전주'}

for i in dic.items():
    print(i[1])
'''

'''
...Tuple 을 출력함.
경상도 ---|--- {'울산', '공통', '대구', '부산'}
전라도 ---|--- {'공통', '전주', '광주'}

for i,j in dic.items():
    print(i,'---|---',j)
'''

'''
전라도 ---|--- {'광주', '전주', '공통'}

for name, contents in dic.items():
    #print(name, '---|---', contents)
    if '광주' in contents:
        print(name, '---|---', contents)
'''

'''
전라도 ---|--- {'전주', '공통', '광주'}

for name, contents in dic.items():
    if '공통' in contents and not ('대구' in contents):
        print(name, '---|---', contents)
'''

'''
...46p.교집합 : '&'.

a={1,2,3}
b={2,3,4}
#print(a&b) # {2, 3}
print(a.intersection(b)) #길어서 잘안씀.
'''

'''
...46p.합집합 : '|'.
{1, 2, 3, 4}

a={1,2,3}
b={2,3,4}
print(a|b)
'''

'''
...46p.차집합 : '-'.
{1}

a={1,2,3}
b={2,3,4}
print(a-b)
'''

'''
...46p.대칭차집합 : '^'.
{1, 4}
'''
a={1,2,3}
b={2,3,4}
print(a^b)
