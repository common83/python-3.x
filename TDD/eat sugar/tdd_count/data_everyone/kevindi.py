# __*__encoding=utf-8 __*__

class kevindi(object):
    # 比赛结果展示
    color_sugar_list = []
    my_test = 0

    # 用最优策略吃糖
    def eat_sugar(self):
        if len(self.color_sugar_list) == 1:
            if self.color_sugar_list[0] == 1:
                # 只有最后一颗
                self.color_sugar_list.remove(1)
                return True
            else:
                # 吃到剩下一颗,换人
                self.color_sugar_list[0] = 1
                return False
        elif len(self.color_sugar_list) == 2:
            if self.color_sugar_list[0] == 1:
                self.color_sugar_list.pop()
            elif self.color_sugar_list[1] == 1:
                self.color_sugar_list.pop(0)
            else:
                self.color_sugar_list[0] -= 1
        return False


    def result_function(self, p_color_num, p_color_sugar_list):
        self.color_sugar_list.clear()
        self.color_sugar_list = p_color_sugar_list[:]
        character = "wang"
        while True:
            if self.eat_sugar():
                # 吃到最后一颗糖，终止游戏
                break
            # 换人
            if character == "wang":
                character = "-wang"
            else:
                character == "wang"
        return character;


if __name__ == '__main__':
    tmp_prime = kevindi()
    color_num = 3
    color_sugar_list = [3, 5, 1]
    print(tmp_prime.result_function(color_num, color_sugar_list))


