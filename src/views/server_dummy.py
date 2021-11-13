from flask import Flask, jsonify
from flask_cors import CORS

app=Flask(__name__)
CORS(app)
@app.route('/ikon/v1/topic/getall',methods=['GET'])
def get_all_topics():
    return jsonify([{"cveTopic": 9,"topicName": "COLORS"},{"cveTopic": 7,"topicName": "GERUNDIO"},{"cveTopic": 5,"topicName": "OBJECT PRONOUN"},{"cveTopic": 1,"topicName": "SUBJECT PRONOUN"},{"cveTopic": 8,"topicName": "TIME"},{"cveTopic": 6,"topicName": "VERB TO BE"}])
if __name__ == '__main__':
    app.run(debug=True)