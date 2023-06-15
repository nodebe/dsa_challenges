#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def timeConversion(s):
    # Write your code here
    pm_time_allocation = {12: 12}
    am_time_allocation = {12: '00'}
    total_time = 12

    for i in range(1, total_time):
        pm_time_allocation[i] = total_time + i

    pm_am_allocation = {'PM': pm_time_allocation, 'AM': am_time_allocation}

    pm_am_allocated = pm_am_allocation[s[-2:]]
    hour_mark = int(s[:2])

    if hour_mark != 12 and s[-2:] == 'AM':
        return s[:-2]

    equivalent_hour_mark = str(pm_am_allocated[hour_mark])
    new_s = equivalent_hour_mark + s[2:-2]

    return new_s


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
