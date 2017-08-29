"""
#...복샘 참조 블로그 주소 : http://blog.naver.com/nasu0210/220586176179
import threading
import datetime

print(datetime) #<module 'datetime' from 'C:\\Users\\joywins\\AppData\\Local\\Programs\\Python\\Python36\\lib\\datetime.py'>
print(datetime.datetime)#<class 'datetime.datetime'>
print(datetime.datetime.now())#2017-08-29 19:09:48.392141
"""

"""
from datetime import *
print(datetime.now()) #2017-08-29 19:11:05.130067
print(datetime.day) #<attribute 'day' of 'datetime.date' objects>
print(date.today()) #2017-08-29
"""

"""
#...쓰레드1번째 예제 :
import threading
from datetime import *
def fun_a():
    print('실행시간: {}'.format(datetime.now()))

print('1번째 실행시간: {}'.format(datetime.now())) #1번째 실행시간: 2017-08-29 19:20:43.591830
#...10초 있다가 실행됨.
threading.Timer(10, fun_a).start() #실행시간: 2017-08-29 19:20:53.592569
"""

"""
#...쓰레드2번째 예제 :
import threading
count = 0
def fn_oneTimer():
    #...global 변수는 함수 안에서 전역변수화 시킴. 
    #   단, 변수선언은 함수 이전에 바깥에 선언되 있어야 함.
    global count
    count += 1
    print(count)
    timer = threading.Timer(1, fn_oneTimer)
    timer.start()
    if count == 10:
        print('stop...')
        timer.cancel()

print('start...')
fn_oneTimer()
"""

"""
#...쓰레드3번째 예제 : 쓰레드를 살려두되 count 가 10 보다 작으면 계속 출력함.
import threading
count = 0
def fn_oneTimer():
    #...함수 안에서 전역변수.
    global count
    count += 1
    print(count)
    if count < 10:
        timer = threading.Timer(1, fn_oneTimer)
        timer.start()

print('start...')
fn_oneTimer()
"""

"""
#...쓰레드4번째 예제 : global 을 쓰지 않고, Timer에서 매개변수를 전달하는 방식.
import threading

def fn_oneTimer(count):
    #...함수 안에서 전역변수.
    count += 1
    print(count)
    #...global 을 쓰지 않고, Timer에서 매개변수를 전달하는 방식.
    timer = threading.Timer(1, fn_oneTimer, args=[count])
    timer.start()
    if count == 10:
        print('stop...')
        timer.cancel()

print('start...')
fn_oneTimer(0)
"""