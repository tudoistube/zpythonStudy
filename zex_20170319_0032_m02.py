from zex_20170319_0032 import *


li = list()

while True :
    s=int(input('(1.입력 2.전체출력 3.종료 :)'))
    
    if s == 1 :
        li.append(Person())
        
    elif s == 2 :
        li[0].dispTitle()
        for i in li :
            #i.disp()
            i.dispItem()
            
    elif s == 3 :
        break
    
    else :
        print('1 ~ 3 까지만 입력가능합니다.')
        
print('프로그램을 종료합니다.')
    
print('===============')

