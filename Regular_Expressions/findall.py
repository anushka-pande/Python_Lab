import re
s = 'man sun mop run'
result = re.findall(r'm\w\w', s)
print(result)
