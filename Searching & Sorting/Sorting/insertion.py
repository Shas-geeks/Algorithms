# nums=[30,70,20,10,10,50,50,40,60]
nums=list(map(int,input("Enter the Array Values").split()))
for i in range(1,len(nums)):
    key=nums[i]
    j=i-1
    while j>-1 and key<nums[j]:
        nums[j+1]=nums[j]
        j-=1
    nums[j+1]=key
print(nums) 