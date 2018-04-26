#!/usr/bin/python
# -*- coding: UTF-8 -*-


class shamchen(object):

    """
    1、两个村庄和邮局的最小距离和是两个村庄之间的中位数，
    2、DP算法的核心是找到状态转移方程；
    在当前情况，令i个村庄建j个邮局的最小距离和为dp（i,j）,而i-1个村庄修j个邮局为
    dp（i-1,j），则有dp(i,j) = dp(k,j-1)+w(k+1,i),其中w(k+1,i)表示的是k+1到第i个村庄修1个邮局时的
    最小距离。
    K的大小范围为j-1<=k<=i-1
    """
    def result_function(self,all_list):
        village_sum = all_list[0]
        all_list.remove(village_sum)

        post_sum = all_list[0]
        all_list.remove(post_sum)
        w = [[0 for col in range(village_sum+1)] for row in range(village_sum+1)]

        for i in range(0,village_sum+1):
            for j in range(i+1,village_sum+1):
                median_list = all_list[i:j]
                w[i][j] = self.get_median(median_list)

        """
        按照邮局的个数来安排，在给定的区间以内，有1,2,3...j个邮局
        """
        for j in range(1,post_sum+1):
            for i in range(1,village_sum+1):
                for k in range(j-1,i):
                    return


    '''
    求中位数
    '''

    def get_median(self,data):
        data = sorted(data)
        size = len(data)
        if size % 2 == 0:  # 判断列表长度为偶数
            median = (data[size // 2] + data[size // 2 - 1]) / 2
            data[0] = median
        if size % 2 == 1:  # 判断列表长度为奇数
            median = data[(size - 1) // 2]
            data[0] = median
        return data[0]







if __name__ == '__main__':
    who_shamchen = shamchen()
    who_shamchen.result_function([10,5,1,2,3,6,7,9,11,22,44,50])