from flask import Blueprint, jsonify, request
import py_stringmatching as sm

blueprint_string_matching = Blueprint(name="string_matching", import_name=__name__)
threshold = 0.6

@blueprint_string_matching.route("/check-matching", methods=["POST"])
def summarization():
    try:
        input1 = request.json['text1']
        input2 = request.json['text2']

        tokenize = sm.QgramTokenizer(qval=3)
        
        score = sm.Jaccard().get_sim_score(tokenize.tokenize(input1), tokenize.tokenize(input2))
        print(score)
        result = False

        if score > threshold: 
            result = True

        return jsonify({"code": 0, "matching": result})
    except: 
        return jsonify({"code": 1, "matching": False})