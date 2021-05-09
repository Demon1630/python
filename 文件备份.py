# 文件打开
# old_name = input('请输入您要备份的文件名：')
# old_name = 'C:\\Users\\Administrator\\Desktop\\1.txt'

index = old_name.rfind('.')

new_name = old_name[:index] + '_备份' + old_name[index:]

old_fil = open('old_name','rb')
new_fil = open('new_name','wb')

while True:
    con = old_fil.read(1024)
    if len(con) == 0:
        break
    new_fil.write(con)

old_fil.close()
new_fil.close()