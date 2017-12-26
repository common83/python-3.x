from turtle import *

def five_corner_start():
    fillcolor("red")
    begin_fill()
    while True:
        forward(200)
        right(144)
        if abs(pos()) < 1:
            break
    end_fill()


def cook():
    diet = ['西红柿', '花椰菜', '黄瓜', '牛排', '虾仁']
    for x in range(5):
        for y in range(0, 5):
            if not (x == y):
                print('{}{}'.format(diet[x], diet[y]))

if __name__ == "__main__":
    # cook()
    five_corner_start()
