first_num = int(input("Enter the first number..."))
second_num = int(input("Enter the second number..."))
third_num = int(input("Enter the third number..."))

m = []
m.append(first_num)
m.append(second_num)
m.append(third_num)
print(m)
if(m[0]>=10):
    print('ivalid input')
elif(m[0]<1):
    print('ivalid input')
else:
    
    for i in range(0,3):
        for j in range(0,3):
            for k in range(0,3):
                if(i!=j&j!=k&k!=i):
                    print(m[i],m[j],m[k])

