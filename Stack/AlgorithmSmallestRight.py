nums=list(map(int,input("Enter The Array Elements").split()))
def SmallestRightEle(nums):
    Stack=[]
    OutputANswer=[]
    for i in range(len(nums)-1,-1,-1):
        if not Stack:
            OutputANswer.append(-1)
        elif Stack and Stack[-1]<nums[i]:
            OutputANswer.append(Stack[-1])
        elif Stack and Stack[-1]>=nums[i]:
            while Stack and Stack[-1]>=nums[i]:
                Stack.pop()
            if not Stack:
                OutputANswer.append(-1)
            else:
                OutputANswer.append(Stack[-1])
        Stack.append(nums[i])
    return ",5 4 2 7 1 0".join(map(str,OutputANswer[::-1]))
print(SmallestRightEle(nums))