# #百钱百鸡

# for husband_chicken_num in range(21):
#   for mother_chiken_num in range(34):
#     if husband_chicken_num*5+mother_chiken_num*3+(100-husband_chicken_num-mother_chiken_num)//3 == 100:
#       child_chiken_num = 100-husband_chicken_num-mother_chiken_num 
#       if(child_chiken_num%3 == 0):
#           print(f'husband_chicken_num={husband_chicken_num} mother_chicken_num={mother_chiken_num} child_chicken_num={child_chiken_num}' )
for x in range(0, 20):
    for y in range(0, 33):
        z = 100 - x - y
        if 5 * x + 3 * y + z / 3 == 100:
            print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (x, y, z))