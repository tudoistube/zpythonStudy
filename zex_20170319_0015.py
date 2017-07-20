def a():
    a=7
    return a

#print(a())
res = a()
print(res)
print('===============')

def a(k):
    r=7 + k
    return r

#print(a(8))
res = a(8)
print(res)
print('===============')

def a():
    k=7
    return k

def b(k):
    s=k+10
    print(s)
    return s
    
#print(a(8))
res = a()
res = b(res)
print(res)
print('===============')
