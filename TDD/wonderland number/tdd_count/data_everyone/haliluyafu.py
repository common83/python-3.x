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
        print 'ECHO (' + str1 + ' ' + str2 + ')'
    else:
        print '!!!!!!!!!NOT ECHO (' + str1 + ' ' + str2 + ')'


class haliluyafu(object):
    def get_num_list(self, num):
        """
        根据数字得到字符列表
        :param num:
        :return:
        """
        num_list = []
        temp_str = str(num)
        for c in temp_str:
            num_list.append(c)
        num_list.sort()
        return num_list

    def check_multi_num(self, num, num_list):
        pass
        num2 = num * 2
        if num2 != num:
            num_list2 = self.get_num_list(num2)
            if num_list2 == num_list:
                print str(num) + '_' + 'X2' + '=' + str(num2)
                return True

        num3 = num * 3
        if num3 != num:
            num_list3 = self.get_num_list(num3)
            if num_list3 == num_list:
                print str(num) + '_' + 'X3' + '=' + str(num3)
                return True

        num4 = num * 4
        if num4 != num:
            num_list4 = self.get_num_list(num4)
            if num_list4 == num_list:
                print str(num) + '_' + 'X4' + '=' + str(num4)
                return True

        num5 = num * 5
        if num5 != num:
            num_list5 = self.get_num_list(num5)
            if num_list5 == num_list:
                print str(num) + '_' + 'X5' + '=' + str(num5)
                return True

        num6 = num * 6
        if num6 != num:
            num_list6 = self.get_num_list(num6)
            if num_list6 == num_list:
                print str(num) + '_' + 'X6' + '=' + str(num6)
                return True

        return False

    def result_function(self, num_list):
        final_num_list = []
        for i in range(100000, 1000000):
            num_list = self.get_num_list(i)
            if self.check_multi_num(i, num_list):
                final_num_list.append(i)

        for item in final_num_list:
            print item
        return len(final_num_list)


if __name__ == '__main__':
    who_object = haliluyafu()
    # list1 = ['0', '0', '0', '1', '1', '1']
    # list2 = ['0', '0', '0', '1', '1']
    # list2.append('1')
    # print list1 == list2

    printX(246, who_object.result_function('any'))  #
