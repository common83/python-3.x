def list_range():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    for i in range(12+1):
        if i<5:
            continue
        else:
            print(i, "=", a[i-5:i])

    r = sum(a[1:3])
    print(r)

class Tdel:
    a = []

    def add_item(self):
        for i in range(5):
            self.a.append(i)

    def clear_item(self):
        if self.a:
            self.a.clear()
        # self.a = []

    def print_item(self):
        print(self.a)


def list_del():
    b = []
    a = Tdel()
    a.add_item()
    a.print_item()
    a.clear_item()
    a.print_item()


# list_del()
# list_del()
list_range()