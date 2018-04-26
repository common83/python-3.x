# __*__encoding=utf-8 __*__
import math

class HeapStack:
    """
    使用数组实现堆处理
    """
    def min_heap(self, a_list,n):
        """
        生成一个小堆
        Args:
            a_list: 输入数组
        Returns:
            返回小堆
        """
        # print("heap before: ", a_list)
        n = n-1
        j=1
        if n>1:
            j = int(math.log(n,2))
        for k in range(j):
            for i in range((n+1)//2):  # 生成小堆
                if a_list[i] > a_list[i*2+1]:
                    temp = a_list[i]
                    a_list[i] = a_list[i*2+1]
                    a_list[i*2+1] = temp
                if (2*i+2 <= n) and (a_list[i] > a_list[2*i+2]):
                    temp = a_list[i]
                    a_list[i] = a_list[2*i+2]
                    a_list[2*i+2 ] = temp
        # print("heap after:  ", a_list)
        return a_list

    def sort_heap(self, a_list):
        """
        从小到大排序堆
        Returns:
        排序后的堆
        """
        n = len(a_list)
        for i in range(n,0,-1):
            self.min_heap(a_list,i)
            # print("swap before:  ", a_list)
            temp = a_list[0]
            a_list[0] = a_list[i-1]
            a_list[i-1] = temp
            # print("swap after:   ", a_list)
        # print("sort: ", a_list)
        return a_list


class kevindi(object):
    def result_function(self, value):
        print(value)
        hs = HeapStack()
        hs.sort_heap(value)
        # print(value)
        return value;


if __name__ == '__main__':
    tmp_prime = kevindi()

    value = [10, 3, 2, 5, 7, 8, 0, 1, 4, 6, 9]
    print(tmp_prime.result_function(value))


