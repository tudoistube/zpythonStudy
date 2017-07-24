'''
'문제1.다음중 제일 느린 동물은?/보기1)굼벵이/보기2)거북이/보기3)지렁이/보기4)달팽이/4',
'문제2.세계에서 제일 많이 팔린 책은?/보기1)성경/보기2)영어책/보기3)수학/보기4)소설/1',
'문제3.한국에서 제일 많이 팔린 책은?/보기1)수학의정석/보기2)운전면허시험책/보기3)교과서/보기4)영어/2',
'문제4.캐나다의 수도는? / 보기1)몬트리올 / 보기2)벤쿠버 / 보기3)오타와 / 보기4)캘거리/3',
'문제5.구기종목에서 공이 제일 빠른것은?/보기1)농구/보기2)축구/보기3)배구/보기4)배드민턴/4'
'''
tot=0

set1 = {'문제1.다음중 제일 느린 동물은?/보기1)굼벵이/보기2)거북이/보기3)지렁이/보기4)달팽이'}
ans1 = {'4'}
# print(list(s1)[0], end='') #줄바꿈 막고.

list1 = list(set1) #set형을 list형으로 바꿈
print(list1[0]) #문제출력함
your_ans1 = set(input('답은?'))#입력한 int를 set형으로 변환

if your_ans1 == ans1:
    print('정답입니다.')
    tot+=20
else:
    print('오답입니다.')
    print() #공백출력



set2 = {'문제2.세계에서 제일 많이 팔린 책은?/보기1)성경/보기2)영어책/보기3)수학/보기4)소설'}
ans2 = {'1'}
list2 = list(set2)
print(list2[0])
your_ans2 = set(input('답은?'))
if your_ans2 == ans2:
    print('정답입니다.')
    tot+=20
else:
    print('오답입니다.')
    print()



set3 = {'문제3.한국에서 제일 많이 팔린 책은?/보기1)수학의정석/보기2)운전면허시험책/보기3)교과서/보기4)영어'}
ans3 = {'2'}
list3 = list(set3)
print(list3[0])
your_ans3 = set(input('답은?'))
if your_ans3 == ans3:
    print('정답입니다.')
    tot+=20
else:
    print('오답입니다.')
    print()


set4 = {'문제4.캐나다의 수도는? / 보기1)몬트리올 / 보기2)벤쿠버 / 보기3)오타와 / 보기4)캘거리'}
ans4 = {'3'}
list4 = list(set4)
print(list4[0])
your_ans4 = set(input('답은?'))
if your_ans4 == ans4:
    print('정답입니다.')
    tot+=20
else:
    print('오답입니다.')
    print()



set5 = {'문제5.구기종목에서 공이 제일 빠른것은?/보기1)농구/보기2)축구/보기3)배구/보기4)배드민턴'}
ans5 = {'4'}
list5 = list(set5)
print(list5[0])
your_ans5 = set(input('답은?'))
if your_ans5 == ans5:
    print('정답입니다.')
    tot+=20
else:
    print('오답입니다.')
    print()


print('당신의 총점은', tot, '입니다.')