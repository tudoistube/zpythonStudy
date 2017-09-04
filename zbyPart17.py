"""
#...길이가 1~10까지의 정사각형 넓이 구하기.
areas = []
for i in range(1, 11):
    areas = areas + [i*i]
print("areas: ", areas)

#...아래 1라인이면 위의 3라인과 같음.
areas2 = [i*i for i in range(1, 11)]
print("areas2: ", areas2)
"""

"""
#...길이가 1~10 중 짝수길이의 정사각형 넓이 구하기.
areas = []
for i in range(1, 11):
    if i%2 == 0:
        areas = areas + [i*i]
print("areas: ", areas)

#...아래 1라인이면 위의 3라인과 같음.
areas2 = [i*i for i in range(1, 11) if i%2 == 0]
print("areas2: ", areas2)
"""

"""
#...Comprehension 을 이용하여 중첩 for 문 처리하기 :
#   각 좌표를 튜플로 가지는 리스트 만들기 :
print([(x, y) for x in range(5) for y in range(5)])
#[(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
"""


"""
#...딕셔너리의 Comprehension :
studentsList = ["영희", "정희", "수희", "미희", "진희"]
#...enumerate 사용 :
for num, name in enumerate(studentsList):
    print("{}번의 이름은 {}입니다".format(num+1, name))
"""

"""
#...딕셔너리의 Comprehension :
studentsList = ["영희", "정희", "수희", "미희", "진희"]
studentsDict = {"{}번".format(num+1): name for num, name in enumerate(studentsList)}
print(studentsDict)
#{'1번': '영희', '2번': '정희', '3번': '수희', '4번': '미희', '5번': '진희'}
"""

"""
#...zip() 함수 : 리스트를 딕셔너리로 만드는 함수 :
studentsList = ["영희", "정희", "수희", "미희", "진희"]
scoresList = [85, 92, 78, 90, 100]
for x, y in zip(studentsList, scoresList):
    print(x, y)
#영희 85 정희 92 수희 78 미희 90 진희 100
"""

#...zip() 함수 : 리스트를 딕셔너리로 만드는 함수 :
studentsList = ["영희", "정희", "수희", "미희", "진희"]
scoresList = [85, 92, 78, 90, 100]
scoresDict = {student : score for student, score in zip(studentsList, scoresList)}
print(scoresDict) #{'영희': 85, '정희': 92, '수희': 78, '미희': 90, '진희': 100}

product_list = ["풀", "가위", "크래파스"]
price_list = [800, 2500, 5000]
product_dict = {name:price for name, price in zip(product_list, price_list)}