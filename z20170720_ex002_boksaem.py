'''
#...36p.List 데이터타입 생성방법: 1. 대괄호[]사용. 2.list()사용.
em=[]
em2=list()
em3=list('리스트는문자열을글자하나하나로분리함')
print(em3)
#['리', '스', '트', '는', '문', '자', '열', '을', '글', '자', '하', '나', '하', '나', '로', '분', '리', '함']

#...36p.tuple 데이터타입 생성방법: 1.소괄호()사용.
tup=('a','b','c')
print(tup) #('a', 'b', 'c')
#...36p.tuple을 List로 변환함.
m=list(tup)
print(m) #['a', 'b', 'c']

day='2017-07-20'
k=day.split('-')
print(day) #2017-07-20
print(k) #['2017', '07', '20']
print(k[0]) #2017
print(k[1]) #07

#...37p.인덱스로 List 접근하기.
li=['a','b','c','d','e']
print(li[0]) #a
print(li[1]) #b
print(li[-1]) #e, 끝에서 읽어옴.
print(li[-2]) #d, 끝에서 읽어옴.

#...37p.리스트 항목 바꾸기.
li=['a','b','c','d','e']
li[1] = 'bb'
print(li) #['a', 'bb', 'c', 'd', 'e']

#...37p.리스트 슬라이스 다루기.
li=['a','b','c','d','e']
#...리스트[0:n] : n-1 까지 선택함. 0, 1, 2 중 n -1 까지 출력하기.
print(li[0:2])
#['a', 'b']
#...왼쪽부터 처음부터 2칸씩 선택.
print(li[::2]) #['a', 'c', 'e']
#...오른쪽부터 처음부터 1칸씩 선택.
print(li[::-1]) #['e', 'd', 'c', 'b', 'a']
#...오른쪽부터 처음부터 2칸씩 선택.
print(li[::-2]) #['e', 'c', 'a']

#...37p.리스트 슬라이스 다루기.
li=['a','b','c','d','e']
li.append('마지막에추가') #추가.
print(li)
li2=['g','h']
li.extend(li2) #리스트병합.방법1.
print(li)
li3=['i', 'j']
li+=li3 #리스트병합.방법1.
print(li)
li.insert(1, '중간에n번째에추가') #리스트 중간에 추가.
print(li)
del li[1] #인덱스를 이용하여 리스트 중간에 삭제
print(li)
li.remove('a') #값을 이용하여 리스트 중간에 삭제
print(li)
li.append('x') #추가.
li.append('x') #추가.
print(li)
li.remove('x') #값을 이용하여 리스트 중간에 삭제
print(li)
li.remove('x') #값을 이용하여 리스트 중간에 삭제
print(li)
li.insert(0,'a') #추가.
print(li)
#pop(index) : 항목을 뽑아내고 삭제하기.
k=li.pop(2)
print(k)
print(li)
#값으로 항목 index 찾기.
print(li.index('e'))
#in : 존재여부 확인하기.
print('a' in li) #Ture : 존재함.
print('s' in li) #False : 존재하지 않음.


li=[1,2,1,1,2,3,2,1,1]
#...37p.특정값 갯수 세기.
print(li.count(3))

li=['a','b','c','d','e','f']
#...39p.문자열 변환하기.
print(','.join(li))
li=['a','b','c','d','e','f']
print('-'.join(li))
li=['a','b','c','d','e','f']
print(''.join(li))

#...40p.정렬하기.
li=['f','b','e','d','c','a']
li.sort() #li가 정렬됨.
print(li)
li.sort(reverse=True) #li가 역순으로 정렬됨.
print(li)

li=['f','b','e','d','c','a']
a=sorted(li) #정렬한복사본을 다른 변수에 넘기고 원본을 보관할 필요가 있을때는 sorted()
print(li)
print(a)

print(len(li)) #항목갯수얻기.

li=['a','b','c','d','e','f']
li2=li #li, li2 가 주소값이 같음.
print(li)
print(li2)
li[0] = 'changed' #같은 주소값이므로 li, li2 모두 바뀜.
print(li)
print(li2)
'''
zorigin=['a','b','c','d','e','f']
b = zorigin.copy() #복사해서 생성하기 : 방법1.copy().
c = list(zorigin) #방법2.list()
d = zorigin[:] #방법3.
print(b)
print(c)
print(d)
zorigin[0]='변화를줌'
print(zorigin)
print(b)
print(c)
print(d)







