# q = [2,1,5,3,4]

# def minimumBribe(q):
#     total_bribes = 0

#     sorted_q = q.copy()
#     sorted_q.sort()

#     sort_q = {sorted_q[i]:i for i in range(0, len(sorted_q))}

#     print(sort_q)

#     for i in range(0, len(q)-1):
#         print(i)
#         condition = (i < sort_q[q[i]] or q[i] > q[i+1])
#         # print(condition)
#         if condition:
#             jumped_position = sort_q[q[i]] - i
#             # print(sort_q[q[i]])
#             print(q[i], jumped_position)

#             if jumped_position > 2:
#                 return "Too chaotic"

#             total_bribes += jumped_position
    
#     return total_bribes

# arr_1 = [1, 2, 5, 3, 7, 8, 6, 4]
# print(minimumBribe(arr_1))

def minimumBribe(q):
    total_bribes = 0

    for i in range(0, len(q)-1):

        condition_1 = q[i] > i+1
        condition_2 = q[i] > q[i+1]

        condition = condition_1 or condition_2

        if condition_1:
            jumped_position = q[i] - (i+1)
        elif condition_2:
            jumped_position = (i+1) - q[i]
        else:
            continue

        if jumped_position > 2:
            return print("Too chaotic")
        
        total_bribes += jumped_position
    
    return print(total_bribes)

arr_1 = [1, 2, 5, 3, 7, 8, 6, 4]
minimumBribe(arr_1)