import unittest
from code1 import speed_eval,score_eval
class SpeedTest(unittest.TestCase):
    def test_Invalid(self):
            self.assertEqual(speed_eval(-5),"Invalid")
            self.assertEqual(speed_eval(221),"Invalid")
            self.assertEqual(speed_eval(240),"Invalid")
    def test_Low(self):
            self.assertEqual(speed_eval(0),"Low")
            self.assertEqual(speed_eval(20),"Low")
    def test_Normal(self):
            self.assertEqual(speed_eval(40),"Normal")
            self.assertEqual(speed_eval(119),"Normal")
    def test_High(self):
            self.assertEqual(speed_eval(120),"High")
            self.assertEqual(speed_eval(159),"High")
    def test_VeryHigh(self):
            self.assertEqual(speed_eval(200),"V.High")
            self.assertEqual(speed_eval(210),"V.High")
            self.assertEqual(speed_eval(220),"V.High")

class ScoreTest(unittest.TestCase):
    def test_Invalid(self):
            self.assertEqual(score_eval(-5),"Invalid")
            self.assertEqual(score_eval(101),"Invalid")
    def test_Failed(self):
            self.assertEqual(score_eval(0),"Failed")
            self.assertEqual(score_eval(49),"Failed")
    def test_Passed(self):
            self.assertEqual(score_eval(50),"Passed")
            self.assertEqual(score_eval(64),"Passed")
    def test_Good(self):
            self.assertEqual(score_eval(65),"Good")
            self.assertEqual(score_eval(70),"Good")
    def test_Vgood(self):
            self.assertEqual(score_eval(75),"V.Good")
            self.assertEqual(score_eval(80),"V.Good")
    def test_Excellent(self):
            self.assertEqual(score_eval(89),"Excellent")
            self.assertEqual(score_eval(85),"Excellent")
            self.assertEqual(score_eval(100),"Excellent")
    
if __name__ == "__main__":
       unittest_.main()