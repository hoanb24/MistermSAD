import unittest
import app

class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(app.add(9,6),15);
        self.assertEqual(app.add(2,2),4);
        self.assertEqual(app.divide(25,5),5);

if __name__ == '__main__':
    unittest.main();