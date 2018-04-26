# __*__encoding=utf-8 __*__
import math


class kevindi(object):
    temp_list = []
    my_test = 0;

    # 获取某个节点的高度
    def get_depth_by_index(self, tree, index):
        d_left = 0
        d_right = 0
        if index * 2 + 2 > len(tree): # 叶子节点
            return 0
        print("index = ", index)

        # 左子树高度
        if tree[index*2 + 1] == "null":
            d_left = -1
        else:
            d_left = self.get_depth_by_index(tree, index*2+1)

        # 右子树高度
        if tree[index*2 + 2] == "null":
            d_right = -1
        else:
            d_right = self.get_depth_by_index(tree, index*2+2)

        print(tree[index],"=",max(d_left, d_right) + 1)
        return max(d_left, d_right) + 1

    # 判断某个节点是否为平衡二叉树
    def is_balance_tree(self, tree, index):
        if abs(self.get_depth_by_index(tree, 2*index+1) - self.get_depth_by_index(tree, 2*index + 2)) < 2:
            return True
        else:
            print("left = ", self.get_depth_by_index(tree, 2*index+1), "right = ",\
                  self.get_depth_by_index(tree, 2*index+2))
            return False


    # 入口函数
    def result_function(self, tree):
        if len(tree) < 4:
            return True

        # 遍历所有的子树
        #for i in range(int(math.log(len(tree), 2))):
        for i in range(len(tree)):
            if not self.is_balance_tree(tree, i):
                print("not Balance tree,",i)
                return False # 某个节点非平衡树
        # 所有节点都是平衡二叉树
        return True


# 打印数组构成的二叉树
def show_list_tree(tree):
    k = 0
    i = 0
    # print("2**k = ", 2 ** k)
    while i < len(tree):
        for j in range(2**k):  # 在同一个层级，不换行
            print(tree[i], " ", end='')
            i += 1
        else:
            # 换行，换下一个层级
            k += 1
            print("")
            # print("2**k = ", 2 ** k)

    print("------------------------")

if __name__ == '__main__':
    tmp_prime = kevindi()

    value = [1,2,2,3,3,'null','null',4,4]
    # show_list_tree(value)
    print(tmp_prime.result_function(value))

