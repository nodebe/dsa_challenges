def twoStrings(s1, s2):
    set_s1 = set(s1)
    set_s2 = set(s2)

    for i in set_s2:
        if i in set_s1:
            return 'YES'
    
    return 'NO'

s1 = 'hello'
s2 = 'world'

print(twoStrings(s1, s2))