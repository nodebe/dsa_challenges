def removeDuplicates(nums) -> int:
    i = 1
    for j in nums:
        if check_range(i, nums):
            break

        while j == nums[i]:
            nums.pop(i)

            if check_range(i, nums):
                break
        i+=1
    
    return len(nums)

def check_range(i, nums):
    if i >= len(nums):
        return True
    else:
        return False

print(removeDuplicates([1,1]))