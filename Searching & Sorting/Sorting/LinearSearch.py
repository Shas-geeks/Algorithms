def LinearSearch(arr, target):
    """
    Perform a linear search on the given array to find the target value.

    Parameters:
    arr (list): The list of elements to search through.
    target: The value to search for in the list.

    Returns:
    int: The index of the target value if found, otherwise -1.
    """
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1
arr=list(map(int,input("Enter the elements of the array separated by spaces: ").split()))
target=int(input("Enter the target value to search for: "))
result=LinearSearch(arr,target)
if result != -1:
    print(f"Target found at index: {result}")       