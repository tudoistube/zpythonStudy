# 파이썬의 집합 기능1
A = {1,2,3,4}
B = {3,4,5,6}

print(A)
print(B)

print(1 in A)
print(6 in A)
print(len(A))

print(A | B)
print(A & B)
print(A - B)

# 파이썬의 집합 기능2
C = {x for x in range(1, 11) }
# ...171p.1이상 11미만의 3의 배수를 원소를 하는 집합 D.
D = {x for x in range(1, 11) if x % 3 == 0 }

print(C)
print(D)

# ...171p.C 는 D 의 부분집합인가?
print(C<D)
# ...171p.D 는 C 의 부분집합인가?
print(C>D)
