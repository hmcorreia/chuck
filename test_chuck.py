import unittest

class MyTestCase(unittest.TestCase):
    def test_chuck_appearence(self):
        self.assertEqual('Chuck Norris', 'Chuck Norris')

if __name__ == '__main__':
    unittest.main()
