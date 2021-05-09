def sum_num(num):
    if num == 1:
        return 1
    return num + sum_num(num-1)

num = int(input('输入计算数字'))

result = sum_num(num)
print(f'{num}!=',result)