d=[1,2,3,4,5]
print(type(d))
print(d[2])
print('===============')

d={'kor':80, 'eng':70, 'mat':60} #'키':값 으로 키에 홑따옴표로 감싸야 함.
print(type(d))
print(d['kor'])
print('===============')

def out(**vs):
    for i in vs.keys():
        print('{0}={1}, {2}'.format(i, vs[i], '별2개는 딕셔너리'))

out(kor=70, eng=80, mat=90)
print('===============')

def out(**vs):
    tot=0
    avg=0
    for i in vs.keys():
        tot+=vs[i]
    avg=tot/len(vs.keys())
    print('총점{0}, 평균{1}, {2}'.format(tot, round(avg,2), '별2개는 딕셔너리'))

out(kor=70, eng=80, mat=90)
print('===============')

def out(**vs):
    tot=0
    avg=0
    for i in vs.keys():
        tot+=vs[i]
    avg=tot/len(vs.keys())
    print('총점{0}, 평균{1}, {2}'.format(tot, round(avg,2), '별2개는 딕셔너리'))
    return tot, round(avg,2)

tot, avg = out(kor=70, eng=80, mat=90)
print('===============')
