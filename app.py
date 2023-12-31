from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MONGODB_URI = os.environ.get("MONGODB_URI")
DB_NAME = os.environ.get("DB_NAME")

client = MongoClient(MONGODB_URI)
db = client[DB_NAME]

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/moviezaki", methods=["POST"])
def homework_post():
    image_receive = request.form['imgurl1']
    comment_receive = request.form['comment1']
    rating_receive = request.form['rating1']
    title_receive = request.form['title2']
    synopsis_receive = request.form['synopsis1']
    doc = {
        'title': title_receive,
        'comment': comment_receive,
        'rating': rating_receive,
        'image': image_receive,
        'synopsis': synopsis_receive
    }
    db.fanmessages.insert_one(doc)
    return jsonify({'msg':'POST request!'})

@app.route("/moviezaki", methods=["GET"])
def web_mars_get():
    orders_list = list(db.lemmekuntul.find({}, {'_id': False}))
    return jsonify({'orders': orders_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)