print("How many rows")
rows = int(input())
print("Type 1 or 0")
v = int(input())
new = bool(v)
if new == True:
    for i in range(1,rows+1):
        for j in range(1, i+1):
            print("*", end="")
        print()
elif new == False:
    for i in range(rows,0,-1):
        for j in range(1,i+1):
            print("*",end="")
        print()