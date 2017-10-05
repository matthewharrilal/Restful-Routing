from flask import Flask, request, make_response
from flask_restful import Resource, Api
from pymongo import MongoClient
from bson.objectid import ObjectId
import bcrypt

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
app.db = client.trip_planner_development
app.bcrypt_rounds = 12
api = Api(app)

class User(Resource):
    #  This class essentially what it does is that we inherit from this already made flask class called Resource

    # Let us create the route that will trigger our function as well as flask server
    @app.route('/route',methods=["POST", "GET"])
    def post():
        # This is our post function and this is going to handle the posting of our resources
        requested_dictionary = request.json
        # We are storing the dictionary that we get from paw in this variable called requested dictionary

        # Now that we have the dictionary we have to insert as a document therefore we have to create a collection
        post_collection = app.db.posts

        # Now that we have the collection we can now insert the json dictionary as a document
        inserted_document = post_collection.insert_one(requested_dictionary)

        # Now that we have inserted the document we now have to retrieve to see if it even exists without checking mongodb

        return (inserted_document)



if __name__ == '__main__':
    # Turn this on in debug mode to get detailled information about request related exceptions: http://flask.pocoo.org/docs/0.10/config/
    app.config['TRAP_BAD_REQUEST_ERRORS'] = True
    app.run(debug=True)
