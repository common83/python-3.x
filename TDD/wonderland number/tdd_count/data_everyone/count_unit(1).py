# coding: utf-8
__author__ = 'vaconzhang'
import unittest


class count_unit(unittest.TestCase):
    def public_same(self, who_object):
        self.assertEqual([], who_object.result_function(1.2))
        self.assertEqual([], who_object.result_function(-1))
        self.assertEqual([], who_object.result_function(0))
        self.assertEqual([1], who_object.result_function(1))
        self.assertEqual([2, 2], who_object.result_function(4))
        self.assertEqual([2, 3], who_object.result_function(6))
        self.assertEqual([2, 2, 2], who_object.result_function(8))
        self.assertEqual([3, 3], who_object.result_function(9))
        self.assertEqual([2, 5], who_object.result_function(10))
        self.assertEqual([2, 2, 3], who_object.result_function(12))
        self.assertEqual([2, 7], who_object.result_function(14))
        self.assertEqual([3, 5], who_object.result_function(15))
        self.assertEqual([2, 2, 2, 2], who_object.result_function(16))
        self.assertEqual([1, 17], who_object.result_function(17))
        self.assertEqual([2, 3, 3], who_object.result_function(18))
        self.assertEqual([1, 19], who_object.result_function(19))
        self.assertEqual([2, 2, 5], who_object.result_function(20))
        self.assertEqual([3, 7], who_object.result_function(21))
        self.assertEqual([2, 11], who_object.result_function(22))
        self.assertEqual([1, 23], who_object.result_function(23))



def string_equal(ref, hyp):
    if len(ref) != len(hyp):
        return False
    for st in hyp:
        try:
            index_num = ref.index(st)
        except:
            return False
        print (index_num)
        if index_num >= 0:
            if index_num < len(ref):
                ref = ref[:index_num] +ref[index_num+1:]
            else:
                ref = ref[:index_num]
        else:
            return False
    return True



if __name__ == '__main__':


    number = 100000
    count = 0

    while number < 500000 :
        if string_equal(str(number), str(number*2)):
            count += 1
            # print number
        elif string_equal(str(number), str(number*3)):
            count += 1
            # print number
        elif string_equal(str(number), str(number*4)):
            count += 1
            # print number
        elif string_equal(str(number), str(number*5)):
            count += 1
            # print number
        elif string_equal(str(number), str(number*6)):
            count += 1
            print (number)

        number += 1
    print(count)


    print(string_equal("abcd","zcdb"))