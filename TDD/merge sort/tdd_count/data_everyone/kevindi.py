# __*__encoding=utf-8 __*__

def merge_sort(p_list):
    """
    归并算法
    Args:
        p_list:待归并的队列

    Returns:归并后的队列

    """
    if len(p_list) == 1:
        return True, p_list[0]
    r_list = []
    n = len(p_list)
    for i in range(0, n, 2): # 2个一组对p_list归并
        temp_list = []
        left_list = p_list[i][:]
        if i+1 < n: # 只有一组
            right_list = p_list[i + 1][:]
        else:
            right_list = []

        while left_list:
            if right_list: # 合并
                if left_list[0] <= right_list[0]:
                    temp_list.append(left_list.pop(0))
                else:
                    temp_list.append(right_list.pop(0))
            else: # 只有左侧list(右侧处理完，或者只有一组）
                temp_list.append(left_list.pop(0))
        if right_list: # 只有右侧list
            temp_list += right_list
        r_list.append(temp_list)
    return False, r_list


class kevindi(object):
    def result_function(self, value):
        print(value)
        n = len(value)
        p_list = []
        for i in value:
            temp_list = [i]
            p_list.append(temp_list)

        i_finish = False
        while not i_finish:
            i_finish, p_list = merge_sort(p_list)

        return p_list;


if __name__ == '__main__':
    tmp_prime = kevindi()

    value = [10, 3, 2, 5, 7, 8, 0, 1, 4, 6, 9]
    print(tmp_prime.result_function(value))



