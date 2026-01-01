NumList=list(map(int,input("Enter Array Element ").split()))
for i in range(0,len(NumList)):
    for j in range (0,len(NumList)-1):
        if(NumList[j]>=NumList[j+1]):
            temp=NumList[j]
            NumList[j]=NumList[j+1]
            NumList[j+1]=temp
print(NumList)