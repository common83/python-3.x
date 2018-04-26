# __*__encoding=utf-8 __*__

class kevindi(object):
    temp_list = {}
    my_test = 0;

    # 计算所有可能的target
    def calcute_target(self, value):
        for i in range(len(value)):
            for j in range(i+1,len(value)):
                sum = value[i] + value[j]
                self.temp_list[sum] = [i, j]
        return

    # 查找分解元素的位置
    def result_function(self, value, target):
        self.temp_list.clear()
        self.calcute_target(value)

        if target in self.temp_list:
            return self.temp_list.get(target)
        else:
            return False

if __name__ == '__main__':
    tmp_prime = kevindi()

    value = [2,7,11,15]
    target = 9
    print(tmp_prime.result_function(value, target))


