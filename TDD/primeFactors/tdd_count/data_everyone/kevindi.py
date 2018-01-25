# __*__encoding=utf-8 __*__
import sys
import math

class kevindi(object):
    prime_sun = [];
    prime_list = []

    def is_prime(self,value):
        #print("is_prime",value)
        if value == 2:
            self.prime_list.append(value)
            return True
        if value < 2:
            return False

        for i in range(2,value):
            if value%i == 0:
                return False
        self.prime_list.append(value)
        return True

    def get_min_prime(self, value):
        for i in range(2, int(math.sqrt(value))+1):
            if self.is_prime(i):
                if value%i == 0:
                    self.prime_sun.append(i)
                    return int(value/i)

        self.prime_sun.append(value)
        return 0

    def result_function(self, value):
        self.prime_sun = [];
        self.prime_list = []
        if value == 1:
            return [1]
        if value == 2:
            return [2]
        prime = self.get_min_prime(value);
        while prime:
            prime = self.get_min_prime(prime)

        return self.prime_sun;


if __name__ == '__main__':
    tmp_prime = kevindi()

    #print(sys.maxsize)
    value = 4
    print(tmp_prime.result_function(value))


