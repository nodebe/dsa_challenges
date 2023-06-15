
import os


def birthdayCakeCandles(candles):
    # Write your code here
    candles.sort(reverse=True)
    tall_candles = 0

    for i in range(candles_count):
        tall_candles += 1
        if (i != candles_count - 1) and candles[i + 1] != candles[i]:
            break

    return tall_candles


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
