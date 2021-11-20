#!/bin/python3

import math
import os
import random
import re
import sys


def stdDev(arr):
    sMean = 0
    for i in range(len(arr)):
        sMean += arr[i]
    mean = sMean / len(arr)
    variance = 0
    for i in range(len(arr)):
        variance += math.pow((arr[i] - mean), 2)
    print(round((math.sqrt(variance / len(arr))), 1))


if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)
