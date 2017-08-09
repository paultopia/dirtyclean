from dirtyclean import clean
import unittest

class TestDirtyClean(unittest.TestCase):

    def setUp(self):
        self.uglystring = "   st—up•id ‘char−ac   ter..s’, in its’ string...”Ç "
        with open("multiline.txt") as mt:
            self.multiline = mt.read()

    def test_basic_clean(self):
        self.assertEqual(clean(self.uglystring),
                         "st up id char ac ter s in its string Ç")

    def test_simplify_letters(self):
        self.assertEqual(clean(self.uglystring, simplify_letters=True),
                         "st up id char ac ter s in its string C")

    def test_multiline(self):
        self.assertEqual(clean(self.multiline),
                         "I am the very model of a multiline string with more stuff than you might want to have in there Ç")


