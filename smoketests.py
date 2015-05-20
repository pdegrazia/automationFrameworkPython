__author__ = 'paolo.degrazia'

import unittest
from automationFramework import AutomationFramework


class SmokeTests(unittest.TestCase):

    def setUp(self):
        pass

    def test_first_test(self):
        AutomationFramework().go()

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()