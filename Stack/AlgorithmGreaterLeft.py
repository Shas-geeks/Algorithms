def GreaterLeft(nums):
    Stack,OutputArr=[],[]
    for i in range(len(nums)):
        if not Stack:
            OutputArr.append(-1)
        elif Stack and Stack[-1]>nums[i]:
            OutputArr.append(Stack[-1])
        elif Stack and Stack[-1]<=nums[i]:
            while Stack and Stack[-1]<=nums[i]:
                Stack.pop()
            if not Stack:
                OutputArr.append(-1)
            else:
                OutputArr.append(Stack[-1])
        Stack.append(nums[i])
    return ", ".join(map(str,OutputArr))
nums=list(map(int,input("Enter The Array Elements :").split()))
print(GreaterLeft(nums))
# """////////////////////////////////////////****(Explanation)****////////////////////////////////////////  
#       This function takes an array of integers and returns a list where each element          
#     is the nearest greater element to the left of the corresponding element in the input array.
#     If there is no greater element to the left, it returns -1 for that position.
#     
#     :param arr: List[int] - Input array of integers
#     :return: List[int] - List of nearest greater elements to the left
#     *************************************************************************************************
#     Example: 
#     Input: arr = [4, 5, 2, 10, 8, 1]
#     Output: [-1, -1, 5, -1, 10, 8]
#     Time Complexity: O(n) 
#    Space Complexity: O(n)                