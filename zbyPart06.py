"""
#...format() :
num = 20
greet = '안녕'
place = '문자열 포맷의 세계'
welcome = ' 환영해^^'

#...format() 을 사용하지 않는 경우 :
print(num, '번 손님,', greet, '! ', place, '에 온걸 ', welcome, '!')

#...format() 을 사용하는 경우 :
base = '{}번 손님, {}! {}에 온걸 {}!' #...{} 의 갯수와 format() 안의 변수의 갯수가 같아야 함.
format_exp = base.format(num, greet, place, welcome) #...format() 앞에 마침표(.)가 있어야 문자열과 연결됨.
print(base)
print(format_exp)
"""

"""
#...여러줄의 문자열을 표현할 때는 따옾표 3개로 둘러쌈.
long_str = '''와 여러줄이
되서 좋아요!!!'''
print(long_str)
#...따옴표 3개를 사용하면 여러개의 문자열을 쉽게 표현할 수 있음.
quote2 = '''가끔은 '와 "를 모두 쓸 때 따옴표 3개는 참 편리해'''
print(quote2)
"""

"""
div1 = 8 / 5 #...나눗셈.
div2 = 8 // 5 #...몫.
div3 = 8 % 5 #...나머지.
"""
print('가위바위보 중 하나를 입력하세요>', end='')#...print문 출력후 한칸 띄우지 않기.
ans = input()
print('가위바위보 : ', ans)