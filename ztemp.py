"""
http://blog.naver.com/nasu0210/220804358762
{'이름':'홍길동','나이':22,'국어':77,'영어':88,'수학':90}
{'이름':'김철수','나이':32,'국어':87,'영어':67,'수학':30}
{'이름':'이영희','나이':29,'국어':100,'영어':70,'수학':84}
{'이름':'김민우','나이':11,'국어':100,'영어':90,'수학':89}
{'이름':'문서영','나이':13,'국어':95,'영어':97,'수학':92}
"""
s = list()
s.append({'이름': '홍길동', '나이': 22, '국어': 77, '영어': 88, '수학': 90})
s.append({'이름': '김철수', '나이': 32, '국어': 87, '영어': 67, '수학': 30})
s.append({'이름': '이영희', '나이': 29, '국어': 100, '영어': 70, '수학': 84})
s.append({'이름': '김민우', '나이': 11, '국어': 100, '영어': 90, '수학': 89})
# print(s)



"""
cnt = 0
for i in s:
    cnt = cnt +1
    z = cnt -1
    #print(i, cnt)
    #print(type(i), i, i['이름'])
    if(i['이름']=='이영희'):
        total = i['국어'] + i['영어'] + i['수학']
        avg = int(total/3)
        print('총점 : ', total, '평균 : ', avg)

tot = 0
for i in range(len(s)):
    #print(i)
    tot = tot + s[i]['나이']
print('나이 합계 = ', tot)

"""
min = 0
for i in s:
    # print(i, cnt)
    # print(type(i), i, i['이름'])
    # print(type(i['국어']))
    print(i['국어'], i['영어'], i['수학'])
    if (i['국어'] > i['영어']):
        min = i['영어']
        i['최소과목'] = '영어'
    elif (i['영어'] > i['수학']):
        min = i['수학']
        i['최소과목'] = '수학'
    else:
        min = i['국어']
        i['최소과목'] = '국어'
    i['최소과목점수'] = min

zmin = {}
zmin['이름'] = s[0]['이름']
print('시작이름', zmin)
min = 0
for i in s:
    # print('for :' , i)
    if (i['국어'] > i['영어']):
        min = i['영어']
        zmin['이름'] = min
        i['최소과목'] = '영어'
    elif (i['영어'] > i['수학']):
        min = i['수학']
        i['최소과목'] = '수학'
    else:
        min = i['국어']
        # zmin.append({'이름': '홍길동', '나이': 22, '국어': 77, '영어': 88, '수학': 90})

"""


        i['최소과목'] = '국어'
    i['최소과목점수'] = min


    total = i['국어'] + i['영어'] + i['수학']
    avg = int(total/3)
    print('총점 : ', total, '평균 : ', avg)

"""

# ...성별이 '여'인 사람 삭제하기.
for i in s:
    if (i['성별'] == '여'):
        s.remove(i)
print(s)