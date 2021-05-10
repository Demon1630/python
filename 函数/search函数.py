"""
re.search函数
"""

import re

str = 'I am ok, Are you 1355 ok ?'

s = re.search('([A-Z][a-z]+).*([0-9])',str)

print(s.group(1))
print(s.group(2))

print(s.group())

print(s)


