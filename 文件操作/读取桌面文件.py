
# f = open('C:\\Users\\Administrator\\Desktop\\1.txt','r')

f = open(r'C:\Users\Administrator\Desktop\2.txt','w+')

f.write(str(123456))


f.seek(0,0)
content = f.read()
print(content)
f.close()

