# __*__encoding=utf-8 __*__

class BowlingGame:
    score = 0

    def game_start(self):
        self.score = 0

    def roll(self,score):
        self.score += score

    def game_over(self):
        self.score = 0

    def get_score(self):
        return self.score

class kevindi(object):
    SIG_FRAME = "|"
    SIG_MISS = "-"
    bowlinggame = BowlingGame()

    def isMISSROLL(self,value):
        if value == self.SIG_MISS:
            return True
        else:
            return False

    def result_function(self, value):
        self.bowlinggame.game_start()
        for i in range(len(value)):
            if value[i] != self.SIG_FRAME:
                if self.isMISSROLL(value[i]):
                    self.bowlinggame.roll(0)
                else:
                    self.bowlinggame.roll(int(value[i]))
            else:
                continue

        score = self.bowlinggame.get_score()
        return score;


if __name__ == '__main__':
    tmp_prime = kevindi()

    value = "11|--|--|--|--|--|--|--|--|--||"
    print(tmp_prime.result_function(value))


