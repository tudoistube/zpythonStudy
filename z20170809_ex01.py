s = 'Hi, YouGoGirl'
s1 = '~'.join(s)
print(s1) #H~i~,~ ~Y~o~u~G~o~G~i~r~l

s2 = s.split('-')
print(s2) #['Hi, YouGoGirl'], List 형.
print(type(s2)) #<class 'list'>

s3 = s.isnumeric()
print(s3) #False

s4 = s.replace("Girl", "Boy")
print(s4) #Hi, YouGoBoy

s5 = s.startswith("Hi")
print(s5) #True

s6 = s.endswith("Girl")
print(s6) #True

s7 = s.count('G')
print(s7) #2

s8 = s.find('i')
print(s8) #1

s9 = s.isalnum() #...알파벳 또는 숫자인지.
s10 = s.isnumeric()
s11 = s.upper()
s12 = s.lower()

t = ' Hi, YouGoGirl      '
s13 = t.strip() #...공백제거.
print(s13)
s14 = t.lstrip()
print(s14)
s15 = t.rstrip()
print(s15)

#...스트링은 순서형자료(스트링, 튜플형, 리스트형)이므로 인덱스로 접근가능.
s16 = s[0]
print(s16) #H
#s[0] = "A"
print(s) #TypeError: 'str' object does not support item assignment
s17 = s.replace('o', 'i')
print(s17) #Hi, YiuGiGirl


#...리스트형 : 순서있고, 변경가능.
li = ['1', '2', '3', '3', '4', '5'] #...생성.
li2 = list('6789') #...생성2.
print(type(li))
li.remove('2')
print(li) #['1', '3', '4', '5']
li.extend(li2)
print(li) #['1', '3', '4', '5', '6', '7', '8', '9']
print(li.count('3')) #2
li.insert(1, '2')
print(li) #['1', '2', '3', '3', '4', '5', '6', '7', '8', '9']
li3 = [1,2,3,4,5]
p = li3.pop(2)
print(li3) #[1, 2, 4, 5]
print(p) #3

li3.reverse()
print(li3) #[5, 4, 2, 1]
li3.sort(reverse=True)
print(li3)