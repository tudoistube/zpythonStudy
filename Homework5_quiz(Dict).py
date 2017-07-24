q_dict={ '문제1.다음중 제일 느린 동물은?/보기1)굼벵이/보기2)거북이/보기3)지렁이/보기4)달팽이':4,
        '문제2.세계에서 제일 많이 팔린 책은?/보기1)성경/보기2)영어책/보기3)수학/보기4)소설':1,
        '문제3.한국에서 제일 많이 팔린 책은?/보기1)수학의정석/보기2)운전면허시험책/보기3)교과서/보기4)영어':2,
        '문제4.캐나다의 수도는?/보기1)몬트리올/보기2)벤쿠버/보기3)오타와/보기4)캘거리':3,
        '문제5.구기종목에서 공이 제일 빠른것은?/보기1)농구/보기2)축구/보기3)배구/보기4)배드민턴':4 }

#딕셔너리의 key로, 리스트는 쓸 수 없다.(값이 바뀌기 때문에, 공간도 많이 차지함)
#딕셔너리의 value는 아무거나 사용가능.
#딕셔너리의 key로, 튜플은 쓸 수 있다.(값이 바뀌지 않음)
#print(type(q_dict)) #데이터형은 dict로 나옴.

tot=0
ans = list(q_dict.keys())

for j in range(len(ans)):   #배열크기 5만큼 반복함
    print(ans[j])       # print(type(ans))   #데이터형은 list
    you_an = input("답은?\n")
    if you_an == ans[j]:
        print("정답입니다.")
        tot += 20
    else:
        print('오답입니다')


print('\n당신의 총점은',tot,'입니다')


'''
배열로 바꾸어서, value 값을 입력한 답과 비교함

ans=list(q_dict.keys())
print(ans[0]) 
#print(type(ans))   #데이터형은 list
you_an=input("답은?\n")
if you_an==ans[0]:
    print("정답입니다.")
    tot+=20
else:
    print('오답입니다')



ans=list(q_dict.keys())
print(ans[1])  
you_an=input("답은?\n")
if you_an==ans[1]:
    print("정답입니다.")
    tot+=20
else:
    print('오답입니다')



ans=list(q_dict.keys())
print(ans[2])  
you_an=input("답은?\n")
if you_an==ans[2]:
    print("정답입니다.")
    tot+=20
else:
    print('오답입니다')
    
    
    
ans=list(q_dict.keys())
print(ans[3])  
you_an=input("답은?\n")
if you_an==ans[3]:
    print("정답입니다.")
    tot+=20
else:
    print('오답입니다')



ans=list(q_dict.keys())
print(ans[4])  
you_an=input("답은?\n")
if you_an==ans[4]:
    print("정답입니다.")
    tot+=20
else:
    print('오답입니다')


print('\n당신의 총점은',tot,'입니다')
'''



''' 
#처음에 생각해본 방법
j=list(q_dict.values()) 
print(j[1])
print(type(j))  #데이터형은 list
'''