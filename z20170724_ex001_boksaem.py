"""
def getMax(a, b):
    if a>b:
        return a
    else:
        return b

k = getMax(5, 7)
print(k)
"""
#...리스트 활용 정렬하기.
"""
def getMax(k):
    m=k[0]
    for i in k:
        if i>m: m=i
        #print(m)
    return m

def getMax2(k):
    k.sort()
    k.reverse()
    return k[0]

li=[3,2,5,4,1]
k=getMax2(li)
print(k)

#...최대값, 최소값 구하기1.
def getMax3(k):
    k.sort()
    k.reverse()
    m = []
    m.append(k[0]) #...Max.
    k.reverse()
    m.append(k[0]) #...min
    return m

li=[3,2,5,4,1]
m = getMax3(li)
for i in m:
    print(i)
"""

#...최대값, 최소값 구하기2.
def getMax4(k):
    m=k[0]
    mi=k[0]
    for i in k:
        if i>m: m=i
        if i<mi: mi=i
    return m, mi

li=[3,2,5,4,1]
m, mi = getMax4(li)
print(m, mi)
print(type((getMax4(li)))) #<class 'tuple'>
#print(type(m))
