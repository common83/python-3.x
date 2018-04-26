__author__ = 'vaconzhang'
import unittest
import data_everyone.grootyan
import data_everyone.haliluyafu
import data_everyone.kevindi
import data_everyone.mulcyang
import data_everyone.shamchen
import data_everyone.timyan
import data_everyone.vaconzhang


class count_unit(unittest.TestCase):
    def public_same(self, who_object):
        # shamchen
        self.assertEqual(9, who_object.result_function([10,5,1,2,3,6,7,9,11,22,44,50]))
        self.assertEqual(0, who_object.result_function([1,1,20]))
        self.assertEqual(20, who_object.result_function([2,1,1,21]))

        # haliluyafu
        self.assertEqual(2, who_object.result_function([4, 2, 1, 2, 3, 55]))
        self.assertEqual(4, who_object.result_function([5, 2, 1, 2, 3, 4, 55]))
        self.assertEqual(3, who_object.result_function([5, 2, 1, 2, 3, 4, 5]))
        self.assertEqual(9, who_object.result_function([10, 5, 1, 2, 3, 6, 7, 9, 11, 22, 44, 50]))
        
        #mulcyang
        self.assertEqual(0, who_object.result_function([5,5,1,2,3,4,5]))
        self.assertEqual(1, who_object.result_function([5,4,1,2,3,4,5]))
        self.assertEqual(2, who_object.result_function([5,3,1,2,3,4,5]))
        self.assertEqual(3, who_object.result_function([5,2,1,2,3,4,5]))
        self.assertEqual(6, who_object.result_function([5,1,1,2,3,4,5]))
        self.assertEqual(9, who_object.result_function([10,5,1,2,3,6,7,9,11,22,44,50]))
        self.assertEqual(4, who_object.result_function([3,2,1,5,10]))

        #timyan
        # self.assertEqual(2684354559, who_object.result_function([5,2,1,536870912,1073741824,2147483648,4294967296]))

        #kevindi
        param_value = [10, 5, 1, 2, 3, 6, 7, 9, 11, 22, 44, 50]
        self.assertEqual(9, who_object.result_function(param_value))


    def test_grootyan(self):
        who_grootyan = data_everyone.grootyan.grootyan()
        self.public_same(who_grootyan)
    def test_haliluyafu(self):
        who_haliluyafu = data_everyone.haliluyafu.haliluyafu()
        self.public_same(who_haliluyafu)
    def test_kevindi(self):
        who_kevindi = data_everyone.kevindi.kevindi()
        self.public_same(who_kevindi)
    def test_mulcyang(self):
        who_mulcyang = data_everyone.mulcyang.mulcyang()
        self.public_same(who_mulcyang)
    def test_shamchen(self):
        who_shamchen = data_everyone.shamchen.shamchen()
        self.public_same(who_shamchen)
    def test_timyan(self):
        who_timyan = data_everyone.timyan.timyan()
        self.public_same(who_timyan)
    def test_vaconzhang(self):
        who_vaconzhang = data_everyone.vaconzhang.vaconzhang()
        self.public_same(who_vaconzhang)


if __name__ == '__main__':

    suite = unittest.TestSuite()

    suite.addTest(count_unit("test_grootyan"))
    suite.addTest(count_unit("test_haliluyafu"))
    suite.addTest(count_unit("test_kevindi"))
    suite.addTest(count_unit("test_mulcyang"))
    suite.addTest(count_unit("test_shamchen"))
    suite.addTest(count_unit("test_timyan"))
    suite.addTest(count_unit("test_vaconzhang"))


    runner = unittest.TextTestRunner()
    runner.run(suite)
