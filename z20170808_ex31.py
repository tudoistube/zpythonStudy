import json

d={'kor':90, 'eng':80, 'mat':88}

print(type(d))
print(d['eng'])

with open('z20170808_ex31.json', 'w') as f:
    #...파일로 만들때는 dump().
    json.dump(d, f)
