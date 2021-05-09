import re

str = '24*89*92*103'

m = re.search('(-?\d+\.?\d*[*/]-?\d+\.?\d*)',str)

print(m)
print(m.group())
print(m.span())
print(str[m.span()[0]:m.span()[1]])

