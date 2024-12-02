import re
s = 'man sun mop run'
result = re.search(r'm\w\w', s)
if result:
	print(result.group())
