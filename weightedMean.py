#!/bin/python3

import math
import os
import random
import re
import sys



def weightedMean(X, W):
    # Write your code here
    prod = 0
    wSum = 0
    for i in range(len(X)):
        prod += X[i]*W[i]
        wSum += W[i]
    print(round((prod/wSum),1))

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    weights = list(map(int, input().rstrip().split()))

    weightedMean(vals, weights)
