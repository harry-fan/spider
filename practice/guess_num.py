#coding:utf-8

# 这是一个猜数字游戏
import random
import sys

class GuessNum(object):
    def __init__(self):
        print("欢迎来到猜数字游戏：你可以在1到20之间选一个数字，通过我给的提示，在6次猜中，你就赢了")
        self.times = 0
        self.answer = random.randint(1,20)
        self.sucess = 2

    def guess(self, num):
        if not self.check_times():
            print("你失败了")
            return False
        if num == self.answer:
            print("good 你赢了")
            return self.sucess
        elif num < self.answer:
            print("你输入的数值小了")
            self.times += 1
            return True
        elif num > self.answer:
            print("你输入的数值大了")
            self.times += 1
            return True

    def check_times(self):
        if self.times < 6:
            return True
        else:
            return False

def deal_str(_str):
    sstr = _str.lower()
    if sstr == 'n':
        return False
    elif sstr == 'y':
        return True
    else:
        print("error")
        return False
def play_again():
    if sys.version_info.major > 2:
        y_n = input("游戏结束了， 还想玩吗:Y/N")
    else:
        y_n = raw_input("游戏结束了， 还想玩吗:Y/N")
    again = deal_str(y_n)
    if again:
        start()
    else:
        return False

def start():
    game = GuessNum()
    num = int(input("输入你给的数吧:"))
    result = game.guess(num)
    while True:
        if result == game.sucess:
            play = play_again() 
            if not play:
                break
        elif result:
            num = int(input("请再尝试："))
            result = game.guess(num)
        else:
            play = play_again()
            if not play:
                break
            
if __name__ == '__main__':
    start()
