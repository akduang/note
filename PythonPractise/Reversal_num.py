#反转整数


# num = int(input("Please input a number:"))
# rev_num = 0

# while num > 0:
#     rev_num = rev_num*10 + num % 10
#     num = num//10
# print(rev_num)

num = int(input("Please input a number:"))

while num > 0:
  rev_num = num % 10
  num = num//10
  print(rev_num,end='')
