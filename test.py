'''
This program deals with the testing of
the server-client application
'''
import unittest
import sys
import pandas
from Userclass import User

class TestClient(unittest.TestCase):
    '''
    This class defines the tests that are conducted
    for the functions defined in the client-server application
    '''
    def test_login(self):
        '''
        This function deals with test for login data
        '''
        tlog = pandas.DataFrame(columns=['username'])
<<<<<<< HEAD
        tlog['username'] = ['test']
        tlog['password'] = ['123']
=======
        tlog['username'] = ['test1']
        tlog['password'] = ['1234']
>>>>>>> bfbad923f6c1b56ebae0af53380282cc7be98966
        tlog['isAdmin'] = 1

        user_test = User()
        user_test.createdusers = tlog
<<<<<<< HEAD
        expresults = ['\nWrong password!']
        obtresults = []
        tests = [
            ['test', '1234'],
=======
        user_test.createdusers.to_csv('ServerAccessSession/Users.csv', index = False)
        expresults = ['\nWrong password!', '\nUsername not registered', '\nLogin completed.']
        obtresults = []
        tests = [
            ['test1', 12356],
            ['test2', 123],
            ['test1', 1234]
>>>>>>> bfbad923f6c1b56ebae0af53380282cc7be98966
        ]

        for test in tests:
            obtresults.append(user_test.login(test[0], test[1]))
        user_test.quit()
<<<<<<< HEAD
        login_rst = pandas.DataFrame(columns=['username'])
        login_rst.to_csv('ServerAccessSession/Users.csv', index=False)
=======
        login_rest = pandas.DataFrame(columns = ['username'])
        login_rest.to_csv('ServerAccessSession/logged_in_Users.csv', index= False)
        login_rst = pandas.DataFrame(columns = ['username','password','isAdmin'])
        login_rst.to_csv('ServerAccessSession/Users.csv', index = False)
>>>>>>> bfbad923f6c1b56ebae0af53380282cc7be98966

        self.assertListEqual(obtresults, expresults)

'''
    def test_registration(self):
        '''
        This function deals with tests for registration
        '''
        tlog = pandas.DataFrame(columns=['username'])
        tlog['username'] = ['test']
        tlog['password'] = ['123']
        tlog['isAdmin'] = 1

        user_test = User()
        user_test.createdusers = tlog
        expresults = ['\nRegistered user successfully.']
        obtresults = []
        tests = [
            ['test', '1234', 'Admin']
        ]

        for test in tests:
            obtresults.append(user_test.register(
                test[0], test[1], test[2]))
        user_test.quit()
<<<<<<< HEAD
        login_rst = pandas.DataFrame(columns=['username'])
        login_rst.to_csv('ServerAccessSession/Users.csv', index=False)

=======
        #login_rst = pandas.DataFrame(columns = ['username','password','isAdmin'])
        #login_rst.to_csv('ServerAccessSession/Users.csv', index = False)
    
>>>>>>> bfbad923f6c1b56ebae0af53380282cc7be98966
        self.assertListEqual(obtresults, expresults)
'''

    def test_read_file(self):
        '''
        This function deals with testing of read file
        '''
        tlog = pandas.DataFrame(columns=['username'])
        tlog['username'] = ['test']
        tlog['password'] = ['123']
        tlog['isAdmin'] = 1
        obtresults = []
        expresults = ['\ngiven file not found',
                      '\nRead file from 0 to 100 are - \nDontChangeThisContent'
                     ]
        user_test = User()
        user_test.createdusers = tlog
        user_test.login('test', '123')
        user_test.change_folder('testfolder1')
        obtresults.append(user_test.read_file('test_read2.txt'))
        obtresults.append(user_test.read_file('test_read.txt'))
        user_test.quit()
        login_rst = pandas.DataFrame(columns=['username'])
        login_rst.to_csv('ServerAccessSession/Users.csv', index=False)

        self.assertListEqual(obtresults, expresults)


    def test_commands(self):
        '''
        This test the commands used by the client
        '''
        user_test = User()
        exptoutput = user_test.commands

        user_test.quit()

        login_rst = pandas.DataFrame(columns=['username'])
        login_rst.to_csv('ServerAccessSession/Users.csv', index=False)

        self.assertTrue(exptoutput)


def step_completed(test_to_use):
    '''
    This function deals with execution of all the
    tests in sequence and returns the result
    '''
    load = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(load.loadTestsFromTestCase(test_to_use))
    runtest = unittest.TextTestRunner(verbosity=2)
    result = runtest.run(suite)

    if result.skipped:
        return False

    return result.wasSuccessful()


def testing():
    '''
    This function executes the function of step_completed
    '''
    print('*'*60 + "\nTesting:\n")
    return step_completed(TestClient)

if __name__ == "__main__":
    if testing() is not True:
        print("\n\tThe tests did not pass,")
        sys.exit(1)

    sys.exit(0)
