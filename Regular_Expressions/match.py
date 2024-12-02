import re
s = 'man sun mop run'
result = re.match(r'm\w\w', s)
print(result.group())
s1 = 'sun man mop run'
result = re.match(r'm\w\w', s1)
print(result)
