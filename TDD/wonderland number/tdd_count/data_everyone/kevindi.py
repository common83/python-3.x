# __*__encoding=utf-8 __*__

class kevindi(object):
    temp_list = []
    my_test = 0;

    def check_with_digit(self,value,mutiply_number):
        value_str = str(value)
        value_list = list(value_str)
        value_2 = mutiply_number * value
        if value_2 > 999999:
            return False
        value_2_list = list(str(value_2))
        for i in range(6):
            k = value_list[i]
            if value_list.count(k) != value_2_list.count(k):
                return False

        #print(value_list,",,",value_2_list)
        for i in range(6):
            if value_list[i] == value_2_list[i]:
                return False
        #print(value_list, ",,", value_2_list)
        return True

    def check_with_number(self, value):
        value_str = str(value)
        if len(value_str) != 6:
            return False

        for i in range(2,7):
            if self.check_with_digit(value,i):
                return True
        return False


    def result_function(self):
        self.temp_list = []
        self.my_test = 0;

        for i in range(100000,1000000):
            if i * 2 > 1000000:
                break
            if self.check_with_number(i):
                self.temp_list.append(i)

        if self.temp_list:
            return self.temp_list
        else:
            return None

if __name__ == '__main__':
    tmp_prime = kevindi()

    print(tmp_prime.result_function())
    print(len(tmp_prime.result_function()))


