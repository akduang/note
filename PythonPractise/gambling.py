#coding: UTF-8
# CRAPS
import random

def jisuan():
  play_num = 1
  first_num = random.randint(2,13)
  if(first_num==7 or first_num == 11):
    return 1
  elif(first_num==2 or first_num == 3 or first_num==12):
    return 0
  else:
    while(play_num==1):
      second_num = random.randint(2,13)
      if second_num == first_num:
        play_num=0
        return 1
      elif second_num == 7:
        play_num=0
        return 0
      else:
        play_num == 1

money = 1000
count = 0
while(money>0):
  result = jisuan()
  if result == 1:
    money = money +1
  else:
    money = money-1
  count = count + 1
print(count)
