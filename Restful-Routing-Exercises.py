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
        '''The way we can go about this is by actually finding the documents by their object id and
        retrieve them that way therefore we can then have a safe way of finding what documents
        populate our database'''


        #  We iterate through these documents by locating their post id
        locating_by_object_id = post_collection.find_one({"_id": ObjectId(inserted_document.inserted_id)})

        if locating_by_object_id:
            return (locating_by_object_id, 200, None)
        else:
            return(None,400,None)


    def get(self, document_id):
        # Since this is a get request essentially we have to be get the resources and we are fetching by id
        '''Therefore we can go about this by accessing the same collection so essentially we have to be able to
        access the same collection by using the same naming coneventions if we did not access the same collection
        our results will turn out nil because we are checking a none existent collection'''

        # Therefore let us access the same collection
        post_collection = app.db.posts

        # Now that we are in the collection we have to iterate through the documents
        location_of_documents = post_collection.find_one({"_id": ObjectId(document_id)})

        if location_of_documents is None:
            response = jsonify(data=[])
            response.status_code = 404
            return (response)
            '''So essentially what jsonify does is that it allows  us
            to query an api and get json back not to be confused with what json.dumps does and that allows us
            to format something of its native schema and format it into a json object'''
        else:
            return location_of_documents

    '''So essentially what this line of code does is that it takes the place of the routes and what that essentially
    does is that it allows us to say that since we are inheriting from the Resource class we have these key words
    such as post and get and that automatically knows that depending on the keyword it will be a get or post request'''

    api.add_resource(location_of_documents, '/route')
    '''Essentially what this line of code does is that it allows us to send almost dummy data between our testing file
    and this server file that is why we do not need to encode the data becuase it is not server to client it is essentially
    file to file'''


if __name__ == '__main__':
    # Turn this on in debug mode to get detailled information about request related exceptions: http://flask.pocoo.org/docs/0.10/config/
    app.config['TRAP_BAD_REQUEST_ERRORS'] = True
    app.run(debug=True)
