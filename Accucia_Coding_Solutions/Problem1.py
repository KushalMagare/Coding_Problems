import re
_input="My name is Ram. I am Ram Kumar. Ram, Please come here"

_list=[]
_list=re.findall(r'\w+', _input)

res = {}

for i in _list:
    res[i] = _list.count(i)
print(res)