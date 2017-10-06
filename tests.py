# import server
import unittest
import json
import bcrypt
import base64
from pymongo import MongoClient
from RestfulRoutingExercises import app
import pdb



class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        #  From my assumption this is another keyword that we inherit from the test case
        self.app = app.test_client()

        app.config['TESTING'] = True

        '''So essentially what we are doing here is that we are setting up our client and we are
        making our database global'''
        mongo = MongoClient('localhost', 27017)
        global db
        # Reduce encryption workloads for tests
        app.bcrypt_rounds = 4

        # The creation of our database

        db = mongo.trip_planner_test

        #  Creation of our server
        app.db = db

        # We do this to clear our database before each test runs
        db.drop_collection('posts')

        # Here we create the tests for the users as well as fill this function with methods

    def test_getting_a_user(self):
        self.app.post('/route',
                            headers=None,
                            data=json.dumps({"name":"Matthew",
                                            "student_id": "Personality",
                                            "fun_facts": "Care Free and Determined"}),
                                            content_type='application/json')
            # Make a get request to fetch the users to check if the user is actually getting created

        response = self.app.get('/route',
                                    query_string=dict(name="Matthew"))

            # When we get the repsonse we then want to decode it so it becomes a native object
        repsonse_json = json.loads(response.data.decode())
        print(response)


            # Here we actually test if the get request was successfull
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
