import random



class Test:

    def __init__(self):
        self.x = 0
        self.temp_list = []
        self.nochange = "WAM"


    def bxx(self):
        if len(self.temp_list) == 0:
            for element in range(3):
                self.x = random.randint(0, 10)
                self.temp_list.append((self.nochange, self.x))
                print(self.temp_list)

test = Test()
test.bxx()