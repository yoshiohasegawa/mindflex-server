from flask import Flask, json, jsonify, request
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load .env variables
load_dotenv()
db_name = os.getenv('DB_NAME')
db_username = os.getenv('DB_USERNAME')
db_password = os.getenv('DB_PASSWORD')

# Initialize Flask server
app = Flask(__name__)

# Establish MongoDB connection
client = MongoClient(f'mongodb+srv://{db_username}:{db_password}@mindflexcluster.csmom.mongodb.net/{db_name}?retryWrites=true&w=majority')
# Connect to mindflex database
db = client.get_database('mindflex')
# questions table
questions = db.questions


# Parse _id property value of ObjectId to String
def parseObjectId(obj):
    obj['_id'] = str(obj['_id'])
    return obj


@app.route('/', methods=['GET'])
def homepage():
    return 'Welcome to the Mindflex API'

@app.route('/api/questions', methods=['GET'])
def get_questions():
    questions_data = list(questions.find())
    questions_data = list(map(parseObjectId, questions_data))

    return jsonify({'data': questions_data})

if __name__ == '__main__':
    app.run(debug=True)