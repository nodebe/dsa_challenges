def reverseArray(arr):

    # Traversing through the array indexes
    for i in range(0, len(arr)+1):
        
        left_index = i
        right_index = len(arr) - (i+1)

        # Check for break cases i.e when pointers get to the middle of the array
        if right_index <= left_index:
            break

        # Switching positions of left and right indices
        arr[left_index], arr[right_index] = arr[right_index], arr[left_index]
    
    return arr

arr_1 = [i for i in range(0,12)]
print(reverseArray(arr_1))