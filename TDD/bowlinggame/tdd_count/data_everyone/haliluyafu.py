# -*- coding: utf-8 -*-

import math
import types

import itertools
import copy
from itertools import combinations
from itertools import permutations
from itertools import combinations_with_replacement

"""
保龄球的计分不难，每一局总共有十格，每一格里面有两球。共有十支球瓶，要尽量在两球之内把球瓶全部击倒，
如果第一球就把全部的球瓶都击倒了，也就是“STRIKE”，画面出现“X”，就算完成一格了，所得分数就是10分
再加下两球的倒瓶数，但是如果第一球没有全倒时，就要再打一球，如果剩下的球瓶全都击倒，也就是“SPARE”，
画面出现“/”，也算完成一格，所得分数为10分再加下一格第一球的倒瓶数，但是如果第二球也没有把球瓶全部击
倒的话，那分数就是第一球加第二球倒的瓶数，再接着打下一格。依此类推直到第十格。但是第十格有三球，第十格
时如果第一球或第二球将球瓶全部击倒时，可再加打第三球。
"""



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


class bowling_score:
    """
    保龄球计分类，记录每一组内的得分
    """
    original_str = ''  # 最初得到的原始分数字符串

    state = ''  # 本组状态  strike、spare、miss ，需要自身计算得到
    init_score = 0  # 本组初始分， 需要自身计算得到

    final_score = 0  # 本组“加权”得分，需要全局计算得到
    my_index = 0  # 我属于第几组
    next_one_score = 0
    next_two_score = 0


class haliluyafu(object):
    score_list = []  # 存放计分列表

    def read_string_to_data(self, ori_str):
        """
        读取字符串 解析到内部的数据结构中
        :param str:
        :return:
        """
        self.score_list = []  # 每次读取时清空旧的数据
        temp_str_ary = ori_str.split('||')  # 前面10组球与最后的奖励球用||分割
        before_str = temp_str_ary[0]
        after_str = temp_str_ary[1]
        print(before_str)
        print(after_str)
        one_to_ten_score_ary = before_str.split('|')
        # 循环处理 1-10球的分数
        for i, one_original_score in enumerate(one_to_ten_score_ary):
            one_score = bowling_score()
            one_score.original_str = one_original_score
            one_score.my_index = i
            self.score_list.append(one_score)
        # 处理最后的奖励分
        last_score = bowling_score()
        last_score.original_str = after_str
        last_score.my_index = 10
        self.score_list.append(last_score)

    def caclulate_final_score(self):
        """
        检查计算每组最终得分
        :return:
        """
        # 还没有赋值的情况
        if len(self.score_list) == 0:
            return 0
        for one_score in self.score_list:
            if one_score.state == 'bonus':  # 奖励球没有“加权”
                continue
            if one_score.state == 'lessten':  # 不用“加权”跳过
                continue
            if one_score.state == 'strike':
                # 查找后续两个球
                one_score.final_score = one_score.init_score + self.get_next_two_ball_num(one_score.my_index + 1)
                continue
            if one_score.state == 'spare':
                # 查找后续一个球
                one_score.final_score = one_score.init_score + self.get_next_one_ball_num(one_score.my_index + 1)

    def get_next_two_ball_num(self, index):
        """
        获取指定序号后面的两个球的分数
        :param index:
        :return:
        """
        score1 = 0
        score2 = 0
        the_len = len(self.score_list)
        if index > the_len - 1:  # 查询的是下一组，最后一组不存在后面的组
            return 0
        else:
            one_score = self.score_list[index]  # 获取下一组的
            if one_score.state == 'strike':  # 本组为X ，返回本组的10 和下组的第一球分数
                score1 = 10
                if self.score_list[index + 1].original_str[0] == 'X':
                    score2 = 10
                if self.score_list[index + 1].original_str[0] == '-':
                    score2 = 0
                if self.score_list[index + 1].original_str[0] in '123456789':
                    score2 = int(self.score_list[index + 1].original_str[0])
            if one_score.state == 'spare':  # 本组为/ ，返回10即可
                score1 = 0
                score2 = 10
            if one_score.state == 'bonus':  # 本组为奖励球
                score1 = 0
                score2 = one_score.final_score  # 直接用计算好的本组分组即可
            if one_score.state == 'lessten':
                score1 = 0
                score2 = one_score.final_score  # 直接用计算好的本组分组即可
            return score1 + score2


    def get_next_one_ball_num(self, index):
        """
        获取指定序号后面的一个球的分数
        :param index:
        :return:
        """
        the_len = len(self.score_list)
        if index > the_len - 1:  # 查询的是下一组，最后一组不存在后面的组
            return 'error index'
        else:
            one_score = self.score_list[index]  # 获取下一组的
            first_score = one_score.original_str[0]  # 1-10组 与 奖励组 对第一球无差别判断
            # 第一球只能是 '-' 'X' '5' 三类
            if first_score == 'X':
                return 10
            elif first_score == '-':
                return 0
            else:
                return int(first_score)

    def caclulate_every_score(self):
        """
        计算内部每组内的未加权得分  init_score  和 得分类别 state
        得分字符串的组合
        X --strike 一球全倒 以X字符可以识别
        7/ -- spare 两球全倒 以/字符可以识别
        -  -- miss 某次未击中
        最终没有全倒 有分为多种 ，但是必然不含 / 不含X
        7-
        -7
        --
        13

        :return:
        """
        # 还没有赋值的情况
        if len(self.score_list) == 0:
            return 0
        for one_score in self.score_list:
            if one_score.my_index < 10:  # 前面的基础球
                if one_score.original_str == 'X':
                    one_score.state = 'strike'
                    one_score.init_score = 10
                    continue
                if one_score.original_str.find('/') != -1:
                    one_score.state = 'spare'
                    one_score.init_score = 10
                    continue
                # 两球和小于10 的组合，奖励球可能只有一个,
                one_score.state = 'lessten'
                num_list = list(one_score.original_str)
                for part_score in num_list:  # 只能是 中划线或者数字
                    if part_score == '-':
                        one_score.init_score += 0
                    else:
                        one_score.init_score += int(part_score)
                one_score.final_score = one_score.init_score  # 小于10球 不用“加权”
            else:
                # 奖励球分数只有 数字、中划线、X，不存在 /
                one_score.state = 'bonus'
                num_list = list(one_score.original_str)
                for part_score in num_list:
                    if part_score == '-':
                        one_score.init_score += 0
                    elif part_score == 'X':
                        one_score.init_score += 10
                    else:
                        one_score.init_score += int(part_score)
                one_score.final_score = one_score.init_score  # 奖励球 不用“加权”

    def get_score_str(self, index):
        """
        打印解析后得到的 某一组计分的原始字符串 比如 '8/'
        可测试性函数 打印中间过程
        :param index:
        :return:
        """
        the_len = len(self.score_list)
        if index > the_len:
            return 'error index'
        else:
            return self.score_list[index - 1].original_str

    def get_final_score(self, index):
        """
        返回某一组击球 自身 “加权”的分数
        :param index:
        :return:
        """
        the_len = len(self.score_list)
        if index > the_len:
            return 'error index'
        else:
            return self.score_list[index - 1].final_score

    def get_init_score(self, index):
        """
        返回某一组击球 自身 未“加权”的分数
        :param index:
        :return:
        """
        the_len = len(self.score_list)
        if index > the_len:
            return 'error index'
        else:
            return self.score_list[index - 1].init_score

    def get_state(self, index):
        """
        返回某一球 的状态
        :param index:
        :return:
        """
        the_len = len(self.score_list)
        if index > the_len:
            return 'error index'
        else:
            return self.score_list[index - 1].state

    def get_total_score(self):
        """
        返回总共分数
        :return:
        """
        score = 0
        for one_score in self.score_list:
            score += one_score.final_score
        score -= self.score_list[-1].final_score  # 奖励球的计分在第10组中，规则不会把奖励球单独再算一次
        return score

    def result_function(self, ori_str):
        """
        保龄球得分计算
        :param ori_str:原始得分 字符串
        :return: 得分 整数
        """

        self.read_string_to_data(ori_str)
        self.caclulate_every_score()
        self.caclulate_final_score()
        return self.get_total_score()


if __name__ == '__main__':
    who_object = haliluyafu()
    printX(157, who_object.result_function('1/|2/|3/|4/|5/|6/|7/|8/|9/|8/||5'))  # 全spare
    printX('5/', who_object.get_score_str(5))
    printX(6, who_object.get_next_one_ball_num(5))
    printX(10, who_object.get_next_two_ball_num(5))

    printX('8/', who_object.get_score_str(10))  # 测试原始每组字符串截取
    printX(10, who_object.get_init_score(10))  # 测试每组本身计分
    printX('spare', who_object.get_state(10))  # 测试每组本身状态
    printX(5, who_object.get_next_one_ball_num(10))  # 测试获取下一球分数
    printX('error index', who_object.get_next_one_ball_num(11))

    printX('5', who_object.get_score_str(11))
    printX(137, who_object.result_function('X|7/|9-|X|-8|8/|-6|--|X|X||81'))  # 全spare
    printX('-8', who_object.get_score_str(5))
    printX(8, who_object.get_init_score(5))
    printX('lessten', who_object.get_state(5))
    printX(8, who_object.get_next_one_ball_num(10))
    printX(9, who_object.get_next_two_ball_num(10))  # 测试获取下两球分数
    printX(19, who_object.get_final_score(10))  # 测试获取某组最终“加权”得分

    printX('X', who_object.get_score_str(10))
    printX(10, who_object.get_init_score(10))
    printX('strike', who_object.get_state(10))

    printX('81', who_object.get_score_str(11))
    printX(9, who_object.get_init_score(11))
    printX('bonus', who_object.get_state(11))

    printX(142, who_object.result_function('X|7/|9-|X|-8|8/|-6|--|X|X||X2'))  # 全spare
    printX('X2', who_object.get_score_str(11))
    printX(12, who_object.get_init_score(11))
    printX('bonus', who_object.get_state(11))
    printX(0, who_object.get_next_one_ball_num(7))
    printX(10, who_object.get_next_one_ball_num(10))
    printX(12, who_object.get_next_two_ball_num(10))  # 测试获取下两球分数
    printX(20, who_object.get_next_two_ball_num(9))  # 测试获取下两球分数
    printX(10, who_object.get_next_two_ball_num(1))  # 测试获取下两球分数
    printX(8, who_object.get_next_two_ball_num(4))  # 测试获取下两球分数
    printX(20, who_object.get_final_score(1))  # 测试获取某组最终“加权”得分
    printX(19, who_object.get_final_score(2))  # 测试获取某组最终“加权”得分
    printX(9, who_object.get_final_score(3))  # 测试获取某组最终“加权”得分
    printX(18, who_object.get_final_score(4))  # 测试获取某组最终“加权”得分
    printX(8, who_object.get_final_score(5))  # 测试获取某组最终“加权”得分
    printX(10, who_object.get_final_score(6))  # 测试获取某组最终“加权”得分
    printX(6, who_object.get_final_score(7))  # 测试获取某组最终“加权”得分
    printX(0, who_object.get_final_score(8))  # 测试获取某组最终“加权”得分
    printX(30, who_object.get_final_score(9))  # 测试获取某组最终“加权”得分
    printX(22, who_object.get_final_score(10))  # 测试获取某组最终“加权”得分

    print(300, who_object.result_function('X|X|X|X|X|X|X|X|X|X||XX'))  # 全strike
    printX(30, who_object.get_final_score(1))  # 测试获取某组最终“加权”得分
    printX(30, who_object.get_final_score(10))  # 测试获取某组最终“加权”得分
    printX(20, who_object.get_final_score(11))  # 测试获取某组最终“加权”得分

    printX(19, who_object.result_function('--|-1|--|-1|--|-1|--|--|--|X||-6'))  # 奖励球两次
    printX('-6', who_object.get_score_str(11))
    printX(6, who_object.get_init_score(11))
    printX('bonus', who_object.get_state(11))

    printX(22, who_object.result_function('--|-1|--|-1|--|-1|--|--|--|5/||9'))  # 奖励球一次
    printX('9', who_object.get_score_str(11))
    printX(9, who_object.get_init_score(11))
    printX('bonus', who_object.get_state(11))
    # print([3,5], who_object.result_function(15))

    printX(8, who_object.result_function('--|-1|--|-1|--|-1|--|--|--|5-||'))  # 奖励球0次
