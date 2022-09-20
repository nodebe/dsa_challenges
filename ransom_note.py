def ransomNote(magazine, note):

    # Creating dictionary to store magazine words value
    magazine_dictionary = {}

    # Inserting magazine keys into dictionary and incrementing their values
    for j in magazine:
        if magazine_dictionary.get(j):
            magazine_dictionary[j] += 1
        else:
            magazine_dictionary[j] = 1
    
    # Checking each word in note against dictionary keys and decrementing the values by one if found
    for i in note:
        if i in magazine_dictionary:
            magazine_dictionary[i] -= 1
        else:
            return print('No')
        
        if magazine_dictionary[i] < 0:
            return print('No')

    return print('Yes')

mag = ['two', 'times', 'three', 'is', 'not', 'four']
note = ['two', 'times', 'two', 'is', 'four']

ransomNote(mag, note)