# __*__encoding=utf-8 __*__

class kevindi(object):
    temp_list = []
    my_test = 0;
    def get_left_max_palindrome(self,value):
        n = len(value)
        if n == 1:
            return 1
        max_palindrome_string = ""
        for i in range(n):
            j = n - 1
            k = i
            palindrome_string_l = ""
            palindrome_string_r = ""
            while k <= j:
                if value[k] == value[j]:
                    if k != j:
                        palindrome_string_l = palindrome_string_l + value[k]
                        palindrome_string_r = value[j] + palindrome_string_r
                    else:
                        palindrome_string_l = palindrome_string_l + value[k]
                    k += 1
                    j -= 1
                else:
                    j -= 1
            if len(palindrome_string_l + palindrome_string_r) > len(max_palindrome_string):
                max_palindrome_string = palindrome_string_l + palindrome_string_r;
                print("palindrome str=", max_palindrome_string)
        print("max str = ", max_palindrome_string)
        return max_palindrome_string


    def get_right_max_palindrome(self,value):
        n = len(value)
        if n == 1:
            return 1
        max_palindrome_string = ""
        for i in range(n):
            j = n - 1
            k = i
            palindrome_string_l = ""
            palindrome_string_r = ""
            while k <= j:
                if value[k] == value[j]:
                    if k != j:
                        palindrome_string_l = palindrome_string_l + value[k]
                        palindrome_string_r = value[j] + palindrome_string_r
                    else:
                        palindrome_string_l = palindrome_string_l + value[k]
                    k += 1
                    j -= 1
                else:
                    k += 1
            if len(palindrome_string_l + palindrome_string_r) > len(max_palindrome_string):
                max_palindrome_string = palindrome_string_l + palindrome_string_r;
                print("palindrome str=", max_palindrome_string)
        print("max str = ", max_palindrome_string)
        return max_palindrome_string

    def get_max_palindrome(self,value):
        n = len(value)
        if n == 1:
            return 1
        max_palindrome_string = ""
        for i in range(n):
            j = n - 1
            k = i
            palindrome_string_l = ""
            palindrome_string_r = ""
            while k <= j:
                if value[k] == value[j]:
                    if k != j:
                        palindrome_string_l = palindrome_string_l + value[k]
                        palindrome_string_r = value[j] + palindrome_string_r
                    else:
                        palindrome_string_l = palindrome_string_l + value[k]
                    k += 1
                    j -= 1
                else:
                    k += 1
                    self.get_max_palindrome(value[k:j])
                    j -= 1
                    self.get_max_palindrome(value[k:j])
            if len(palindrome_string_l + palindrome_string_r) > len(max_palindrome_string):
                max_palindrome_string = palindrome_string_l + palindrome_string_r;
                print("palindrome str=", max_palindrome_string)
        print("max str = ", max_palindrome_string)
        return max_palindrome_string


    def get_all_sub_string(self,k,value):
        if k == len(value):
            return value
        if k == 1:
            return list(value)

        for i in range(k,len(value)):
            a = value[:k-1]+value[i]






    def result_function(self, input_string):
        n = len(input_string)
        if n == 1:
            return 1
        max_palindrome_string = self.get_max_palindrome(input_string)
        palindrome_string_l = self.get_left_max_palindrome(input_string)
        palindrome_string_r = self.get_right_max_palindrome(input_string)
        if len(palindrome_string_l) > len(palindrome_string_r):
            max_palindrome_string = palindrome_string_l

        print("max str = ",max_palindrome_string)
        return len(max_palindrome_string)


if __name__ == '__main__':
    tmp_prime = kevindi()

    value = "1222345678909998765434421"
    print(tmp_prime.result_function(value))




