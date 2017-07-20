def add(f, s):
    tot=0
    avg=0
    
    tot=f+s
    avg=tot/2

    if(avg >= 60):
        p='합격'
    else:
        p='다음기회에 도전'
    return tot, avg, p #튜플로 받음.

t, a, p = add(70, 80)
print(t, a, p)

