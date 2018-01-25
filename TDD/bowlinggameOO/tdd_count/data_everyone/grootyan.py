# __*__encoding=utf-8 __*__

import math
import types

class grootyan(object):

    def result_function(self, number):


        if not isinstance(number, type(1)):
            print("Type error please input IntType numberx")
            return []
        if number <= 0:
            print("please input postive number")
            return []
        result_parse_prime_number = []
        if number == 1:
            return [1]
        if self.judge_prime_number(number):
            return [1, number]
        else:
            x_tmp = 2
            while x_tmp < math.sqrt(number) + 1:
                if number % x_tmp == 0:
                    result_parse_prime_number.append(x_tmp)
                    number /= x_tmp
                    if self.judge_prime_number(int(number)):
                        result_parse_prime_number.append(int(number))
                        return result_parse_prime_number
                else:
                    x_tmp += 1

    def judge_prime_number(self, number):


        if not isinstance(number, type(1)):
            print("Type error please input IntType numbery")
            return None
        if number <= 0:
            print("please input postive number")
            return None

        if number in (2, 3, 5, 7, 11):
            return True
        elif number in (1, 4) or number % 2 == 0:
            return False
        for x_tmp in range(int(math.sqrt(number))+1)[2:]:
            if number % x_tmp == 0:
                return False
        return True


    def get_all_prime_number(self, number):

        if not isinstance(number, type(1)):
            print("Type error please input IntType numberz")
            return []
        if number <= 0:
            print("please input postive number")
            return []
        result_prime_list = []
        for x_tmp in range(number+1):
            if self.judge_prime_number(x_tmp):
                result_prime_list.append(x_tmp)
        return result_prime_list


if __name__ == '__main__':
    tmp_prime = grootyan()
    print("1:", tmp_prime.result_function(1))
    print("4:", tmp_prime.result_function(4))
    print("6:", tmp_prime.result_function(6))
    print("8:", tmp_prime.result_function(8))
    print("9:", tmp_prime.result_function(9))
    print("10:", tmp_prime.result_function(10))
    print("12:", tmp_prime.result_function(12))
    print("14:", tmp_prime.result_function(14))
    print("15:", tmp_prime.result_function(15))
    print("16:", tmp_prime.result_function(16))
    print("17:", tmp_prime.result_function(17))
    print("18:", tmp_prime.result_function(18))
    print("19:", tmp_prime.result_function(19))
    print("20:", tmp_prime.result_function(20))
    print("21:", tmp_prime.result_function(21))
    print("22:", tmp_prime.result_function(22))
    print("23:", tmp_prime.result_function(23))
