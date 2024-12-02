import re 
s = 'This; is the: "Core" Python\'s book'
result = re.split(r'\W+', s)
print(result)
