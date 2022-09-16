def minimumBribe(q):
    total_bribes = 0

    sorted_q = q.copy()

    if q == sorted_q.sort():
        return 0

    for i in range(1, len(q)+1):
        condition = (q[i-1] > i)

        if condition:
            jumped_position = q[i-1] - i

            if jumped_position > 2:
                return "Too chaotic"

            total_bribes += jumped_position
    
    return total_bribes

arr = [2,1,5,3,4]
arr_1 = [1, 2, 5, 3, 7, 8, 6, 4]
print(minimumBribe(arr_1))