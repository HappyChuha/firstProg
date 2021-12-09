list1 = [int,float, "pc", "no cap", 72, 4, 6, 8, 9, "LOLOLLLOL", 8465146, 4, 232]
for item in list1:
    if str(item).isnumeric() and item>6 or item==6:
        print(item)