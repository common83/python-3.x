# __*__encoding=utf-8 __*__
import unittest
import data_everyone.kevindi

class count_unit(unittest.TestCase):
    def public_same(self, who_object):

        value = "12346302"
        self.assertEqual(5, who_object.result_function(value))

        self.assertEqual(20, who_object.result_function("1222345678909998765434421"))
        self.assertEqual(7, who_object.result_function("1223505252"))
        self.assertEqual(6, who_object.result_function("112211"))
        self.assertEqual(6, who_object.result_function("122355252"))
        self.assertEqual(1, who_object.result_function("12345"))
        self.assertEqual(2, who_object.result_function("11"))
        self.assertEqual(9, who_object.result_function("111111222222222"))

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
