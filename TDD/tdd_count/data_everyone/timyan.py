#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/24 10:49
# @Author  : crrlxx
# @contact: @gmail.com
# @Site    :
# @File    : test_hiker.py
# @Software: PyCharm Community Edition
from itertools import combinations
import sys


class timyan(object):

    def result_function(self, inarr):
        arr = []
        num = 0
        num = inarr[1]
        arr = inarr[2:]
        if arr == None or len(arr) == 0 or num < 1 or len(arr) < num:
            return 0
        w = [[0 for i in range(len(arr))] for j in range(len(arr))]
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                w[i][j] = w[i][j - 1] + arr[j] - arr[(i + j) // 2]
        dp = [w[0][i] for i in range(len(arr))]
        for i in range(1, num):
            for j in range(len(arr) - 1, i - 1, -1):
                minDistance = sys.maxsize
                for k in range(i - 1, j):
                    minDistance = min(minDistance, max(dp[k], w[k + 1][j]))
                dp[j] = minDistance
        return dp[-1]


if __name__ == '__main__':
    tmp_prime = timyan()
