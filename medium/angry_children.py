def maxMin(k, arr):
    # Write your code here
    arr.sort()
    n = len(arr)

    min_unfairness = max(arr)
    
    for i in range(n - k + 1):
        j = i + k - 1
        val_range = arr[j] - arr[i]

        min_unfairness = min(val_range, min_unfairness)
    
    return min_unfairness

# Thought process

# Instead of creating arrays to store values, we run a loop that gets the two values we need at each instance, subtract the min from the max, and compare it to the min_unfairness if it is smaller