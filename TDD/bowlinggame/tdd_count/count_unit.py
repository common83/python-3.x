# __*__encoding=utf-8 __*__
import unittest
import data_everyone.kevindi
import data_everyone.haliluyafu
import data_everyone.mulcyang

class count_unit(unittest.TestCase):
    def public_same(self, who_object):

        value = "X|X|X|X|X|X|X|X|X|X||XX"
        self.assertEqual(300, who_object.result_function(value))

        value = "9-|9-|9-|9-|9-|9-|9-|9-|9-|9-||"
        self.assertEqual(90, who_object.result_function(value))

        value = "5/|5/|5/|5/|5/|5/|5/|5/|5/|5/||5"
        self.assertEqual(150, who_object.result_function(value))

        value = "X|7/|9-|X|-8|8/|-6|X|X|X||81"
        self.assertEqual(167, who_object.result_function(value))

        value = "X|-/|22|22|22|22|22|22|22|22||"
        self.assertEqual(64, who_object.result_function(value))

        value = "X|--|22|22|22|22|22|22|22|22||"
        self.assertEqual(42, who_object.result_function(value))

        value = "X|1/|22|22|22|22|22|22|22|22||"
        self.assertEqual(64, who_object.result_function(value))

        value = "X|9/|22|22|22|22|22|22|22|22||"
        self.assertEqual(64, who_object.result_function(value))

        value = "X|X|-/|22|22|22|22|22|22|22||"
        self.assertEqual(80, who_object.result_function(value))

        value = "X|X|11|22|22|22|22|22|22|22||"
        self.assertEqual(63, who_object.result_function(value))

        value = "X|X|X|22|22|22|22|22|22|22||"
        self.assertEqual(94, who_object.result_function(value))

        value = "X|X|3/|22|22|22|22|22|22|22||"
        self.assertEqual(83, who_object.result_function(value))

        value = "X|X|--|22|22|22|22|22|22|22||"
        self.assertEqual(58, who_object.result_function(value))

        value = "-/|X|22|22|22|22|22|22|22|22||"
        self.assertEqual(66, who_object.result_function(value))

        value = "9/|X|22|22|22|22|22|22|22|22||"
        self.assertEqual(66, who_object.result_function(value))

        value = "11|X|22|22|22|22|22|22|22|22||"
        self.assertEqual(48, who_object.result_function(value))

        value = "--|X|22|22|22|22|22|22|22|22||"
        self.assertEqual(46, who_object.result_function(value))

        value = "-/|-/|22|22|22|22|22|22|22|22||"
        self.assertEqual(54, who_object.result_function(value))

        value = "22|22|22|22|22|22|22|22|22|22||"
        self.assertEqual(40, who_object.result_function(value))

        value = "22|22|22|22|22|22|22|22|22|2/||X"
        self.assertEqual(56, who_object.result_function(value))

        value = "22|22|22|22|22|22|22|22|22|2/||-"
        self.assertEqual(46, who_object.result_function(value))

        value = "22|22|22|22|22|22|22|22|22|2/||2"
        self.assertEqual(48, who_object.result_function(value))

        value = "22|22|22|22|22|22|22|22|22|X||22"
        self.assertEqual(50, who_object.result_function(value))

        value = "22|22|22|22|22|22|22|22|22|X||--"
        self.assertEqual(46, who_object.result_function(value))

        value = "22|22|22|22|22|22|22|22|22|X||-2"
        self.assertEqual(48, who_object.result_function(value))

        value = "22|22|22|22|22|22|22|22|22|X||2-"
        self.assertEqual(48, who_object.result_function(value))

        value = "22|22|22|22|22|22|22|22|22|X||X-"
        self.assertEqual(56, who_object.result_function(value))

        value = "22|22|22|22|22|22|22|22|22|X||-X"
        self.assertEqual(56, who_object.result_function(value))

        value = "22|22|22|22|22|22|22|22|22|X||XX"
        self.assertEqual(66, who_object.result_function(value))

        value = "22|22|22|22|22|22|22|22|22|X||2/"
        self.assertEqual(56, who_object.result_function(value))

        value = "22|22|22|22|22|22|22|22|22|X||2X"
        self.assertEqual(58, who_object.result_function(value))

        value = "22|22|22|22|22|22|22|22|22|X||-/"
        self.assertEqual(56, who_object.result_function(value))

        value = "--|--|--|--|--|--|--|--|--|--||"
        self.assertEqual(0, who_object.result_function(value))


    def test_kevindi(self):
        who_kevindi = data_everyone.kevindi.kevindi()
        self.public_same(who_kevindi)

    def test_haliluyafu(self):
        who_haliluyafu = data_everyone.haliluyafu.haliluyafu()
        self.public_same(who_haliluyafu)

    def test_mulcyang(self):
        who_mulcyang = data_everyone.mulcyang.mulcyang()
        self.public_same(who_mulcyang)



if __name__ == '__main__':
    # step1:
    suite = unittest.TestSuite()
    suite.addTest(count_unit("test_kevindi"))

    # step1:
    suite = unittest.TestSuite()
    suite.addTest(count_unit("test_haliluyafu"))

    # step1:
    suite = unittest.TestSuite()
    suite.addTest(count_unit("test_mulcyang"))

    # step3:
    runner = unittest.TextTestRunner()
    runner.run(suite)
