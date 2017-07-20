a = 80
if a >= 60 :
    print('합격')
else :
    print('불합격')
    print('===============')
"""
80 이상 합격

"""
a = 80
if a >= 80 :
    print('합격')
elif a >= 60 :
    print('보류')
else :
    print('불합격')
    print('===============')
"""
90 이상 수
80 이상 우
70 이상 미
60 이상 양
60 미만 가
"""
a = int(input('점수를 입력하시오. :'))
if a >= 90 :
    print('수')
elif a >= 80 :
    print('우')
elif a >= 80 :
    print('미')
elif a >= 80 :
    print('양')
else :
    print('가')
    print('===============')
"""
이월드 요금계산
종류(종일권, 야간권)
구분(소인, 대인)

종일권  소인 32,000
          대인 40,000
야간권  소인 20,000
          대인 28,000
"""
time = int(input('종류(종일권:1, 야간권:2)를 입력하시오. :'))
age = int(input('구분(대인:1, 소인:2)를 입력하시오. :'))
cost = int() #초기화함. c=0 과 같음.
if time == 1 :
    #pass #나중에 기술하겠다는 것을 의미함. 비워놓으면 안됨.
    if age == 1 :
        cost=40000
    else :
        cost=32000
else :
    if age == 1 :
        cost=28000
    else :
        cost=20000
print('요금 : ' + str(cost) + '원')
print('===============')


















