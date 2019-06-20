#!/usr/bin/env python

w, h = input("Please enter Width and Height: ").split()
w = int(w)
h = int(h)
n = int(input("Please enter the number of rectangles: "))

rectangles = []

for i in range(n):
    x1, y1, x2, y2 = input().split()
    rectangles.append([int(x1), int(y1), int(x2), int(y2)])

squareAllRectangles: int = 0
for i in rectangles:
    squareAllRectangles += abs((i[2] - i[0]) * (i[3] - i[1]))

paintedSquare: int = 0
for i in range(len(rectangles) - 1):
    # looking for intersection on X
    minX = min(rectangles[i][0], rectangles[i][2], rectangles[i + 1][0], rectangles[i + 1][2])
    maxX = max(rectangles[i][0], rectangles[i][2], rectangles[i + 1][0], rectangles[i + 1][2])
    intersectionX = (rectangles[i][2] - rectangles[i][0]) + \
                    (rectangles[i + 1][2] - rectangles[i + 1][0]) - \
                    (maxX - minX)
    intersectionX = 0 if intersectionX < 0 else intersectionX

    # looking for intersection on Y
    minY = min(rectangles[i][1], rectangles[i][3], rectangles[i + 1][1], rectangles[i + 1][3])
    maxY = max(rectangles[i][1], rectangles[i][3], rectangles[i + 1][1], rectangles[i + 1][3])
    intersectionY = (rectangles[i][3] - rectangles[i][1]) + \
                    (rectangles[i + 1][3] - rectangles[i + 1][1]) - \
                    (maxY - minY)
    intersectionY = 0 if intersectionY < 0 else intersectionY

    paintedSquare += intersectionX * intersectionY

S = w * h - squareAllRectangles + paintedSquare
print(S)
