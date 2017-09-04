"""
def always_false():
    print('함수 always_false')
    return False

def always_true():
    print('함수 always_true')
    return True

#...and 와 or 연산 모두 첫번째 값을 보고 더 이상
#   실행할 필요가 없으면 두번째 값은 실행하지 않음.
if always_false() and always_true():
    print(True)
else:
    print(False)
'''
함수 always_false
False
'''
"""

"""
zdict = {"key2": "val1"}
#...파이썬에서는 단락 평가를 지원함.
if "key1" in zdict and zdict["key1"]=="val1":
    print("key1 도 있고, 그 값은 val1 이다.")
else:
    print("없네요")
"""

"""
print('0:', bool(0)) #0: False
print('[빈리스트]:', bool([])) #[빈리스트]: False
print('None:', bool(None)) #None: False
print('빈문자열:', bool('')) #빈문자열: False
"""

"""
#...실행후 아무것도 입력하지 않고 Enter 를 누름.
val = input('입력해주세요>') or '아무값도 입력받은게 없어요.'
print('입력받은값: ', val)
#입력해주세요>
#입력받은값:  아무값도 입력받은게 없어요.
"""

"""
if []:
	print("[]은 True입니다.")

if [1, 2, 3]:
	print("[1,2,3]은/는 True입니다.")

if {}:
	print("{}은 True입니다.")

if {'abc': 1}:
	print("{'abc':1}은 True입니다.")

if 0:
	print("0은/는 True입니다.")

if 1:
	print("1은 True입니다.")
"""

"""
#...or 연산의 결과는 앞의 값이 True 이면 뒤는 더 보지도 않고,
#   앞의 값이 Fasle 이면 뒤의 값을 따름.
a = 1 or 10	# 1의 bool 값은 True입니다.
b = 0 or 10	# 0의 bool 값은 False입니다.
print("a:{}, b:{}".format(a, b))
print("a:{}, b:{}".format(bool(a), bool(b)))
'''
a:1, b:10
a:True, b:True
'''
"""

