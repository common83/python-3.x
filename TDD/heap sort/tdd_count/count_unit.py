# __*__encoding=utf-8 __*__
import unittest
import data_everyone.kevindi

class count_unit(unittest.TestCase):
    def public_same(self, who_object):

        value = [10, 3, 2, 5, 7, 8, 0, 1, 4, 6, 9]
        self.assertEqual([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0], who_object.result_function(value))

        value = [10, 3]
        self.assertEqual([10, 3], who_object.result_function(value))

        value = [10]
        self.assertEqual([10], who_object.result_function(value))


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
