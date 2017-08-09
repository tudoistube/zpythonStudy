#자동으로 닫힘.
with open('c:/pytest/z20170808_ex24.txt', 'r') as f:
    l = f.readlines()
#print(l)

for i in l:
    print(i, end='')

print(f.closed)