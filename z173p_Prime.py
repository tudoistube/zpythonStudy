# ...173p.소인수분해 프로그램
x = int(input("? "))    # 소인수분해를 할 숫자를 입력받아 정수로 바꿉니다.
d = 2                   # 가장 작은 소수인 2부터 나누어 봅니다.

while d <= x:
    if x % d == 0:    # x가 d로 나누어지면(나머지가 0이면)
        x = x / d     # x를 d로 나눠서 다시 x에 저장합니다.
        print("d : ", d, ", x : ", x)      # d는 x의 약수이므로 출력합니다.
    else:
        d = d + 1     # 나누어지지 않으면 1을 더해서 반복합니다.
        print("else d : ", d, ", x : ", x)      # d는 x의 약수이므로 출력합니다.
