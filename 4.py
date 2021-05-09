age = 18
name = 'TOM'
weight = 50.5
stu_id = 1

# 1.今年我的年龄是x岁
print('今年我的年龄是%d岁' % age)

# 2.我的名字是x
print('我的名字是%s' % name)

# 3.我的体重是x斤
print('我的体重是%.2f斤' % weight)

# 4.我的学号是x
print('我的学号是%d' % stu_id)

print('我的学号是%03d' % stu_id)
print('我的名字是%s,我今年%d岁' %(name,age))

print('我的名字是%s,我今年%s岁'%(name,age))
print(f'我的名字是{name},我今年{age}岁')