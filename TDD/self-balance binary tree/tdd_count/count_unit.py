# __*__encoding=utf-8 __*__
import unittest
import data_everyone.kevindi

class count_unit(unittest.TestCase):
    def public_same(self, who_object):

        value = [3, 9, 20, 'null', 'null', 15, 7]
        self.assertEqual(True, who_object.result_function(value))

        value = [1,2,2,3,3,'null','null',4,4]
        self.assertEqual(False, who_object.result_function(value))

        value = [1]
        self.assertEqual(True, who_object.result_function(value))

        value = [1,"null",2]
        self.assertEqual(True, who_object.result_function(value))

        value = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
        self.assertEqual(True, who_object.result_function(value))

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
