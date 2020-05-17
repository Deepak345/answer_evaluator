from flask import Flask, request, jsonify, render_template
import json
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)

@app.route('/')
def webprint():
    return render_template('answer.html')

@app.route('/obtain', methods=['POST'])
def obtain():
    answer = request.form['answer']
    print(answer)
    #data preprocessing
    response = jsonify(predictor(answer)) #answer = preprocessed attribute
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

def predictor(test):
    # classifier = pickle.load(open('model.sav','rb'))
    # result = classifier.predict(test)
    # print(result)
    ret = {'type' : "JSON/TXT"}
    # ret['result'] = str(result[0])
    ret['result'] = str(50)
    print(ret)
    return ret






app.run(port=8000, debug=True)
     