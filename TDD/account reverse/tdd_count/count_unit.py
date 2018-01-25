# __*__encoding=utf-8 __*__
import unittest
import data_everyone.kevindi

class count_unit(unittest.TestCase):
    def public_same(self, who_object):
        # kevindi
        self.assertEqual("noway", who_object.result_function(2500000,8000000))
        self.assertEqual(52, who_object.result_function(29, 119))
        self.assertEqual("noway", who_object.result_function(0, 1))
        self.assertEqual("noway", who_object.result_function(0, 1000000000000))
        self.assertEqual("noway", who_object.result_function(0, 0))
        self.assertEqual("noway", who_object.result_function(1000000000000, 1000000000000))
        self.assertEqual("noway", who_object.result_function(1000000000000, 0))
        self.assertEqual("noway", who_object.result_function(1, 1))
        self.assertEqual("noway", who_object.result_function(1, 2))
        self.assertEqual("noway", who_object.result_function(2, 1))
        self.assertEqual("noway", who_object.result_function(1, 3))
        self.assertEqual("noway", who_object.result_function(3, 1))
        self.assertEqual("noway", who_object.result_function(1, 4))
        self.assertEqual("noway", who_object.result_function(4, 1))
        self.assertEqual("noway", who_object.result_function(1, 5))
        self.assertEqual("noway", who_object.result_function(5, 1))
        self.assertEqual("noway", who_object.result_function(1, 6))
        self.assertEqual("noway", who_object.result_function(6, 1))
        self.assertEqual("noway", who_object.result_function(1, 7))
        self.assertEqual(2, who_object.result_function(4, 19))
        self.assertEqual(2, who_object.result_function(2, 9))

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
