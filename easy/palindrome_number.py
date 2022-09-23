def isPalindrome(x: int) -> bool:
    if x < 10:
        return False

    reversed_list = []
    while x > 0:
        reversed_list.append(x%10)
        x //= 10

    if reversed_list[::-1] == reversed_list:
        return True
    
    else:
        return False

print(isPalindrome(1232))