# __*__encoding=utf-8 __*__

class kevindi(object):
    STRIKE_FRAME = 1
    SPARE_FRAME = 2
    BONUS_FRAME = 3
    KNOCK_FRAME = 4
    SIG_STRIKE = "X"
    SIG_SPARE = "/"
    SIG_MISS = "-"
    SIG_FRAME = "|"
    SIG_BONUS = "||"

    game_frames = []

    # return frame type:strike_frame, spare_frame, bonus_frame, knock_frame
    def get_frame_type(self, index):
        #print("get_frame_type", "index:", index, "frame:", self.game_frames[index])
        if index == 10:
            return self.BONUS_FRAME
        if self.game_frames[index].find(self.SIG_STRIKE) != -1:
            return self.STRIKE_FRAME
        if self.game_frames[index].find(self.SIG_SPARE) != -1:
            return self.SPARE_FRAME
        return self.KNOCK_FRAME

    def get_one_boll_score(self,index):
        frame_type = self.get_frame_type(index)
        if frame_type == self.KNOCK_FRAME:
            score = int(self.game_frames[index][0])
            return score
        if frame_type == self.STRIKE_FRAME:
            return 10
        if frame_type == self.SPARE_FRAME:
            score = int(self.game_frames[index][0])
            return score
        if frame_type == self.BONUS_FRAME:
            if self.game_frames[index][0] == "X":
                return 10
            score = int(self.game_frames[index][0])
            return score

    def get_two_boll_score(self, index):
        frame_type = self.get_frame_type(index)
        if frame_type == self.KNOCK_FRAME:
            score = int(self.game_frames[index][0]) + int(self.game_frames[index][1])
            return score
        if frame_type == self.STRIKE_FRAME:
            score = 10 + self.get_one_boll_score(index+1)
            return score
        if frame_type == self.SPARE_FRAME:
            return 10
        if frame_type == self.BONUS_FRAME:
            if self.game_frames[index][1] == "/":
                return 10
            a = 0
            b = 0
            if self.game_frames[index][0] == "X":
                a = 10
            else:
                a = int(self.game_frames[index][0])
            if self.game_frames[index][1] == "X":
                b = 10
            else:
                b = int(self.game_frames[index][1])
            score = a + b
            return score


    def result_function(self, game_score):
        if not game_score:
            return 0
        # print("input value",game_score)
        game_score = game_score.replace("-", "0")
        # print("replaced -",game_score)
        # bonus_frame = game_score[game_score.rfind(self.SIG_FRAME):]
        self.game_frames = game_score.split("|")
        print("test",len(self.game_frames),self.game_frames)
        del self.game_frames[10]
        print("test",len(self.game_frames),self.game_frames)
        if not self.game_frames[10]:  # review bonus score
            self.game_frames[10] = "00"
        print("test", len(self.game_frames), self.game_frames)
        score = 0
        for i in range(10): # not have bonus frame
            # print("result_function,frame=",i,"score=",score)
            frame_type = self.get_frame_type(i)
            if frame_type == self.KNOCK_FRAME:
                frame_score = int(self.game_frames[i][0]) + int(self.game_frames[i][1])
                score += frame_score
            if frame_type == self.STRIKE_FRAME:
                frame_score = 10 + self.get_two_boll_score(i+1)
                score += frame_score
            if frame_type == self.SPARE_FRAME:
                frame_score = 10 + self.get_one_boll_score(i+1)
                score += frame_score
            if frame_type == self.BONUS_FRAME:
                print("error")

        return score;


if __name__ == '__main__':
    tmp_prime = kevindi()

    value = "22|22|22|22|22|22|22|22|22|X||"
    print(tmp_prime.result_function(value))


