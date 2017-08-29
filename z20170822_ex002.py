"""
def calc(n1=0, op="+", n2=0):
    n1 = int(input("첫번째 수를 입력하세요."))
    op = input("연산자를 입력하세요.")
    n2 = int(input("두번째 수를 입력하세요."))

    if op == "+":
        res = n1 + n2
    elif op == "*":
        res = n1 * n2
    elif op == "/":
        res = n1 / n2
    else:
        res = n1 - n2

    print("결과 : ", res)
    tu = (res, n1, op, n2)
    return tu

tu = calc()
for i in tu:
    print(i)

"""
param = 100
def func():
    global param
    param = param + 1
    print(param)

func()