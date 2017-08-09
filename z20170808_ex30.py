import json

d={'kor':90, 'eng':80, 'mat':88}

print(type(d))
print(d['eng'])

#...json 으로 읽을때는 dumps.
#...사전형데이터를 string 으로 바꿈 : 직렬화.
j = json.dumps(d)

print(j)
print(type(j))