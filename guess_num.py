# 產生一個隨機整數1~100(不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對的話 印出"終於猜對了!"
# 猜錯的話 要告訴他 比答案大/小

import random
r = random.randint(1, 100)
while True:
    guess = input('猜我心裡在想哪個數字？回答：')
    guess = int(guess)
    if guess == r:
        print('你猜對了！')
        break
    elif guess > r:
        print('比答案大')
    elif guess < r:
        print('比答案小')