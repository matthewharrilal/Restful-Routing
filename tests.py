import server
import unittest
import json
import bcrypt
import base64
from pymongo import MongoClient

class TriplPlannerTestCase(unittest.TestCase):
    def setUp(self):
        #  From my assumption this is another keyword that we inherit from the test case
        self.app  = server.app.test_client()

        server.app.config['Testing'] = True

        '''So essentially what we are doing here is that we are setting up our client and we are
        making our database global'''
        mongo = MongoClient('localhost', 27017)
        global db
        # Reduce encryption workloads for tests
        server.app.bcrypt_rounds = 4

        # The creation of our database

        db = mongo.trip_planner_test

        #  Creation of our server
        server.app.db = db

        # Here we create the tests for the users as well as fill this function with methods
        def testCreateUser(self):
            '''So essentially let us explain what is going on here we are going to basically send dummy data to our server and see if
            it can send that data to the database this is almost acting as our paw'''
            

if __name__ == '__main__':
    unittest.main()
