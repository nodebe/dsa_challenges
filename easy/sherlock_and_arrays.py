def balancedSums(arr):
    # Write your code here
    left_sum = 0
    total_sum = sum(arr)
    
    # Check if the 2 * left_sum is = total_sum - current element
    for i in arr:
        if 2*left_sum == total_sum - i:
            return "YES"
            
        left_sum+=i
    
    return "NO"

arr_1 = [1,2,3,3]
arr_2 = [1,2,3]

print(balancedSums(arr_1))