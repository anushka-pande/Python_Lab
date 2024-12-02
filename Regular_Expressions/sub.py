import re
s = 'Ahmedabad, Kumbhmela will be conducted at Ahmedabad in India. Ahmedabad.'
res = re.sub(r'Ahmedabad', 'Allahabad', s)
print(res)
res = re.subn(r'Ahmedabad', 'Allahabad', s)
print(res)
