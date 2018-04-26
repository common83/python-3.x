# __*__encoding=utf-8 __*__

class kevindi(object):
    temp_list = []
    my_test = 0;
    village_number = 0
    office_number = 0

    def get_space(self, village_value, i):
        v = len(village_value)
        s1 = i*village_value[i] - sum(village_value[:i])
        s2 = sum(village_value[i:]) - (v - i)*village_value[i]
        s = s1 + s2
        return s


    def get_office_distance(self,v, p, village_value):
        i = v//2
        p = i
        s = self.get_space(village_value,i)
        j = i -1
        while j > 0:
            s1 = self.get_space(village_value,j)
            if s1 < s:
                s = s1
                p = j
                j -= 1
            else:
                break
        j = i+1
        while j < v-1:
            s2 = self.get_space(village_value,j)
            if s2 < s:
                s = s2
                p = j
                j += 1
            else:
                break
        print("office =",village_value[p],"distance=",s)
        return s

    def result_function(self, param_value):
        self.village_number = param_value[0]
        self.office_number = param_value[1]
        if not self.office_number < self.village_number:
            return 0
        if not 1 <= self.office_number <= 30:
            return 0
        if not 1 <= self.village_number <= 300:
            return 0

        office_number = 1
        max_len = self.get_office_distance(self.village_number, office_number, param_value[2:])
        return max_len


if __name__ == '__main__':
    tmp_prime = kevindi()

    param_value = [10,5,1,2,3,6,7,9,11,22,44,50]
    print(tmp_prime.result_function(param_value))

    param_value = [6,1,1,2,3,4,5,6]
    print(tmp_prime.result_function(param_value))


