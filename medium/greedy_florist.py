def getMinimumCost(k, c):
    c.sort()
    n = len(c)
    
    min_cost = 0

    for i in range(n):
        # notb == number of times bought
        notb = ((n-(i+1))//k)
        min_cost += ((notb + 1) * c[i])
    
    return min_cost


arr = [1,3,5,7,9]
print(getMinimumCost(3, arr))