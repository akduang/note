#水仙花数


num = int(input("number:"))
# print("\n")
# print(num.type)

low = num % 10
mid = int (num//10%10)
high = int (num//100)
if num == low**3+mid**3+high**3:
    print("Yes")
else:
    print("not")