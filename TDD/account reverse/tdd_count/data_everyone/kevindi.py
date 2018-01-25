# __*__encoding=utf-8 __*__

class kevindi(object):
    month_profit = []
    y = 0
    k = 0
    my_test = 0;

    def month_report(self,month):
        if month < 5:
            return -1
        else:
            return sum(self.month_profit[month-5:month])

    def is_according_to_month_report(self, month):
        if self.month_report(month) >= 0:
                return False
        return True

    def according_to_month_report(self, month):
        i = 1
        while not self.is_according_to_month_report(month):
            if i > 5 or month < i:
                break
            else:
                self.month_profit[month - i] = self.k
                i += 1

    def result_function(self, y, k):  # +y, -k
        self.y = y
        self.k = -k
        self.month_profit = []
        for i in range(12):
            self.month_profit.append(y)
        #print("month profit:", self.month_profit)
        for i in range(1, 13):
            self.according_to_month_report(i)

        print("month profit:",self.month_profit)
        print("month report:",end="")
        for i in range(1,13):
            print(self.month_report(i),end=",")
        print("")
        year_profit = sum(self.month_profit[:])
        print("year profit:",year_profit)
        if year_profit > 0:
            return year_profit
        else:
            return "noway"


if __name__ == '__main__':
    tmp_prime = kevindi()

    print(tmp_prime.result_function(29,119))


