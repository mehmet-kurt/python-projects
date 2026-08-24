nums = [1,2,3,4,5]
runningSum = []
for i in range(len(nums)):
    y = 0
    for a in range(i+1):
        y = y + nums[a]
    runningSum.insert(i,y)

print(runningSum)