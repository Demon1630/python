j= 1

while j <= 9:
    i = 1
    while i <= j:
        print(f'{j}x{i}={j*i}',end='\t')
        i +=1
    print()
    j+=1