import unittest
from generate import getCountryCode
class TestCountry(unittest.TestCase):
    def testIfCountryIsSweden(self):
        # ARRANGE
        currentCountry = "sv_SE"
        # ACT
        c = getCountryCode(currentCountry)
        # ASSERT
        self.assertEqual(c, "SE")
if __name__ == '__main__':
    unittest.main() 
