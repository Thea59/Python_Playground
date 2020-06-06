# -*- coding: utf-8 -*-
# 循环重复工作
print("Welcome!")
guess = 0  # 初始化guess值，有效的默认值以确保循环进行第一次
while guess != 5:
    g = input("Guess the number: ")  # 循环体的第一部分
    guess = int(g)
    if guess == 5:
        print("You win!")
    else:
        if guess > 5:
            print("Too high")
            
        else:
            print("Too low")
print("Game over!")
