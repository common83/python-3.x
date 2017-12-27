# __*__encoding=utf-8 __*__

class kevindi(object):
    temp_list = []
    my_test = 0;
    def get_repeat_string(self,value):
        s = ""
        for i in range(len(value)):
            if value.count(value[i])>1:
                s += value[i]
        return s

    def get_max_palindrome(self,value):
        n = len(value)
        max = 0
        palindrome_string  = ""
        for i in range(n):
            for j in range(n,i,-1):
                if value[i:j] == (value[i:j])[::-1]:
                    if j-i > max:
                        max = j - i;
                        palindrome_string = value[i:j]
                        break
                    else:
                        break
        return palindrome_string


    def result_function(self, input_string):
        n = len(input_string)
        if n == 1:
            return 1
        repeat_string = self.get_repeat_string(input_string)
        palindrome_string = self.get_max_palindrome(repeat_string)
        print("repeat str=",repeat_string)
        print("palindrome str=",palindrome_string)
        palindrome_len = len(palindrome_string)
        print("palindrome len=", palindrome_len)
        if palindrome_len % 2 == 1:
            print("result palindrome str = ",palindrome_string)
            return palindrome_len
        else:
            j = 0
            for i in range(palindrome_len//2):
                while j < n :
                    if palindrome_string[i] == input_string[j]:
                        break
                    else:
                        j += 1
            if palindrome_string[palindrome_len//2+1] == input_string[j+1]:
                print("result palindrome str = ", palindrome_string)
                return len(palindrome_string)
            else:
                palindrome_string = palindrome_string[:palindrome_len//2] + input_string[j+1] + \
                                           palindrome_string[palindrome_len//2:]
                print("result palindrome str = ", palindrome_string)
                return len(palindrome_string);

        print("result palindrome str = ", palindrome_string)
        return len(palindrome_string);


if __name__ == '__main__':
    tmp_prime = kevindi()

    value = "1222345678909998765434421"
    print(tmp_prime.result_function(value))



