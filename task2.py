#!/usr/bin/env python

# https://acmp.ru/index.asp?main=task&id_task=27


class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.X = {1: x1, 2: x2}
        self.Y = {1: y1, 2: y2}

    def __eq__(self, other):
        return self.X[1] == other.X[1] and self.X[2] == other.X[2] and \
               self.Y[1] == other.Y[1] and self.Y[2] == other.Y[2]

def parseParameters(str1, str2):
    w, h = str1.split()
    return int(w), int(h), int(str2)


def parseRectangles(source):
    # if source is "int" - parsing n lines from input(),
    # if source is "string" - parsing the string
    rect = []
    if type(source) == int:
        for i in range(source):
            x1, y1, x2, y2 = input().split()
            rect.append(Rectangle(int(x1), int(y1), int(x2), int(y2)))

    else:
        for i in source.split(';'):
            temp = i.split()
            rect.append(Rectangle(int(temp[0]), int(temp[1]), int(temp[2]), int(temp[3])))
    return rect


def createCanvas(w, h):
    return [[0 for y in range(h)] for x in range(w)]


def painting(rectangles, canvas):
    for i in range(len(rectangles)):
        for iterX in range(min(rectangles[i].X[1], rectangles[i].X[2]),
                           max(rectangles[i].X[1], rectangles[i].X[2])):
            for iterY in range(min(rectangles[i].Y[1], rectangles[i].Y[2]),
                           max(rectangles[i].Y[1], rectangles[i].Y[2])):
                canvas[iterX][iterY] += 1
    return canvas


def calculateWhiteArea(canvas):
    square = 0
    for i in canvas:
        for j in i:
            if j == 0:
                square += 1
    return square


if __name__ == "__main__":
    w, h, n = parseParameters(input(), input())
    print(calculateWhiteArea(painting(parseRectangles("1 1 3 3; 2 2 4 4"), createCanvas(w, h))))
