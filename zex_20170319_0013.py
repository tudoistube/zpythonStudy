def out(**zdic):
    print(type(zdic))
    print(zdic.items())
    print(zdic.keys())
    tot=0
    for i in zdic.keys():
        print(i) #키
        print(zdic[i]) #값
        print(i, zdic[i])
        print('{0}={1}'.format(i, zdic[i]))
print('-------------------------')
out(kor=90, eng=80, mat=70)
print('===============')


