# __*__encoding=utf-8 __*__
import unittest
import data_everyone.kevindi

class count_unit(unittest.TestCase):
    def public_same(self, who_object):

        value = [34, 21, 32, 41, 25, 14, 42, 43, 14, 31, 54, 45, 5 , 42, 23, 33, 15, 51, 31, 35, 21, 52, 33, 13, 23]
        self.assertEqual("No saddle points", who_object.result_function(value))

        value = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        self.assertEqual([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24], who_object.result_function(value))

        value = [1,0,-3,2,3,
                 1,1,1,1,5,
                 1,1,1,1,6,
                 1,1,1,1,7,
                 1,1,1,1,8]
        self.assertEqual([4], who_object.result_function(value))

        value = [1,0,-3,2,3,
                 1,1,1,1,5,
                 1,1,1,1,6,
                 1,1,1,1,7,
                 1,1,1,1,8]
        self.assertEqual([4], who_object.result_function(value))

        self.assertEqual([4,9,14,19,24], who_object.result_function([1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]))
        self.assertEqual("No saddle points", who_object.result_function([7,7,8,9,8,9,9,9,9,9,10,11,12,1,1,13,14,15,16,17,0,1,2,3,4]))
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24], who_object.result_function([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))

        self.assertEqual([4, 9, 14, 19, 24],
           who_object.result_function([1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))
        self.assertEqual("No saddle points",
           who_object.result_function([1, 2, 3, 4, 5, 2, 3, 4, 5, 1, 3, 4, 5, 1, 2, 4, 5, 1, 2, 3, 5, 1, 2, 3, 4]))  #
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
           who_object.result_function([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
        self.assertEqual([4, 9, 14, 19, 24],
           who_object.result_function([1.1, 2.2, 3.3, 4.4, 5.5, 1.1, 2.2, 3.3, 4.4, 5.5, 1.1, 2.2, 3.3, 4.4, 5.5, 1.1, 2.2, 3.3, 4.4, 5.5, 1.1, 2.2, 3.3, 4.4, 5.5]))


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
