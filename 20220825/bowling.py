class player_frame:
    def __init__(self, *args, **kwargs):
        self.score = [[0, ""]] * 10
        self.frames = [0] * 10

    def sum_digits_string(self, some_string):
        sum_digit = 0
        for x in some_string:
            if x.isdigit() == True:
                z = int(x)
                sum_digit = sum_digit + z

        return sum_digit

    def evaluate_game(self, rolls) -> int:
        rolls_temp = rolls.split(" ")
        if len(rolls_temp) == 10:
            self.frames = rolls_temp
        else:
            return "Error"  # add error correction

        for idx, i in enumerate(self.frames):
            if "X" in i:
                self.score[idx] = [10, "strike"]
            elif "/" in i:
                self.score[idx] = [10, "spare"]
            elif "--" in i:
                self.score[idx] = [0, "gutter"]
            else:
                self.score[idx] = [self.sum_digits_string(i), ""]

        for jdx, j in enumerate(self.score):
            if jdx == 8:
                self.last_frame(j, self.frames[jdx])
            elif j[1] == "strike":
                num = self.score[jdx][0] + self.score[jdx + 1][0] + self.score[jdx + 2][0]
                self.score[jdx][0] = num
            elif j[1] == "spare":
                num = self.score[jdx][0] + self.score[jdx + 1][0]
                self.score[jdx][0] = num

            # self.score[jdx]=self.score[jdx]+self.score[jdx+1]

        return None

    def last_frame(self, score, raw_frame) -> int:
        pass


if __name__ == "__main__":
    player1 = player_frame()
    
    player1.evaluate_game("X X X X X X X X X XXX")
    player1.evaluate_game("X 5- 7/ 5- X 5- X 5- X XXX")
