from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import time 

app=Flask(__name__)
CORS(app)

@app.route('/ikon/v1/topic/getall',methods=['GET'])
def get_all_topics():
    return jsonify([{"cveTopic": 9,"topicName": "COLORS"},{"cveTopic": 7,"topicName": "GERUNDIO"},{"cveTopic": 5,"topicName": "OBJECT PRONOUN"},{"cveTopic": 1,"topicName": "SUBJECT PRONOUN"},{"cveTopic": 8,"topicName": "TIME"},{"cveTopic": 6,"topicName": "VERB TO BE"}])

@app.route('/ikon/v1/uploadFile',methods=['POST'])
def upload_file():
    file = request.files['files']
    type_file = request.headers.get('X-type')
    print(type_file)
    filename = file.filename
    newFileName = filename.split('.')[0] + '_' + str(int(time.time())) + '.' + filename.split('.')[1]
    newFileName= newFileName.replace(' ','_')
    t=str(time.time())
    file.save(os.path.join('/home/luisd/Escritorio/work/IKON/ikons/public/',type_file, newFileName))
    return jsonify({"status":200,"message": "File uploaded successfully","path": "http://localhost:8080/"+type_file+'/'+newFileName})

if __name__ == '__main__':
    app.run(debug=True,port=9095)

