def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    arr_sum = 0

    for i in arr:
        arr_sum += i

    min_ = arr_sum - arr[-1]
    max_ = arr_sum - arr[0]

    print(min_, max_)


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
