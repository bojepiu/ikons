from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import time 

app=Flask(__name__)
CORS(app)
#SECTION CARDS
@app.route('/ikon/v1/card/getall', methods=['GET'])
def get_all_cards():
    return jsonify({"cards": "XD"})

@app.route('/ikon/v1/card/<id>', methods=['GET'])
def get_card(id):
    return jsonify({"card": "XD","id":id})

@app.route('/ikon/v1/card', methods=['POST'])
def insert_update_card():
    try:
        js=request.json
        print(js)
        return jsonify({"card": js['cveCard'],"status": "updated"}),200
    except:
        return jsonify({"status": "error"}),400

@app.route('/ikon/v1/card/<id>', methods=['DELETE'])
def delete_card(id):
    return jsonify({"card": "XD","id":id,"status": "deleted"}),200

@app.route('/ikon/v1/card/bytopic/<cveTopic>', methods=['GET'])
def get_cards_by_topic(cveTopic):
    return jsonify({"cards": "XD","cveTopic":cveTopic})


@app.route('/ikon/v1/topic/getall',methods=['GET'])
def get_all_topics():
    return jsonify([{"cveTopic": 1,"topicName": "PRONOMS"},{"cveTopic": 2,"topicName": "COLORS"},{"cveTopic": 3,"topicName": "OBJECT PRONOUN"},{"cveTopic": 6,"topicName": "SUBJECT PRONOUN"},{"cveTopic": 4,"topicName": "TIME"},{"cveTopic": 5,"topicName": "VERB TO BE"},{"cveTopic":200,"topicName":"PRONOMS2"},{"cveTopic":201,"topicName":"PRONOMS3"}])

@app.route('/ikon/v1/uploadFile',methods=['POST'])
def upload_file():
    file = request.files['files']
    type_file = request.headers.get('X-type')
    filename = file.filename
    newFileName = filename.split('.')[0] + '_' + str(int(time.time())) + '.' + filename.split('.')[1]
    newFileName= newFileName.replace(' ','_')
    file.save(os.path.join('/home/luisd/Escritorio/work/IKON/ikons/public/',type_file, newFileName))
    return jsonify({"status":200,"message": "File uploaded successfully","path": "http://localhost:8080/"+type_file+'/'+newFileName})

app.handle_exception = lambda e, s: jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True,port=9095)

