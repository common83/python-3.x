# __*__encoding=utf-8 __*__
import unittest
import data_everyone.kevindi

class count_unit(unittest.TestCase):
    def public_same(self, who_object):

        value = "MT-TECH-TEAM"
        self.assertEqual(33, who_object.result_function(value))

        value = "MT-TEcH-TEAM"
        self.assertEqual(33, who_object.result_function(value))

        value = "MT-TEdH-TEAM"
        self.assertEqual(33, who_object.result_function(value))

        value = ""
        self.assertEqual(0, who_object.result_function(value))

        value = "a"
        self.assertEqual(1, who_object.result_function(value))

        value = "aaa"
        self.assertEqual(3, who_object.result_function(value))

        value = "aa"
        self.assertEqual(2, who_object.result_function(value))

        value = "ab"
        self.assertEqual(2, who_object.result_function(value))

        value = "abb"
        self.assertEqual(3, who_object.result_function(value))

        value = "abba"
        self.assertEqual(4, who_object.result_function(value))

        value = "abc"
        self.assertEqual(5, who_object.result_function(value))

        value = "a3"
        self.assertEqual(2, who_object.result_function(value))

        value = "23"
        self.assertEqual(2, who_object.result_function(value))

        value = "-_"
        self.assertEqual(2, who_object.result_function(value))

        value = "01"
        self.assertEqual(2, who_object.result_function(value))

        value = "000"
        self.assertEqual(3, who_object.result_function(value))

        value = "0"
        self.assertEqual(1, who_object.result_function(value))

        self.assertEqual(0, who_object.result_function(""))
        self.assertEqual(33, who_object.result_function("MT-TECH-TEAM"))
        self.assertEqual(5, who_object.result_function("_---_"))
        self.assertEqual(8, who_object.result_function("32123"))
        self.assertEqual(53, who_object.result_function("321___---abcabcabc"))
        self.assertEqual(124, who_object.result_function("abcdefghijklmnopqrstuvwxyz"))

        # vacon
        self.assertEqual(33, who_object.result_function("MT-TECH-TEAM"))
        self.assertEqual(0, who_object.result_function(""))
        self.assertEqual(1, who_object.result_function("a"))
        self.assertEqual(2, who_object.result_function("ab"))
        self.assertEqual(4, who_object.result_function("aabb"))
        self.assertEqual(5, who_object.result_function("aabbb"))
        self.assertEqual(9, who_object.result_function("aabbbc"))
        self.assertEqual(60, who_object.result_function("abbccccddddddddeeeeeeeeeeeeeeeeeeee"))

        # haliluyafu
        self.assertEqual(33, who_object.result_function('MT-TECH-TEAM'))
        self.assertEqual(53, who_object.result_function('aaabbbbcdddddffggggggg'))
        self.assertEqual(20, who_object.result_function('abcdefg'))
        self.assertEqual(22, who_object.result_function('abbbbbcccccccccc'))  #
        self.assertEqual(7, who_object.result_function('aaaaaab'))  #
        self.assertEqual(15, who_object.result_function('aaaaaaaaaaaaaaa'))  #


        # timyan
        self.assertEqual(33, who_object.result_function("MT-TECH-TEAM"))
        self.assertEqual(42, who_object.result_function("AAABBBBBCCCCCDDDDDDDD"))
        self.assertEqual(20, who_object.result_function("abcdefg"))
        self.assertEqual(1, who_object.result_function("a"))
        self.assertEqual(0, who_object.result_function(""))

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
