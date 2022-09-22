def searchingChallenge(str):
    '''
        We use that if there are two converted integer values that are in same subset in the string, it means we should return True
    '''
    nums = '1234567890'
    found_num_and_position = {}
    num_position = []

    # Traversing through each element in the string to fetch out the numbers and store them in the found_num_and_position
    for i in range(len(str)):
        if str[i] in nums:
            # Each found number is stored with its index as the key
            found_num_and_position[i] = int(str[i])
            # The index is also stored for reference
            num_position.append(i)
    
    counter = 0

    # Looping through a range to find the numbers that are assigned to positions in the num_position array
    for i in range(max(num_position)+1):
        if i in num_position:
            if found_num_and_position[i] % 2 == 0:
                counter += 1
                
            if counter >= 2:
                return True
            
        else:
            counter=0

    return False

str1 = 'f178svg3k19k46'
str2 = '7r5gg37413'
print(searchingChallenge(str1))
print(searchingChallenge(str2))
