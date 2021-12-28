import math
print("Welcome to calculator\nEnter ** for power, + for adding, / for division and - for subtracting")
while True:
    try:
        print("Enter first number-")
        first =int(input())
        print("Enter second number-")
        second =int(input())
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
        elif operator == '**':
            ans5 = pow(first, second)
            print(ans5)
    except Exception as e:
        print("Wrong input")