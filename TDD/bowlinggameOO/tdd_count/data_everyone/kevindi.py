# __*__encoding=utf-8 __*__

class BowlingGame:
    score = 0
    frame_list = []

    def game_start(self):
        if self.frame_list:
            self.frame_list.clear()
        self.score = 0

    def roll(self, index, value):
        frame = Frame(index, value)
        self.score += frame.get_frame_score()
        self.frame_list.append(frame)
        frame.clear()

    def game_over(self):
        if self.frame_list:
            self.frame_list.clear()
        self.score = 0

    def get_score(self):
        return self.score

class Frame:
    FRAME_TYPE = {"SPARE":1, "STRIKE":2, "DIGIT":3, "BONUS":4 }
    SPARE_FRAME_VALUE = 10
    STRIKE_FRAME_VALUE = 10
    frame_index = 0
    frame_value = ""
    frame_type = -1
    frame_score = 0

    def __init__(self, index, value):
        if value:
            self.frame_value = value.replace("-", "0")
            self.frame_index = index
        self.get_frame_type()

    def get_frame_type(self):
        if not self.frame_value:
            self.frame_type = "BONUS"
            self.frame_score = 0
            return self.frame_type
        if self.frame_value.find("/") > 0:
            self.frame_type = "SPARE"
            self.frame_score = self.SPARE_FRAME_VALUE
        else:
            self.frame_type = "DIGIT"
            self.frame_score = int(self.frame_value[0]) + int(self.frame_value[1])

        return self.frame_type

    def get_frame_score(self):
        return self.frame_score

    def clear(self):
        self.frame_index = 0
        self.frame_value = ""
        self.frame_type = -1
        self.frame_score = 0



class kevindi(object):
    SIG_FRAME = "|"
    SIG_SPARE = "/"
    bowlinggame = BowlingGame()


    def result_function(self, value):
        self.bowlinggame.game_start()
        frame_list = value.split("|")
        del frame_list[10]

        for i in range(len(frame_list)):
            print(i,frame_list[i])
            self.bowlinggame.roll(i, frame_list[i])
        score = self.bowlinggame.get_score()
        return score;


if __name__ == '__main__':
    tmp_prime = kevindi()

    value = "1/|--|--|--|--|--|--|--|--|--||"
    print(tmp_prime.result_function(value))


