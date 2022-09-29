def missingCharacters(s):
    # Write your code here
    characters = [i for i in '0123456789abcdefghijklmnopqrstuvwxyz']
    character_dict = {}
    
    for i in range(len(characters)):
        character_dict[characters[i]] = i
    
    for i in set(s):
        if i in character_dict:
            print(character_dict[i])
            characters.pop(character_dict[i])
            del character_dict[i]
    
    return ''.join(characters)

print(missingCharacters('8hypotheticall024y6wxz'))