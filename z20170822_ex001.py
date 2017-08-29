"""
#...list.
li=[(1,2), (3,4), (5,6)]
for i in li:
    for j in i:
        print(j)
"""
"""
#...dictionary.
dic={"a":"A", "b":"B", "c":"C"}
for i in dic.values():
    print(i)
"""

"""
#...set.
#...frozen set 은 읽기만 가능함.
s={1, 2, 3, 4, 5}
s1={2, 3, 7}
s.discard(1)
print(s) #{2, 3, 4, 5}
#print(s | s1)  #{1, 2, 3, 4, 5, 7} #...합집합.
#print(s & s1) #{2, 3} #...교집합.
#print(s - s1) #{1, 4, 5} #...차집합.
#print(s ^ s1) #{1, 4, 5, 7} #...대칭차집합.

fs = frozenset(s)
print(fs) #frozenset({2, 3, 4, 5})
for i in fs :
    print(i) #2 3 4 5
"""

print("안녕")