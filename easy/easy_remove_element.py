def removeElement(nums, val) -> int:
    nums_length = len(nums)

    length_of_nums = 0
    while length_of_nums < nums_length:
        while nums[length_of_nums] == val:
            nums.pop(length_of_nums)
            nums_length -= 1

            if nums_length == length_of_nums:
                break
        else:
            length_of_nums+=1
        
    
    return length_of_nums

print(removeElement([3,2,1,0,3], 3))