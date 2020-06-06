# -*- coding: utf-8 -*-
# 分支(条件)：代码的分叉路，判断真假值(_bool)
#条件语句
print("Welcome!")
g = input("Guess the number: ")
guess = int(g)
if guess == 5:
    print("You win!")
else:
    if guess > 5:
        print("Too high")
    else:
        print("Too low")
print("Game over!")
