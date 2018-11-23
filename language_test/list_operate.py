import math


def list_range():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    for i in range(12+1):
        if i<5:
            continue
        else:
            print(i, "=", a[i-5:i])

    r = sum(a[1:3])
    print(r)
list_range()
class Tdel:
    a = []

    def add_item(self):
        for i in range(5):
            self.a.append(i)

    def clear_item(self):
        if self.a:
            self.a.clear()
        # self.a = []

    def print_item(self):
        print(self.a)


def list_del():
    b = []
    a = Tdel()
    a.add_item()
    a.print_item()
    a.clear_item()
    a.print_item()


# list_del()
# list_del()
#list_range()
def check_range():
    for i in range(2,7):
        print(i)

def show_tree(list_tree):
    level_nume = len(list_tree)
    max_nodes_one_level = 1

    if level_nume > 1:
       max_nodes_one_level = 2 * (level_nume-1)

    for node_list in list_tree:
        node_str = str(node_list)
        print(node_str.center(max_nodes_one_level * 4 + 1,'_'))
        print("")

def list_to_str_list(int_list):
    s = []
    for i in int_list:
        s.append(str(i))
    return s


def binary_tree(n):
    list_tree = []
    d = 1 # 每层的节点数
    i = 1
    while i < n:
        list_node = []
        for k in range(d): # 该层有多少节点
            if i < n: # 数组未越界
                list_node.append(i)
                i += 1
        list_tree.append(list_node)
        d *= 2

    print(list_tree)
    show_tree(list_tree)



def test_join():
    int_list = [1,2,3,4,5]
    print(type(int_list))
    try:
        s1 = "".join(int_list)
        print(s1)
    except:
        print("error for int type in int_list")

    str_list = ['1','2','3']
    try:
        s2 = "".join(str_list)
        print(s2)
    except:
        print("error for int type in int_list")

    temp_str = str(int_list)
    print("Error str function:",temp_str)

    s3 = ""
    for i in int_list:
        s3 += str(i)
    print("list to string:",s3)


# 打印数组构成的二叉树
def show_list_tree(tree):
    k = 0
    i = 0
    # print("2**k = ", 2 ** k)
    print("k=",k)
    while i < len(tree):
        for j in range(2**k):  # 在同一个层级，不换行
            print(tree[i], " ", end='')
            i += 1
        else:
            # 换行，换下一个层级
            k += 1
            print("")
            print("k=", k)
            # print("2**k = ", 2 ** k)


def get_depth_by_index(tree, index):
    d_left = 0
    d_right = 0
    if index * 2 + 2 > len(tree):  # 叶子节点
        return 0
    # print("index = ", index)

    # 左子树高度
    if tree[index * 2 + 1] == "null":
        d_left = -1
    else:
        d_left = get_depth_by_index(tree, index * 2 + 1)

    # 右子树高度
    if tree[index * 2 + 2] == "null":
        d_right = -1
    else:
        d_right = get_depth_by_index(tree, index * 2 + 2)

    # print(tree[index], "=", max(d_left, d_right) + 1)
    return max(d_left, d_right) + 1


# a = [n for n in range(2**4-1)]
# print(a)

# show_list_tree(a)
# print("dept")
# for i in range(20):
#     print(i,"=",get_depth_by_index(a,i))



# binary_tree(a)
# b = int(math.log(a,2))
# print(b)
# # test_join()

# 数组合并
list_a = [1,2,3,4]
list_b = [4,5,6,7]
list_c = list_a + list_b
print("merge",list_c)

list_a.extend(list_b)
print("merge", list_a)

list_a.append(list_b)
print("merge", list_a)

list_a += list_b
print("merge",list_a)

