#...함수 안에서는 함수 밖에 있는 변수에 값을 할당할 수 없다.
#   어쩔수 없이 함수 밖에 있는 변수의 값을 할당할 경우에는
#   global 을 사용함.
name = '파이썬조아'
def rename(new_name):
    global name
    print("변경전 :", name) #변경전 : 파이썬조아
    name = new_name
    print("변경후 :", name) #변경후 : 마자마자

rename('마자마자')
print(name) #마자마자