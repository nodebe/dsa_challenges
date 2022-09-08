def hour_glass(arr):
    # To store the hour glass sum and get the max sum later on
    sums = []
    j = 0

    # Traversing through the Array
    while j < len(arr):
        # To know when to stop traversing the column for edge cases and avoiding passing list index
        if j >= len(arr)-2:
            break

        j_1 = arr[j+1]
        j_2 = arr[j+2]
        i = 0

        # Traversing through each inner array
        while i < len(arr[j]):
            # To know when to stop traversing the row for edge cases and avoiding passing list index
            if i >= len(arr[j])-2:
                break

            top = arr[j][i] + arr[j][i+1] + arr[j][i+2]
            mid = j_1[i+1]
            bottom = j_2[i] + j_2[i+1] + j_2[i+2]

            hour_glass_sum = top + mid + bottom

            sums.append(hour_glass_sum)

            i+=1
        
        j+=1
    return max(sums)

arr = [[1,1,1,0,0,0],[0,1,0,0,0,0],[1,1,1,0,0,0],[0,0,2,4,4,0],[0,0,0,2,0,0],[0,0,1,2,4,0]]
arr_2 = [[-1,-1,0,-9,-2,-2],[-2, -1, -6, -8, -2, -5], [-1, -1, -1, -2, -3, -4], [-1, -9, -2, -4, -4, -5], [-7, -3, -3, -2, -9, -9],[-1, -3, -1, -2, -4, -5]]

print(hour_glass(arr_2))