# __*__encoding=utf-8 __*__
import unittest
import data_everyone.kevindi

class count_unit(unittest.TestCase):
    def public_same(self, who_object):

        value = 1
        self.assertEqual([1], who_object.result_function(value))

        value = 2
        self.assertEqual([2], who_object.result_function(value))

        value = 3
        self.assertEqual([3], who_object.result_function(value))

        value = 4
        self.assertEqual([2,2], who_object.result_function(value))

        self.assertEqual([11,11], who_object.result_function(121))
        self.assertEqual([2,2,5,5], who_object.result_function(100))
        self.assertEqual([3, 3, 3, 7, 11, 13, 37], who_object.result_function(999999))
        self.assertEqual([13, 13, 97, 131], who_object.result_function(2147483))

    def test_kevindi(self):
        who_kevindi = data_everyone.kevindi.kevindi()
        self.public_same(who_kevindi)


if __name__ == '__main__':
    # step1:
    suite = unittest.TestSuite()
    suite.addTest(count_unit("test_kevindi"))

    # step3:
    runner = unittest.TextTestRunner()
    runner.run(suite)
