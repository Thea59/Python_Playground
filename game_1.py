# -*- coding: utf-8 -*-
# 命令清单：单线行走
print("Welcome!")
g = input("Guess the number: ")  # 读取并返回用户输入，赋值给g
guess = int(g)  # 把输入的g值转换成数字
if guess == 5:
    print("You win!")
else:
    print("You lose!")
print("Game over!")
