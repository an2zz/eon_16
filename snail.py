num = int(input('수를 입력하세요 : '))
num_list = [[0] * 6 for i in range(num)]  
a = 0
b= 1
i = 0
j = -1

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
        print('%d ' % num_list[i][j], end = '')
    print()
