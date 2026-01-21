"""
      This function takes an array of integers and returns a list where each element
    is the index of the nearest smaller element to the left of the corresponding element
    in the input array. If there is no smaller element to the left, it returns -1 for that position.
    
    :param arr: List[int] - Input array of integers
    :return: List[int] - List of indices of nearest smaller elements to the left

    *************************************************************************************************
    Example:
    Input: arr = [4, 5, 2, 10, 8, 1]
    Output: [-1, 4, -1, 2, 2, -1]
    Time Complexity: O(n)
    Space Complexity: O(n)
"""
def SmallestLeft(arr):
    Stack=[]
    OutputAns=[]
    for i in range(len(arr)):
        if not Stack:
            OutputAns.append(-1)
        elif Stack and Stack[-1]>=arr[i]:
            while Stack and Stack[-1]>=arr[i]:
                Stack.pop()
            if not Stack:
                OutputAns.append(-1)
            else:
                OutputAns.append(Stack[-1])
        elif Stack and Stack[-1]<arr[i]:
            OutputAns.append(Stack[-1])
        Stack.append(arr[i])
    return ", ".join(map(str,OutputAns))
arr=list(map(int,input("Enter The Array Elements :").split()))
print(SmallestLeft(arr))