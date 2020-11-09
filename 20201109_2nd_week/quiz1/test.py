import unittest
import quiz1

test_case = [(25,1,11), (5750,0,4700), (11011,2,9481), (12224,8,7733), (11549,1,11905)]

class Test(unittest.TestCase):
    def test(self):
        for i in test_case:
            self.assertEqual(quiz1.solution(i[0], i[1]),i[2])
