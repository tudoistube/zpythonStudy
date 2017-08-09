"""
파이썬에서 utf-8 인코딩 파일 읽기.
http://hianna.tistory.com/290
"""
import codecs
#f=open('c:/pytest/z20170808_ex23_utf8.txt', 'r') #...rt : text 를 읽기 모드. r 도 가능함.
f = codecs.open('c:/pytest/z20170808_ex23_utf8.txt', 'r', 'utf-8')
#f=open('c:/pytest/z20170808_ex22.txt', 'r') #...rt : text 를 읽기 모드. r 도 가능함.
l = list(f)
"""
print(l) #['가나다\n', '라마바\n', '사아자\n']
print(l[0])
"""
print(l[:4])
for i in l[:4]:
    print(i, end='')