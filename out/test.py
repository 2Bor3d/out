import unittest
from out import out
from Color import Color
class MyTestCase(unittest.TestCase):
    def test_fat(self):
        self.assertEqual(out("Test", Color.FAT, output=False), out("Test", 1, output=False))
        self.assertEqual(out("Test", Color.FAT, output=False), out("Test", "fat", output=False))
        self.assertEqual(out("Test", "fat", output=False), out("Test", 1, output=False))
    def test_underlined(self):
        self.assertEqual(out("Test", Color.UNDERLINED, output=False), out("Test", 4, output=False))
        self.assertEqual(out("Test", Color.UNDERLINED, output=False), out("Test", "underlined", output=False))
        self.assertEqual(out("Test", "underlined", output=False), out("Test", 4, output=False))
    def test_background(self):
        self.assertEqual(out("Test", Color.BACKGROUND, output=False), out("Test", 7, output=False))
        self.assertEqual(out("Test", Color.BACKGROUND, output=False), out("Test", "background", output=False))
        self.assertEqual(out("Test", "background", output=False), out("Test", 7, output=False))
    def test_crossed(self):
        self.assertEqual(out("Test", Color.CROSSED, output=False), out("Test", 9, output=False))
        self.assertEqual(out("Test", Color.CROSSED, output=False), out("Test", "crossed", output=False))
        self.assertEqual(out("Test", "crossed", output=False), out("Test", 9, output=False))
    def test_grey(self):
        self.assertEqual(out("Test", Color.GREY, output=False), out("Test", 30, output=False))
        self.assertEqual(out("Test", Color.GREY, output=False), out("Test", "grey", output=False))
        self.assertEqual(out("Test", "grey", output=False), out("Test", 30, output=False))


if __name__ == '__main__':
    unittest.main()
