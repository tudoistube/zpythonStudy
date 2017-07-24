q_list=[]   #빈 리스트 선언

q_list.append('문제1.다음중 제일 느린 동물은?/보기1)굼벵이/보기2)거북이/보기3)지렁이/보기4)달팽이/4')
q_list.append('문제2.세계에서 제일 많이 팔린 책은?/보기1)성경/보기2)영어책/보기3)수학/보기4)소설/1')
q_list.append('문제3.한국에서 제일 많이 팔린 책은?/보기1)수학의정석/보기2)운전면허시험책/보기3)교과서/보기4)영어/2')
q_list.append('문제4.캐나다의 수도는?/보기1)몬트리올/보기2)벤쿠버/보기3)오타와/보기4)캘거리/3')
q_list.append('문제5.구기종목에서 공이 제일 빠른것은?/보기1)농구/보기2)축구/보기3)배구/보기4)배드민턴/4')

#퀴즈정답: 4,1,2,3,4.
#print(len(quest))

tot=0
#leng=len(quest) #변수 따로 안 만들고, range()안에 넣어도 된다.

for i in q_list:
    ans=i.split('/')
    for j in range(len(q_list)):
        print(ans[j])
        
    '''
    print(ans[0])
    print(ans[1])
    print(ans[2])
    print(ans[3])
    print(ans[4])
   '''
    you_an=input('답은? \n')
    if you_an == ans[5]:
        print('정답입니다.')
        tot+=20
    else:
        print('오답입니다.')
    print() #공백출력
print('당신의 총점은', tot, '입니다.')