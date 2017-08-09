#...http://cafe.naver.com/gubass/2083
import json

with open('z20170808_ex31.json', 'r') as f:
    l_info=json.load(f)
print(l_info)
print(type(l_info))
print(l_info['eng'])

