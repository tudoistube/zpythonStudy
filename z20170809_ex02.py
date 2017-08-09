#...http://blog.naver.com/nasu0210/220989492595
#from 폴더 import 클래스 또는 함수
from xml.etree.ElementTree import Element,dump,SubElement,ElementTree

person=Element('Person',time='14:03:00')
name=Element('name')
name.text='홍길동' #...위치 : 0번째.
person.append(name)

age=Element('age')
age.text='22'
person.append(age)

#...한줄로 요소를 생성하고 요소값까지 지정함.
SubElement(person,'adress').text='대구'

no=Element('no')
no.text='17'
person.insert(1,no)
#person.remove(no)
person.attrib['date']='2017-04-22'
#dump(person) #...콘솔로 출력됨.
ElementTree(person).write('C:\zpython\z20170809_ex03.xml') #...파일로 만들어짐.
#...만약 권한 문제로 실행되지 않으면, 파이썬IDLE를 관리자 권한으로 실행함.
