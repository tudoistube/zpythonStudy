li=[]
li.append('1. 다음중 가장 느린 동물은?/1)거북이/2)굼벵이/3)지렁이/4)달팽이/4')
li.append('2. 다음중 가장 느린 동물은?/1)거북이/2)굼벵이/3)지렁이/4)달팽이/3')
li.append('3. 다음중 가장 느린 동물은?/1)거북이/2)굼벵이/3)지렁이/4)달팽이/2')
li.append('4. 다음중 가장 느린 동물은?/1)거북이/2)굼벵이/3)지렁이/4)달팽이/1')
li.append('5. 다음중 가장 느린 동물은?/1)거북이/2)굼벵이/3)지렁이/4)달팽이/3')
print('-------------------------')
tot=0
for i in li:
    sl=i.split('/') #[]로 되므로 list, 0부터 시작함.
    #print(type(sl))
    #print(sl)
    print(sl[0])
    print(sl[1])
    print(sl[2])
    print(sl[3])
    print(sl[4])
    #print("\n")
    a=input('\n 답?')

    if a==sl[5]:
        print('정답입니다.')
        tot=tot+20
    else :
        print('오답입니다.')
    print()

print('당신의 점수는',tot,'입니다.')
