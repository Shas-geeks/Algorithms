NumArr=list(map(int,input("Enter ArrayElement").split()))
for i in range(0,len(NumArr)-1):
    min_ele,k=NumArr[i],i
    for j in range(i+1,len(NumArr)):
        if min_ele>=NumArr[j]:
            min_ele=NumArr[j]
            k=j
    temp=NumArr[i] 
    NumArr[i]=NumArr[k]
    NumArr[k]=temp
print(NumArr)


    