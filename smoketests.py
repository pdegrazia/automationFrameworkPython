__author__ = 'paolo.degrazia'

import unittest
from automationFramework import AutomationFramework

class SmokeTests(unittest.TestSuite):
    pass

if __name__ == '__main__':
    AutomationFramework().go()