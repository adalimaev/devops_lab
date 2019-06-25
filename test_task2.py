from unittest import TestCase
import task2


class TestTask2(TestCase):

    def test_rectangle_constructor(self):
        rect = task2.Rectangle(10, 20, 30, 40)
        self.assertEqual(rect.X, {1: 10, 2: 30})
        self.assertEqual(rect.Y, {1: 20, 2: 40})

    def test_rectangle_eq_operator(self):
        rect1 = task2.Rectangle(10, 20, 30, 40)
        rect2 = task2.Rectangle(10, 20, 30, 40)
        self.assertTrue(rect1 == rect2)

    def test_parseParameters(self):
        param1 = "5 5"
        param2 = "2"
        self.assertEqual(task2.parseParameters(param1, param2), (5, 5, 2))

    def test_parseRectangles(self):
        rectangles = [task2.Rectangle(0, 0, 5, 5),
                      task2.Rectangle(1, 1, 4, 4),
                      task2.Rectangle(2, 2, 3, 3)]
        str = "0 0 5 5; 1 1 4 4; 2 2 3 3"
        self.assertEqual(rectangles, task2.parseRectangles(str))

    def test_createCanvas(self):
        canvas = task2.createCanvas(100, 1000)
        self.assertEqual(len(canvas), 100)
        self.assertEqual(len(canvas[99]), 1000)
        self.assertEqual(canvas[99][87], 0)

    def test_painting(self):
        rectangles = [task2.Rectangle(1, 1, 3, 3), task2.Rectangle(2, 2, 4, 4)]
        empty_canvas = [[0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0]]
        reslt_canvas = [[0, 0, 0, 0, 0],
                        [0, 1, 1, 0, 0],
                        [0, 1, 2, 1, 0],
                        [0, 0, 1, 1, 0],
                        [0, 0, 0, 0, 0]]
        canvas1 = task2.painting(rectangles, empty_canvas)
        self.assertEqual(canvas1, reslt_canvas)

    def test_calculateWhiteArea(self):
        empt_cnv = [[0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0]]
        canvas2 = [[0, 0, 0, 0, 0],
                   [0, 1, 1, 0, 0],
                   [0, 1, 2, 1, 0],
                   [0, 0, 1, 1, 0],
                   [0, 0, 0, 0, 0]]
        full_cn = [[2, 8, 5, 3, 1],
                   [1, 6, 1, 4, 1],
                   [7, 1, 1, 1, 1],
                   [1, 3, 1, 8, 1],
                   [2, 1, 9, 1, 1]]
        self.assertEqual(task2.calculateWhiteArea(empt_cnv), 25)
        self.assertEqual(task2.calculateWhiteArea(canvas2), 18)
        self.assertEqual(task2.calculateWhiteArea(full_cn), 0)
