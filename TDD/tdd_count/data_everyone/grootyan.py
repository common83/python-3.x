import os
import sys

class Node:
    def isLeft(self):
        return self.father.left == self
    def get_pin_lv(self):
        return self.pin_lv

def createNodes(pin_lvs):
    return [Node(pin_lv) for pin_lv in pin_lvs]


def createHuffmanTree(nodes):
    queue = nodes[:]
    while len(queue) > 1:
        queue.sort(key=lambda item:item.pin_lv)
        node_left = queue.pop(0)
        node_right = queue.pop(0)
        node_father = Node(node_left.pin_lv + node_right.pin_lv)
        node_father.left = node_left
        node_father.right = node_right
        node_left.father = node_father
        node_right.father = node_father
        queue.append(node_father)
    queue[0].father = None
    return queue[0]

def huffmanEncoding(nodes,root):
    codes = [''] * len(nodes)
    for i in range(len(nodes)):
        node_tmp = nodes[i]
        while node_tmp != root:
            if node_tmp.isLeft():
                codes[i] = '0' + codes[i]
            else:
                codes[i] = '1' + codes[i]
            node_tmp = node_tmp.father
    return codes



class grootyan(object):

    def strDic(self,str):
        dic = {}
        for i in str:
            if dic.has_key(i):
                dic[i] += 1
            else:
                dic[i] = 1
        #dic = sorted(dic.items(), key=lambda d: d[1])
        return dic

    def result_function(self, str):
        in_dic = self.strDic(str)
        if len(in_dic) < 2:
            return len(in_dic)*len(str)
        nodes = createNodes([item[1] for item in in_dic.items()])
        root = createHuffmanTree(nodes)
        codes = huffmanEncoding(nodes, root)
        ret = 0
        for item in range(len(nodes)):
            ret += (len(codes[item])*nodes[item].get_pin_lv())

        return ret



if __name__ == '__main__':
    demo =  grootyan()
    #!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import types
from itertools import combinations



class Node:
    def __init__(self,word_pinlv):
        self.left = None
        self.right = None
        self.father = None
        self.word_pinlv = word_pinlv
    def isLeft(self):
        return self.father.left == self
    def get_word_pinlv(self):
        return self.word_pinlv

def createNodes(word_pinlvs):
    return [Node(word_pinlv) for word_pinlv in word_pinlvs]

def huffmanEncoding(nodes,root):
    codes = [''] * len(nodes)
    for i in range(len(nodes)):
        node_tmp = nodes[i]
        while node_tmp != root:
            if node_tmp.isLeft():
                codes[i] = '0' + codes[i]
            else:
                codes[i] = '1' + codes[i]
            node_tmp = node_tmp.father
    return codes

def createHuffmanTree(nodes):
    queue = nodes[:]
    while len(queue) > 1:
        queue.sort(key=lambda item:item.word_pinlv)
        node_left = queue.pop(0)
        node_right = queue.pop(0)
        node_father = Node(node_left.word_pinlv + node_right.word_pinlv)
        node_father.left = node_left
        node_father.right = node_right
        node_left.father = node_father
        node_right.father = node_father
        queue.append(node_father)
    queue[0].father = None
    return queue[0]


class grootyan(object):

    def strDic(self,str):
        dic = {}
        for i in str:
            if dic.has_key(i):
                dic[i] += 1
            else:
                dic[i] = 1
        #dic = sorted(dic.items(), key=lambda d: d[1])
        return dic

    def result_function(self, str):
        in_dic = self.strDic(str)
        if len(in_dic) < 2:
            return len(in_dic)*len(str)
        nodes = createNodes([item[1] for item in in_dic.items()])
        root = createHuffmanTree(nodes)
        codes = huffmanEncoding(nodes, root)
        ret = 0
        for item in range(len(nodes)):
            ret += (len(codes[item])*nodes[item].get_word_pinlv())

        return ret



if __name__ == '__main__':
    str_to_code =  grootyan()
    strCoding= str_to_code.result_function('_______')
    print(strCoding)
