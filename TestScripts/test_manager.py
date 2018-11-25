import unittest
from TestScripts.RegressionTests.mainpage_tests import MainTest

# Get all tests from classes
mainTest = unittest.TestLoader().loadTestsFromTestCase(MainTest)

# Create a test suite combining all test cases
regressionSuite = unittest.TestSuite()
regressionSuite.addTest(mainTest)

smokeSuite = unittest.TestSuite()
smokeSuite.addTest(mainTest)

# Test runner
unittest.TextTestRunner(verbosity=2).run(smokeSuite)
