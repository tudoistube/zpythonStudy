
import datetime

d=datetime.date(2017,3,12)
print(type(d))
print(d)
print(d.weekday())
print('-------------------------')

d=datetime.date(2017,3,13)
print(d)
print(type(d.weekday()))
print(d.weekday())
print('-------------------------')

import datetime
#dictionary 이용하기.
y={0:'월요일',1:'화요일',2:'수요일',3:'목요일',4:'금요일',5:'토요일',6:'일요일'}
d=datetime.date(2017,3,13)  
print(y[d.weekday()])
print('-------------------------')
d=datetime.date.today()  
print(y[d.weekday()])
print('-------------------------')
d=datetime.datetime(2017,3,12,14,40)
print(d)
print(y[d.weekday()])
print('-------------------------')
d=datetime.time(14,41)
print(d)
print('-------------------------')
d=datetime.date.today()
print(d)
d2=datetime.datetime.today()
print(d2)
d3=datetime.datetime.now()
print(d3)
print('===============')

from datetime import date
d=date.today()
print(d.year)
d2=datetime.date.today()
print(d2.year)
print('-------------------------')
