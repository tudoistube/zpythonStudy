li = [i  for i in range(1, 11)]
print(li) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum(li)) #55

#...사전형 : {키: 값}, 중복제거됨, 마지막중복값이 덮어씀.
dic = dict() #또는 dic = {}
dic = {1:"value", 2:"b", 3:"c"}
print(dic) #{1: 'value', 2: 'b', 3: 'c'}
print(dic.keys()) #dict_keys([1, 2, 3])
print(dic.values()) #dict_values(['value', 'b', 'c'])


