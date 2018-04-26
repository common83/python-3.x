# __*__encoding=utf-8 __*__

class kevindi(object):

    # 该行最大值
    def get_max_in_row(self,value,i):
        i = 5 * i
        k = max(value[i:i + 5])
        return k

    # j是不是该列最小值
    def is_min_value_in_colum(self,value,j):
        k = value[j]
        j = j%5
        while j < 25:
            if value[j] <k:
                return False
            j +=5
        return True


    def result_function(self, value):
        if len(value) != 25:
            return "error input"+str(len(value))
        temp_list = []
        for i in range(5):
            k = self.get_max_in_row(value,i)
            for j in range(5 * i, 5 * i + 5):
                if value[j] == k:
                    if self.is_min_value_in_colum(value,j):
                        temp_list.append(j)
        if temp_list:
            return temp_list
        else:
            return "No saddle points"


if __name__ == '__main__':
    tmp_prime = kevindi()

    value = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1 ]
    print(tmp_prime.result_function(value))


