import  re

# str = 'Cats are smarter than dogs'
#
# m1 = re.match(r'(.*)are(.*?).*', str)
# print(m1)
#
# print(m1.group())
# print(m1.group(0))
# print(m1.groups(1))

m = re.match('[abcd]','ab')
print(m)

a,b = [0,1]
print(f'a={a},b={b}')

s = '(.*?)wow(0*?)'

# m2 = re.match('hello','world hello')
# print(m2)