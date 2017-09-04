"""
import datetime
znow = datetime.datetime.now()
print(znow) #2017-09-04 12:30:06.341107
"""

"""
import datetime
startTime = datetime.datetime.now()
print(type(startTime)) #<class 'datetime.datetime'>
#...datetime.replace() 메서드는 자신을 바꾸는게 아니고
#   새로운 datetime 인스턴스를 만들어서 반환함.
#   그러나, 원하는 시각이 저장된 datetime 인스턴스를 얻기 위해
#   now 로 현재 시각을 받아온 다음 다시 replace() 로 바꾸는
#   과정은 꽤 번거롭고, replace 의 목적은 이런 목적으로 만든
#   메서드가 아님.
changedTime = startTime.replace(year=2018, month=3, day=1)
print(startTime) #2017-09-04 13:33:42.811547
print(changedTime) #2018-03-01 13:33:42.811547
"""

"""
import datetime
startTime2 = datetime.datetime(2018, 3, 1)
print(startTime2) #2018-03-01 00:00:00
howLong = startTime2 - datetime.datetime.now()
print(type(howLong)) #<class 'datetime.timedelta'>
#...class 'datetime.timedelta' 는 days 와 seconds 로
#   시간을 계산할 수 있음.
print(howLong.days) #177
print(howLong.seconds) #37188
print("2018.3.1 까지는 {}일{}시간이 남았습니다.".format(howLong.days, howLong.seconds))
#2018.3.1 까지는 177일37129시간이 남았습니다.
"""

"""
import datetime
def days_until_christmas():
    christmas_2030 = datetime.datetime(2030, 12, 25)
    days = (christmas_2030 - datetime.datetime.now()).days
    return days

print("{}일".format(days_until_christmas())) #4859일
"""

import datetime
print(datetime.datetime.now()) #2017-09-04 15:28:02.003553

hundredPlus = datetime.timedelta(days=100)
zdaysAfter100 = datetime.datetime.now() + hundredPlus

print(zdaysAfter100) #2017-12-13 15:27:22.756847

hundredMinus = datetime.timedelta(days=-100)
zdaysBefore100 = datetime.datetime.now() + hundredMinus
print(zdaysBefore100) #2017-05-27 15:31:04.322105

#...오늘 9시부터 1일 뒤의 시간과 날짜를 구함.
ztomorrow = datetime.datetime.now().replace(hour=9, minute=0, second=0) \
            + datetime.timedelta(days=1)
print(ztomorrow) #2017-09-05 09:00:00.444493
ztomorrow = datetime.datetime.now() \
            + datetime.timedelta(days=1)
print(ztomorrow) #2017-09-05 15:36:44.841415