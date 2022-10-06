def missingNumbers(arr, brr):
    # Write your code here
    arr_dict = dictArranger(arr)
    brr_dict = dictArranger(brr)
    
    new_list = []
    
    for i in arr_dict:
        if arr_dict[i] >= brr_dict[i]:
            del brr_dict[i]
    
    for j in brr_dict:
        new_list.append(j)
    
    new_list.sort()

    return new_list

def dictArranger(array):
    array_dict = {}
    for i in array:
        if i not in array_dict:
            array_dict[i] = 1
        else:
            array_dict[i] += 1
    
    return array_dict


arr = [203, 204, 205, 206, 207, 208, 203, 204, 205, 206]
brr = [203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 205, 206, 204]

print(missingNumbers(arr, brr))