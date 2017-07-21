"""
#...47p.Dictonary 형 데이터 : 키로 접근함.

dic={'kor':80, 'eng':90, 'mat':77}
print(type(dic)) #<class 'dict'>
#...45p.dic 을 set 에 넣으면 키만 들어감.
a=set(dic)
print(type(a)) #<class 'set'>
print(a) #{'eng', 'mat', 'kor'}
"""

"""
#...47p.다른객체를 딕셔너리로 변환함.
...List 를 Dict 로 변환(Tuple 형태도 동일함).

li=[['a','b'], ['c','d'], ['e','g']]
print(dict(li)) #{'a': 'b', 'c': 'd', 'e': 'g'}

li=['ab','cd','ef']
print(dict(li)) #{'a': 'b', 'c': 'd', 'e': 'f'}
"""

"""
#...47p.딕셔너리에 새로운 값 추가하기.
...Dic 는 값이 순차적으로 나오지 않음.

dic={'kor':80, 'eng':90, 'mat':86}
dic['tot'] = 256 #...새로운 항목 추가함.
print(dic) #{'kor': 80, 'eng': 90, 'mat': 86, 'tot': 256}
"""

"""
#...47p.딕셔너리 결합하기.

dic={'kor':80, 'eng':90, 'mat':86}
dic2={'kor2':88, 'eng2':99, 'mat2':88}
dic.update(dic2)
print(dic) #{'kor': 80, 'eng': 90, 'mat': 86, 'kor2': 88, 'eng2': 99, 'mat2': 88}
"""

"""
#...48p.딕셔너리 삭제하기.

dic={'kor':80, 'eng':90, 'mat':86}
del dic['mat']
print(dic) #{'kor': 80, 'eng': 90}
dic.clear() #전체삭제.
print(dic) #{}
"""

"""
#...48p.딕셔너리 존재유무 확인하기.

dic={'kor':80, 'eng':90, 'mat':86}
print('kor' in dic) #True
"""

"""
#...48p.딕셔너리에 없는 키로 접근하면 에러발생함.
print(dic['tot'])
"C:\Program Files\Anaconda3\python.exe" E:/WS_Python/z20170721_ex003_boksaem.py
Traceback (most recent call last):
  File "E:/WS_Python/z20170721_ex003_boksaem.py", line 62, in <module>
    print(dic['tot'])
KeyError: 'tot'

dic={'kor':80, 'eng':90, 'mat':86}
print(dic['kor']) #80
print(dic.get('tot')) #...오류발생안함: None
print(dic.get('mat', 'tot')) #...오류발생안함: None 86
"""

"""
#...49p.딕셔너리의 키 또는 값 얻기.

dic={'kor':80, 'eng':90, 'mat':86}
#...List or Tuple 로 변환해서 얻기.
#...키얻기.
k = list(dic.keys())
print(k) #['kor', 'eng', 'mat']
print(k[1]) #eng
#...값얻기.
k = list(dic.values())
print(k) #[80, 90, 86]
print(k[1]) #90

#...값얻기.
dic={'kor':80, 'eng':90, 'mat':86}
k = list(dic.items()) #...49p.모든 순서쌍 얻기.
print(k) #[('kor', 80), ('eng', 90), ('mat', 86)]
print(k[1]) #('eng', 90)
print(k[1][0]) #eng
print(k[1][0][1]) #n
print(k[1][1]) #90
"""

"""
#...49p.딕셔너리의 할당과 복사.
"""
#...딕셔너리 할당.
dic={'kor':80, 'eng':90, 'mat':88}
dic2 = dic
print(dic2) #{'kor': 80, 'eng': 90, 'mat': 88}
dic['tot']=258
print(dic) #{'kor': 80, 'eng': 90, 'mat': 88, 'tot': 258}
print(dic2) #{'kor': 80, 'eng': 90, 'mat': 88, 'tot': 258}
#...copy() 를 이용해 복사할 수 있음.
dic={'kor':80, 'eng':90, 'mat':88}
dic2=dic.copy()
dic['tot']=258
print(dic) #{'kor': 80, 'eng': 90, 'mat': 88, 'tot': 258}
print(dic2) #{'kor': 80, 'eng': 90, 'mat': 88}
