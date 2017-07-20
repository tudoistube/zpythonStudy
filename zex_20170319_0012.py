def meg(*ztuple):
    print(type(ztuple))
    #print(ztuple)

    re=''
    for i in ztuple:
        re+=i
        #print(re)
    return re
print('-------------------------')
k=meg('h', 'i', 'f', 'r', 'i', 'e', 'n', 'd')
print(k)
print('===============')


def meg(*ztuple):
    print(type(ztuple))
    #print(ztuple)
    tot=0
    for i in ztuple:
        tot+=i
        #print(re)
    return tot
print('-------------------------')
k=meg(1,2,3,4,5)
print(k)
print('===============')

def sum(*ztuple):
    print(type(ztuple))
    #print(ztuple)
    tot=0
    for i in ztuple:
        tot+=i
    return tot
print('-------------------------')
k=meg(1,2,3,4,5,6)
print(k)
print('===============')

def square(*ztuple):
    print(type(ztuple))
    #print(ztuple)
    tot=0
    for i in ztuple:
        tot+=(i*i)
    return tot
print('-------------------------')
k=square(1,2,3)
print(k)
print('===============')
