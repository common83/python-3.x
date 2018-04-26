__author__ = 'vaconzhang'
"""
霍夫曼编码，参考：https://www.jianshu.com/p/4cbbfed4160b
"""

class HuffNode(object):
    def __init__(self, leaf_judge, value, weight, left_tree=None, right_tree=None):
        if leaf_judge:
            self.value = value
            self.weight = weight
            self.leaf = True
            self.left_tree = None
            self.right_tree = None
        else:
            self.value = None
            self.weight = left_tree.weight + right_tree.weight
            self.leaf = False
            self.left_tree = left_tree
            self.right_tree = right_tree

def get_char_weight(input_str):
    """
    获取输入字符串中每个字符的权重
    :param input_str:
    :return:
    """
    char_weight = {}
    for tmp_char in input_str:
        if tmp_char not in char_weight:
            char_weight[tmp_char] = 1
        else:
            char_weight[tmp_char] += 1
    return char_weight


def get_huff_node_leaf_list(input_str):
    """
    构造 以（只有叶子节点构造的霍夫曼树）的list
    @:param input_str：输入的字符串
    :return:
    """
    # 统计字符串中各字符出现的次数
    char_weight = get_char_weight(input_str)

    # 构造霍夫曼初始树list
    list_huff_leaf_nodes = []
    for x in char_weight:
        tem_tree = HuffNode(True, x, char_weight[x])  # 使用 HuffNode的构造函数 定义一棵只包含一个叶节点的Huffman树
        list_huff_leaf_nodes.append(tem_tree)
    return list_huff_leaf_nodes
    

def get_huff_tree(para_list_huff_leaf_nodes):
    """
    构建霍夫曼树
    :param para_list_huff_leaf_trees:  以（只有叶子节点构造的霍夫曼树）的list
    :return: 返回构造的霍夫曼树的根节点
    """
    while len(para_list_huff_leaf_nodes) > 1:
        para_list_huff_leaf_nodes.sort(key=lambda x: x.weight)
        tmp_left_tree = para_list_huff_leaf_nodes[0]
        tmp_right_tree = para_list_huff_leaf_nodes[1]
        para_list_huff_leaf_nodes = para_list_huff_leaf_nodes[2:]
        tmp_node_tree = HuffNode(False, None, None, tmp_left_tree, tmp_right_tree)
        para_list_huff_leaf_nodes.append(tmp_node_tree)
    return para_list_huff_leaf_nodes[0]


def traverse_huffman_tree(huff_tree_root, pre_code, char_code_dict):
    print(huff_tree_root)
    if huff_tree_root.leaf:
        print(huff_tree_root.value)
        char_code_dict[huff_tree_root.value] = pre_code
        return None
    else:
        traverse_huffman_tree(huff_tree_root.left_tree, "0" + pre_code, char_code_dict)
        traverse_huffman_tree(huff_tree_root.right_tree, "1" + pre_code, char_code_dict)
    
def get_code_dict(input_str):
    """
    获取霍夫曼编码码表
    @:param input_str: 待编码的字符串
    :return:
    """
    list_huff_leaf_trees = get_huff_node_leaf_list(input_str)
    root = get_huff_tree(list_huff_leaf_trees)
    char_code = {}
    traverse_huffman_tree(root, "", char_code)
    print(char_code)
    return char_code

def get_code_num(input_str):
    """
    获取字符串编码后的长度
    :param input_str: 输入的待编码的字符串
    :return: 返回编码后的码长
    """
    char_weight = get_char_weight(input_str)
    char_code = get_code_dict(input_str)
    code_num = 0
    for tmp_key in char_code:
        code_num += len(char_code[tmp_key]) * char_weight[tmp_key]
    # print(code_num)
    return code_num


class vaconzhang(object):
    def result_function(self, input_str):
        if input_str == "":
            return 0
        return get_code_num(input_str)

if __name__ == '__main__':
    tmp_vacon = vaconzhang()
    print(tmp_vacon.result_function("MT-TECH-TEAM"))
