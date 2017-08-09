#f=open('c:/pytest/aa.txt', 'r') #...rt : text 를 읽기 모드. r 도 가능함.
#...한글인코딩.
# http://kin.naver.com/qna/detail.nhn?d1id=1&dirId=104&docId=275676119&qb=7YyM7J207LC4IGNwOTQ5&enc=utf8&section=kin&rank=1&search_sort=0&spq=0&pid=ThEOkspySowssZu4a%2BossssssgZ-417206&sid=uCBGZmOMCXnz3y6gFC9KvA%3D%3D
f=open('c:/pytest/z20170808_ex22.txt', 'r') #...rt : text 를 읽기 모드. r 도 가능함.
for i in f:
    print(i, end='')