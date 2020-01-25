import unittest
import pandas
import sys
from Userclass import User

class clienttest(unittest.TestCase):

    def test_login(self):
        '''

        '''
        tlog = pandas.DataFrame(columns=['username'])
        tlog['username'] = ['test']
        tlog['password'] = ['123']
        tlog['isAdmin'] = 1

        user_test = User()
        user_test.createdusers = tlog
        expresults = ['\nWrong password!', '\nUsername not registered', '\nLogin completed.']
        obtresults = []
        tests = [
            ['test', '1234'],
            ['test2', '123'],
            ['test', '123']
        ]

        for test in tests:
            obtresults.append(user_test.login(
                test[0], test[1]))
        user_test.quit()
        login_rst = pandas.DataFrame(columns = ['username'])
        login_rst.to_csv('ServerAccessSession/Users.csv', index = False)

        self.assertListEqual(obtresults, expresults)


    def test_registration(self):
        tlog = pandas.DataFrame(columns=['username'])
        tlog['username'] = ['test']
        tlog['password'] = ['1234']
        tlog['isAdmin'] = 1

        user_test = User()
        user_test.createdusers = tlog
        expresults = ['\nUsername not available']
        obtresults = []
        tests = [
            ['test', '1234', 'Admin'],
            ['test2', '123', 'Admin'],
            ['test', '123', 'Admin']
        ]

        for test in tests:
            obtresults.append(user_test.register(
                test[0], test[1], test[2]))
        user_test.quit()
        login_rst = pandas.DataFrame(columns = ['username'])
        login_rst.to_csv('ServerAccessSession/Users.csv', index = False)

        self.assertListEqual(obtresults, expresults)


def step_completed(test_to_use):

    load = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(load.loadTestsFromTestCase(test_to_use))
    runtest = unittest.TextTestRunner(verbosity = 2)
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
