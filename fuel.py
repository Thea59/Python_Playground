# -*- coding: utf-8 -*-
# 一个小例子~
a = input("Please enter the surplus fuel: ")
fuel = int(a)
money = 5

if fuel > 3:
    print("It's OK")
    print("You can drive downtown.")
else:
    if money > 10:
        print("You should buy some gas.")
    else:
        print("You better stay at home.")  # 笑晕
print("What's next?")
