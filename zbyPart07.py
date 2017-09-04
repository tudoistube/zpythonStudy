"""
zList = ['월', '화', '수', '목', '금']
for i in zList :
    print(i, end=' ') #월 화 수 목 금
"""

"""
for i in ['월', '화', '수', '목', '금'] :
    print(i, end=' ') #월 화 수 목 금
"""

"""
zList = ['월', '화', '수', '목', '금']
for i in range(5):
    n = zList[i]
    print('{}번 : {}'.format(i, n))
"""

"""
zList = ['월', '화', '수', '목', '금']
for i in range(len(zList)):
    n = zList[i]
    print('{}번 : {}'.format(i, n))
"""

"""
zList = ['월', '화', '수', '목', '금']
for i, name in enumerate(zList):
    print('{}번 : {}'.format(i, name))
"""

zList = ['월', '화', '수', '목', '금']
for a in enumerate(zList):
    print('{}번 : {}'.format(a[0], a[1]))

"""
print(chr(44032)) #가
print(chr(44032 + 11172 - 1)) #힣
for i in range(11172) :
    print(chr(44032 + i), end='') #가....힣
"""
