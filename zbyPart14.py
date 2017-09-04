"""
zlist = [135, 462, 27, 2753, 234]
print(zlist.index(27)) #2
print(zlist.index(50))
'''
Traceback (most recent call last):
  File "D:/JoyWins/WS_Python/ztryHello/ztemp.py", line 3, in <module>
    print(zlist.index(50))
ValueError: 50 is not in list
'''
"""

"""
zlist = [135, 462, 27, 2753, 234]
if 50 in zlist:
    list.index(50)
else:
    print('50은 없는 값이네요.') #50은 없는 값이네요.
"""

"""
zlist2 = [1, 2, 3] + [4, 5, 6]
print(zlist2) #[1, 2, 3, 4, 5, 6]
"""

"""
#...zlist.extend() 를 이용하면 원래 있던 zlist 리스트를 고칠 수 있음.
zlist = [135, 462, 27, 2753, 234]
zlist2 = [9, 10, 11]
zlist.extend(zlist2)
print(zlist)
#[135, 462, 27, 2753, 234, 9, 10, 11]
"""

"""
#...zlist.insert(index, value) 로 리스트에 값을 추가함.
zlist = [135, 462, 27, 2753, 234]
zlist.insert(2, 999)
print(zlist) #[135, 462, 999, 27, 2753, 234]
"""

"""
#...인덱스가 -1 은 뒤에서 첫번째라는 뜻임.
zlist = [135, 462, 27, 2753, 234]
zlist.insert(-1, 999)
print(zlist) #[135, 462, 27, 2753, 999, 234]
"""

"""
#...인덱스가 음수이면 뒤에서부터 하나씩 가져옴.
#   인덱스가 -1이면 뒤에서 첫번째 값을 의미함.
zlist = [100, 200, 300]
print(zlist[-1]) #300
"""

"""
#...insert() 는 리스트의 인덱스를 벗어나는 값을 넣어도
#   리스트의 가장 마지막에 값이 추가됨.
zlist = [100, 200, 300]
zlist.insert(9, 500)
print(zlist) #[100, 200, 300, 500]
print(zlist.index(500)) #3
"""

"""
zlist = [135, 462, 27, 2753, 234]
zlist.sort()
print(zlist) #[27, 135, 234, 462, 2753]
"""

"""
#...list.reverse() 는 내림차순이 아니라 리스트의 값을
#   거꾸로 뒤집음.
zlist = [135, 462, 27, 2753, 234]
zlist.reverse()
print(zlist) #[234, 2753, 27, 462, 135]
"""

"""
zlist = [135, 462, 27, 2753, 234]
print(zlist.index(227))
"""

"""        
def safe_index(my_list, value):
    # 함수를 완성하세요
    if value in my_list:
        return my_list.index(value)
	else:
        return None

safe_index([1,2,3,4,5], 5)
safe_index([1,2,3], 5)
"""

"""
def safe_index2(my_list, value):
    try:
        return my_list.index(value)
    except ValueError:
        return None

safe_index2([1,2,3,4,5], 5)
safe_index2([1,2,3], 5)
"""

"""
zlist1 = [1, 2, 3, 4]
zlist1.insert(0, 8)
print(zlist1)
zlist1.sort()
print(zlist1)
zlist1.reverse()
print(zlist1)
"""

"""
zlist = [1, 2, 3]
zstr = "Hi, JoyWins!"
print(3 in zlist) #True
print("JoyWins" in zstr) #True
#...파이썬은 영문 대소문자를 구분함.
print("joywins" in zstr) #False
print(zlist.index(2)) #1
print(zstr.index('J')) #4
"""

"""
#...list() 에 문자열을 넣으면 각 문자가 든 리스트가 됨.
zlist = list("abcdef")
print(zlist) 
#['a', 'b', 'c', 'd', 'e', 'f'] #리스트형이 됨.

#...문자열.split() 을 하면 각 단어가 든 리스트로 됨.
zstr = "Python 이 맘에 들려구 해요."
zstrList = zstr.split()
print(zstrList) 
#['Python', '이', '맘에', '들려구', '해요.'] #리스트형이 됨.
"""

"""
zstr = "10:15:23"
#...문자열.split(구분자)를 실행하면 구분자를 기준으로
#   리스트형에 값을 담음.
zstrList = zstr.split(":")
print(zstrList) #['10', '15', '23']
#...구분자.join(리스트) 을 실행하면 구분자로 연결된 문자열이 됨.
print(":".join(zstrList)) #10:15:23
print("".join(zstrList)) #101523
"""

"""
str = "오늘은 날씨가 흐림"
words = str.split(" ")
print(words) #['오늘은', '날씨가', '흐림']
position = words.index("흐림")
print(position) #2
new_str = " ".join(words)
print(new_str) #오늘은 날씨가 흐림
"""

"""
#...문자열 슬라이스.
ztxt = "Hi,JoyWins"
print(ztxt[1]) #i
print(ztxt[1:5]) #i,Jo
"""

"""
#...리스트 슬라이스.
ztxt = "Hi,JoyWins"
zlist = list(ztxt)
print(zlist) #['H', 'i', ',', 'J', 'o', 'y', 'W', 'i', 'n', 's']
print(zlist[2:5]) #[',', 'J', 'o']
#...리스트의 처음부터 끝까지 슬라이스하기.
print(zlist[:len(zlist)]) #['H', 'i', ',', 'J', 'o', 'y', 'W', 'i', 'n', 's']
print(zlist[0:len(zlist)]) #['H', 'i', ',', 'J', 'o', 'y', 'W', 'i', 'n', 's']
print(zlist[0:]) #['H', 'i', ',', 'J', 'o', 'y', 'W', 'i', 'n', 's']
"""

"""
#...파이썬2와 파이썬3에서 리스트를 복사하는 방법.
ztxt = "Hi,JoyWins"
zlist = list(ztxt)
#...파이썬2에서 리스트를 복사하는 방법.
zlist2 = zlist[:]
print(zlist) #['H', 'i', ',', 'J', 'o', 'y', 'W', 'i', 'n', 's']
print(zlist2) #['H', 'i', ',', 'J', 'o', 'y', 'W', 'i', 'n', 's']
#...파이썬3에서 리스트를 복사하는 방법.
#   파이썬3에서는 리스트를 복사할 때 슬라이스를 이용하지 않는 것을 권장함.
zlist3 = zlist.copy()
print(zlist3) #['H', 'i', ',', 'J', 'o', 'y', 'W', 'i', 'n', 's']
"""

rainbow = ["빨", "주", "노", "초", "파", "남", "보"]

# red_colors가 ["빨", "주", "노"]의 값을 가지도록 rainbow를 slice하세요.
red_colors = rainbow[ 0 : 3 ]
print(red_colors)

#blue_colors가 ["파", "남", "보"]의 값을 가지도록 rainbow를 slice하세요.
blue_colors = rainbow[4 :  ]
print(blue_colors)

"""
zlist = list(range(20))
print(zlist)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print(zlist[15:20])#[15, 16, 17, 18, 19]
#...슬라이스[시작값:마지막값+1:step] 으로 값을 2, 3 씩 건너뛰면서 구할 수 있음.
print(zlist[5:15:2]) #[5, 7, 9, 11, 13]
print(zlist[5:15:3]) #[5, 8, 11, 14]
"""

"""
#...슬라이스의 스텝에 마이너스(-)를 주면서 스텝만큼 감소시킴.
list1 = list(range(20))
# reverse_list가 17, 13, 9, 5의 값을 가지도록 list1을 slice하세요
reverse_list = list1[17:4:-4]
print(reverse_list) #[17, 13, 9, 5]
"""

"""
znum = list(range(10))
print(znum) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
del znum[0]
print(znum) #[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(znum[:5]) #[1, 2, 3, 4, 5]
#...슬라이스를 이용해서 리스트 안에 영역을 정해서 값을 지우기.
del znum[:5]
print(znum) #[6, 7, 8, 9]
print(znum[1:3]) #[7, 8]
znum[1:3] = [77, 88]
print(znum) #[6, 77, 88, 9]
#...바꾸려는 값의 개수와 기존 값의 개수가 꼭 같을 필요는 없음.
#   값 1개를 값 3개로 바꿔서 6이 33, 44, 55로 바뀜.
znum[:1]=[33, 44, 55]
print(znum) #[33, 44, 55, 77, 88, 9]
#...값 2개를 값 1개로 바꿔서 44, 55가 8로 바뀜.
print(znum[1:3]) #[44, 55]
znum[1:3] = [8]
print(znum) #[33, 8, 77, 88, 9]
"""

list1 = [0, 1, 2, 3, 4, 5]
print(list1[1:4]) #[1, 2, 3]
list1[1:4] = [11, 22, 33]
print(list1) #[0, 11, 22, 33, 4, 5]

#...list2의 1부터 3까지를 del과 slice를 이용해서 지우기.
list2 = [0, 1, 2, 3, 4, 5]
del(list2[1:4])
print(list2) #[0, 4, 5]