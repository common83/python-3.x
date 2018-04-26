#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import types
from itertools import combinations


class mulcyang(object):

    def result_function(self, list_str):
        village_count = list_str[0]
        post_count = list_str[1]
        village_poss = list_str[2:]
        dis = [[0 for col in range(village_count)] for row in range(village_count)]
        dp = [[0 for col in range(post_count)] for row in range(village_count)]

        for i in range(village_count):
            for j in range(i+1,village_count):
                dis[i][j] = dis[i][j - 1] + village_poss[j] - village_poss[int((i + j) / 2)]

        for i in range(village_count):
            dp[i][0] = dis[0][i]

        for j in range(1, post_count):
            for i in range(village_count):
                dp[i][j] = 9999999
                for k in range(0,i):

                    dp[i][j] = min(dp[k][j-1]+ dis[k+1][i],dp[i][j])
        return dp[village_count-1][post_count-1]




if __name__ == '__main__':
    print('最大值为：' + str(knapsack_dynamic(w, p, n, m, x)))
    print('物品的索引：', x)
    print(list(combinations(range(6),2)))
    print(max([1,2,3,4,5,6]))
    print(([[0 for col in range(2)] for row in range(3)]))

