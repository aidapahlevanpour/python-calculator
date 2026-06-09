while True:
    num1 = float(input('enter the first number:'))
    num2 = float(input('enter the seccond number:'))
    print('+  -  *  /')
    ch = input('choose an operation:')
    if ch == '+' :
        a = num1 + num2
    elif ch == '-' :
        a = num1 - num2
    elif ch == '*' :
        a = num1 * num2
    elif ch == '/' :
        if num2 != 0 :
            a = num1 / num2
        else :
            a = 'error: cannot divide by zero.'
    else :
        a = 'error: invslid oeration.'
    
    print(num1, ch, num2, '=', a)

    another = input('do you want another calculation?(yes/no)')
    if another == 'no' :
        break

    print(another)