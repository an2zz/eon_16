num_list = [[0] * 6 for i in range(6)]  
a = 0
b= 1
i = 0
j = -1
num = 6
 
while True:
    for p in range(1, num + 1):
        a += 1
        j += b
        num_list[i][j] = a
    num -= 1
    if num <= 0:
        break
    for p in range(1, num + 1):
        a += 1
        i += b
        num_list[i][j] = a        
    
    b *= -1
        
for i in range(len(num_list)):
    for j in range(len(num_list[0])):
        print('%3d ' % num_list[i][j], end = '')
    print()
