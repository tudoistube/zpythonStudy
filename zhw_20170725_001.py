"""
#...반평균보다 작은 사람들의 이름을 구하기.
"""
#...리스트형.
li=[
     {'이름':'홍길동','나이':22,' 성별':'여','국어':77, '영어':88,'수학':90}
   , {'이름':'김철수','나이':32,' 성별':'남','국어':87, '영어':67,'수학':30}
   , {'이름':'이영희','나이':29,' 성별':'여','국어':100,'영어':70,'수학':84}
   , {'이름':'김민우','나이':11,' 성별':'남','국어':100,'영어':15,'수학':89}
   , {'이름':'문서영','나이':13,' 성별':'남','국어':95, '영어':97,'수학':92}
   ]


"""
#...함수 안쓰고 구하기.
tot = 0
avg = 0.0
#print(type(li))  #...<class 'list'>
for i in li :
    #print(type(i))  #...<class 'dict'>
    #...tot, avg 요소 추가.
    i['tot'] = i['국어']+i['영어']+i['수학']
    i['avg'] = round((i['국어']+i['영어']+i['수학']) /3, 1)
    tot += i['tot']

avg = round((tot / 3 / len(li)), 1)

print('전체총점 : ', tot, ' 전체평균 : ', avg)
print('')
print('평균보다 작은 사람')

for i in li:
    if avg > i['avg'] :
        print('이름 : ', i['이름'], ' | 평균 : ', i['avg'])

"""

"""
#...함수 만들어서 구하기.
"""
tot = 0
avg = 0.00
def getTotal(p_li):
    _tot = 0
    for i in p_li:
        # print(type(i))  #...<class 'dict'>
        # ...tot, avg 요소 추가.
        i['tot'] = i['국어'] + i['영어'] + i['수학']
        i['avg'] = round((i['국어'] + i['영어'] + i['수학']) / 3, 1)
        _tot += i['tot']
    print('전체총점 : ', _tot)
    return _tot

def getAvg(p_tot, p_li):
    _avg = 0.00
    _avg = round((p_tot / 3 / len(p_li)), 2)
    print('전체평균 : ', _avg) #...해결과제 : C 언어처럼 %.2f 사용해서 서식으로 반올림값 표현하기.
    return _avg


tot = getTotal(li)
avg = getAvg(tot, li)

#...해결과제 : 별도 파일에서 입력값 모듈로 불러와서 클래스로 만들기.