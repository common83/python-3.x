# __*__encoding=utf-8 __*__
import unittest
import data_everyone.kevindi

class count_unit(unittest.TestCase):
    def public_same(self, who_object):
        value = [2, 7, 11, 15]
        target = 9
        self.assertEqual([0,1], who_object.result_function(value, target))

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
