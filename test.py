import unittest
import pandas
import sys
import Userclass

class clienttest(unittest.TestCase):

    def test_login(self):
        '''

        '''
        tlog = pandas.DataFrame(columns=['username'])
        tlog['username'] = ['test']
        tlog['password'] = ['1234']
        tlog['isAdmin'] = 1

        Userclass.createdusers = tlog
        expresults = ["\nWrong password!", "\nUsername not registered", "\nLogin completed."]
        obtresults = []
        tests = [
            ['test', '1234'],
            ['test2', '123'],
            ['test', '123']
        ]

        for test in tests:
            obtresults.append(Userclass.login(
                test[0], test[1]))
        Userclass.quit()

        self.assertListEqual(obtresults, expresults)

def step_completed(test_to_use):

    load = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(test_to_use))
    runtest = unittest.TextTestResult(verbosity=2)
    result = runtest.run(suite)

    if result.skipped:
        return False

    return result.wasSuccessful()

def login_test():
    print('*'*60 + "\nTesting:\n")
    return step_completed(clienttest)

if __name__ == "__main__":
    if login_test() is not True:
        print("\n\tThe first step did not pass,")
        sys.exit(1)

    sys.exit(0)
