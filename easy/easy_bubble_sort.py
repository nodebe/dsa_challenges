def countSwaps(a):
    numSwaps = 0
    for i in range(len(a)):
        # Reason for subtracting from i+1 is because we know that for every bubble, the elements after the (length of a - ith element) are at their right position so we do not need to compare that again.
        for j in range(len(a)-(i+1)):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                numSwaps += 1
    
    print(f'Array is sorted in {numSwaps} swaps.')
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[-1]}')
    
    return