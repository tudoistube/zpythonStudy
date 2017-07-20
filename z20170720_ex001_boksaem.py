print(2**64) #...#는 한줄 주석입니다.
print('\"\"\"은 여러줄 주석입니다.')
"""
print('파이썬프로그래밍')
print('파이썬프로그래밍')
"""
print('\'\'\'은 여러줄 주석입니다.')
'''
print('파이썬프로그래밍')
print('파이썬프로그래밍')
'''
#들여쓰기 : 4칸 띄워쓰기.

#input
'''
#age = input('나이를 입력하세요:')
age2 = int(input('나이를 입력하세요:'))
print(type(age2))
#if int(age) < 81 :
if age2 < 81:
    print('아직 괜찮아')
else:
    print('이제 쉬어가면서 ')
'''


#파이썬은 입력받는 자료형에 따라 자료형이 달라짐.
'''
age = input('나이를 입력하세요:')
age = int(input('나이를 입력하세요:'))
age = 5.2
age = 5
print(type(age2))
'''

#파이썬과 객체지향, 23p.
var1 = '파이썬과 객체지향'
var2 = '파이썬과 객체지향'
var3 = '파이썬 매력발산'
#주소값출력.
#컴파일러에 따라 같은 값은 주소도 같은 값으로 처리함.
print(id(var1))
print(id(var2))
print(id(var3))

#...30p.여러문장을 출력하기.
print('''여러줄
출력은
여러줄 주석처럼
쌍따옴표로 감싸기''')

"""
#...30p.문자열 길이 확인하기.
print(len('한글'))
print(len('ab'))

var1='재미있는 파이썬 공부'
var1.replace('파이썬 공부', 'Python Study')
print(var1)
print(var1.replace('파이썬 공부', 'Python Study'))
"""
#형변환.
a=10
b='10'
print(a+int(b))