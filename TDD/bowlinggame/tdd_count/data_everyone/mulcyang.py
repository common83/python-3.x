__author__ = 'mulcyang'
import math
import types
import copy
import sys
from itertools import combinations


class mulcyang(object):

    def one_qiu_scr(self,index,scor_str):
        if scor_str[index].isdigit():
            return int(scor_str[index])
        elif scor_str[index] == 'X':
            return 10
        elif scor_str[index] == '/':
            return (10-int(scor_str[index-1]))
        else:
            return 0

    def result_function(self, scor_str):
        scor = 0
        scors = scor_str.split("||")
        scor_str = ''
        scor_grop = scors[0].replace('|','')
        for str in scors:
            scor_str += str.replace('|','')
        print(scor_str)
        print(scor_grop)
        for i in range(len(scor_grop)):
            if scor_grop[i].isdigit():
                scor += int(scor_grop[i])
            else:
                if scor_grop[i] == 'X':
                    scor += self.one_qiu_scr(i,scor_str)
                    scor += self.one_qiu_scr(i+1,scor_str)
                    scor += self.one_qiu_scr(i+2,scor_str)
                elif scor_grop[i] == '/':
                    scor += self.one_qiu_scr(i,scor_str)
                    scor += self.one_qiu_scr(i+1,scor_str)
            print(scor)


        return scor


if __name__ == '__main__':
    str = 'aaaabbbb'
    new = str.replace('a','')
    print(str)
    print(new)
    print(sys.maxsize)
