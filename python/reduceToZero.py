num = 1000000
x = 0
t = 0
while num>0:
    if num % 2 == 0:
        num = num/2
    else:
        num = num-1


    t += 1

print(t)


