import json

f = open('result.json',encoding='utf8').read()
data = json.loads(f)
print(len(data['messages']))
print(data['name'])
'''
Salom!!!!
'''