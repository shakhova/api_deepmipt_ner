from flask import json, request, Response #, jsonify

import ner

from app import app


EXTRACTOR = ner.Extractor()


@app.route('/get_ner', methods=['GET'])
def train_model():
    text = request.args.get('text', default = None, type = str)

    prediction = dict()
    for m in EXTRACTOR(text):
        prediction[' '.join([i.text for i in m.tokens])] = m.type

    json_string = json.dumps(prediction, ensure_ascii = False)

    return Response(json_string, content_type="application/json; charset=utf-8" )


@app.route('/')
def hello():
    return 'Hello! It`s NER API on flask!!!\n'