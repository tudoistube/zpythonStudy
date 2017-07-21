
"""
var1 = int(input('3+6=?'))

while var1 != 9:
    var1 = int(input('오답입니다. 3+6=?'))

print('정답입니다.')
"""
"""
var1 = int(input('0~100 사이의 점수를 입력하세요.'))

while ((var1 < 0) or (var1 >100)) :
    var1 = int(input('0~100 사이의 점수를 입력하세요.'))

print('정답입니다.')
"""

"""
var1 = input('주민번호 앞자리 6자리를 입력하세요.')

while len(var1)!=6:
    var1 = input('주민번호 앞자리 6자리를 입력하세요.')

print('정답입니다 :', var1)
"""

"""
a = [[1,2,3], [4,5,6], [7,8,9]]
for i in range(3):
    for j in range(3):
        print(a[i][j])
    
"""



#...49p.딕셔너리의 키 또는 값 얻기.

dic={'red':'빨강', 'blue':'파랑', 'green':'초록'}
var1 = input('color?')
"""
zkey = list(dic.keys())
zval = list(dic.values())
print(zkey)
print(zval)
print(dic[var1]) #키로 값구하기.

#...값으로 키구하기.
for i,j in dic.items():
    print(i) #빨강
    print(j) #red
    
#...방법1.    
for i in dic.values():
    if(i == var1) :
        print(i)
        
#...방법2.
for i,j in dic.items():
    if (j == var1):
        print(i)

"""

"""
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
