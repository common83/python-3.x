# __*__encoding=utf-8 __*__
import unittest
import data_everyone.kevindi

class count_unit(unittest.TestCase):
    def public_same(self, who_object):

        value = [10, 3, 2, 5, 7, 8, 0, 1, 4, 6, 9]
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], who_object.result_function(value))

        value = [10]
        self.assertEqual([10], who_object.result_function(value))

        value = [0, 10]
        self.assertEqual([0, 10], who_object.result_function(value))

        value = [10, 3, 2, 5, 7, 8, 0, 1, 4, -6, 9]
        self.assertEqual([-6, 0, 1, 2, 3, 4, 5, 7, 8, 9, 10], who_object.result_function(value))

        value = [10, 3, 0, 5, 7, 0, 0, 1, 4, 0, 9]
        self.assertEqual([0, 0, 0, 0, 1, 3, 4, 5, 7, 9, 10], who_object.result_function(value))

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
