# 평균, 분산, 표준편차를 구하는 프로그램
import math

# 자료값 리스트
# ...174p.통계자료를 처리할 때는 여러개의 자료값이 필요한데
#               이럴때는 List 를 사용하는 것이 가장 적당함.
d = [1, 2, 3, 4, 5]
print(d)

# 평균 구하기
mean = sum(d) / len(d)
print(mean)

# 분산 구하기
# ...174p.각 자료값에서 평균값을 뺀 값(편차)의 제곱을 모두 더해서 자료의 개수로 나눈 값.
vsum = 0
for x in d:
    vsum = vsum + (x - mean)**2
var = vsum / len(d)
print(var)

# 표준편차 구하기
# ...174p.분산의 제곱근 값.
std = math.sqrt(var)
print(std)
