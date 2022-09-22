def rotLeft(a, d):
    d %= len(a)
    shifted_arr = a[d:] + a[0:d]

    return shifted_arr

arr = [1,2,3,4,5]

print(rotLeft(arr, 230000000002213232312122))