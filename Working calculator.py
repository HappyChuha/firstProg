while True:
    print("Enter first number-")
    first = int(input())
    print("Enter second number-")
    second = int(input())      
    print("Enter an operator")
    operator = input()
    if operator == '*':
        ans = first * second
        print(ans)

    elif operator == '/':
        ans2 = first / second
        print(ans2)

    elif operator == '-':
        ans3 = first - second
        print(ans3)

    elif operator == '+':
        ans4 = first + second
        print(ans4)
        break
    elif operator == '**':
        ans5 = pow(first, second)
        print(ans5)

