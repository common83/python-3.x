# -*- coding: utf-8 -*-

import math
import types

import itertools
import copy
from itertools import combinations
from itertools import permutations
from itertools import combinations_with_replacement


def printX(value1, value2):
    """
    简易 测试比较并打印
    :param value1:
    :param value2:
    :return:
    """
    str1 = str(value1)
    str2 = str(value2)
    if value1 == value2:
        print('ECHO (' + str1 + ' ' + str2 + ')')
    else:
        print('!!!!!!!!!NOT ECHO (' + str1 + ' ' + str2 + ')')


class haliluyafu(object):
    def result_function(self, num_list):
        """
        动态规划计算 如何建邮局问题
        :param num_list:
        :return:
        """
        village_num = num_list[0]
        post_num = num_list[1]
        village_pos = num_list[2:]
        print(village_pos)

        shortest_total_dis = 999999

        # 动态规划第一步 使用暴力计算法 计算出结果
        # 从所有村庄中选邮局
        combinations_post = combinations(village_pos, post_num)
        for one_combie in combinations_post:
            # 一种邮局位置的组合
            post_pos_list = list(one_combie)
            # print post_pos_list

            total_dis = 0

            # 计算村庄和邮局的总最小距离
            for one_village_pos in village_pos:
                shortest_dis = 999

                # 一个村庄和最近的邮局的距离
                for one_post_pos in post_pos_list:
                    temp_dis = abs(one_post_pos - one_village_pos)
                    if temp_dis < shortest_dis:
                        shortest_dis = temp_dis

                total_dis += shortest_dis
            # print total_dis

            if total_dis < shortest_total_dis:
                shortest_total_dis = total_dis

        return shortest_total_dis


if __name__ == '__main__':
    who_object = haliluyafu()

    printX(2, who_object.result_function([4, 2, 1, 2, 3, 55]))  #
    printX(4, who_object.result_function([5, 2, 1, 2, 3, 4, 55]))  #
    printX(3, who_object.result_function([5, 2, 1, 2, 3, 4, 5]))  #


