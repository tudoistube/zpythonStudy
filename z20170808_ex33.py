import json

d={'name':'joywins', '나이':23, 'job':'programmer'}

print(type(d))
print(d['나이'])

with open('z20170808_ex33.json', 'w') as f:
    #...파일로 만들때는 dump().
    json.dump(d, f, ensure_ascii=False)
