"""
import math
print("파이의 값은 {}입니다.".format( math.pi ))
print("{}의 ceil : 올림 {}, floor : 내림 {}".format(math.pi, math.ceil(math.pi), math.floor(math.pi)))
#파이의 값은 3.141592653589793입니다.
#3.141592653589793의 ceil : 올림 4, floor : 내림 3
"""

"""
import random
candidtes = ['가위', '바위', '보']
selected = random.choice(candidtes)
print(selected)
"""

"""
def get_web(url) :
    # URL 을 넣으면 페이지 내용을 돌려주는 함수.
    import urllib.request
    response = urllib.request.urlopen(url)
    data = response.read()
    decoded = data.decode('utf-8')
    return decoded

url = input('웹페이지 주소를 입력하기?')
content = get_web(url)
print(content)
"""

Bo = '보'
Gawi = '가위'
Bawi = '바위'

def random_choice():
    import random
    return random.choice(['가위','바위','보'])