accounts = [[1,7,9],[8,3,17],[15,7,12]]
x = []
for i in range(len(accounts)):
    y=0
    for a in range(len(accounts[i])):

        y += accounts[i][a]

    x.append(y)

print(x)
result = 0
for i in range(len(x)):
    a = x[i]
    b = result
    if a > b :
        result = a

print(result)