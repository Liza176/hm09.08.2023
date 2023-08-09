
n1 = input('Из двоичной системы счисления в десятичную? (Да или Нет) ')
if n1 == 'Да':
    n = int(input())
    dvo = ''
    if n == 0:
        print('0')
        exit() 
    for u in range(n):
        if n % 2 == 0:
            dvo = '0' + dvo
            n = n // 2
        else:
            dvo = '1' + dvo
            n = n // 2
        if n == 0:
            break

    print(dvo)
else:
    n = int(input())
    des = 0
    count = 0
    for i in str(n):
        count += 1
        des = int(i)*2**count + des
    print(des)

        

    
