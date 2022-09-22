def checker(seen):
    # Traversing through the elements in the seen array
    for i in range(len(seen) - 1):
        # joining the next elements after seen[i] in the seen array
        for j in range(i+1, len(seen)):
            if int(seen[i]) % 2 == 0:
                remaining_values = int(''.join(seen[j:]))
                if remaining_values % 2 == 0:
                    return True

    return False

def searchingChallenge(str):
    nums = '1234567890'
    found_num_and_position = {}
    num_position = []
    seen = []

    # Traversing through each element in the string to fetch out the numbers and store them in the found_num_and_position
    for i in range(len(str)):
        if str[i] in nums:
            # Each found number is stored with its index as the key
            found_num_and_position[i] = str[i]
            # The index is also stored for reference
            num_position.append(i)
    
    # Looping through a range to find the numbers that are assigned to positions in the num_position array
    for i in range(max(num_position)+1):
        if i in num_position:
            # Inserting the found number into the seen array
            seen.append(found_num_and_position[i])
            
            # Run the checker function
            if checker(seen):
                return True
            
        else:
            seen = []

    return False

str1 = 'f178svg3k19k46'
str2 = '7r5gg37413'
print(searchingChallenge(str1))
print(searchingChallenge(str2))
