from flask import Blueprint, jsonify, request
from gensim.models import Word2Vec
import src.training.pre_processing as pre_processing
import nltk
import numpy as np 
import nltk
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min

blueprint_text = Blueprint(name="text", import_name=__name__)
n_clusters = 3

@blueprint_text.route("/summarization", methods=["POST"])
def summarization():
    try:
        data = request.json['content']
        sum = kmeans(data)

        return jsonify({"code": 0, "sum": sum})
    except:
        return jsonify({"code": 1, "sum": False})

def kmeans(content):
    w2v_model = Word2Vec.load('src/training/w2v.model')
    vocabulary = []
    for word in w2v_model.wv.key_to_index:
        vocabulary.append(word)

    # read root sentences and normalize sentences
    root_sentences = nltk.sent_tokenize(content)
    contents_parsed = pre_processing.text_preprocess(content)
    sentences = nltk.sent_tokenize(contents_parsed)

    X = []
    for sentence in sentences:
        words = sentence.split(" ")
        sentence_vec = np.zeros((128))
        
        for word in words:
            if word in vocabulary:
                sentence_vec+=w2v_model.wv[word]

        X.append(sentence_vec)

    print("Number of element: " + str(len(X)))

    kmeans = KMeans(n_clusters=n_clusters)
    kmeans = kmeans.fit(X)

    print("K-Means Clustering\n")
    avg = []
    for j in range(n_clusters):
        print("Cụm", j+1)
        idx = np.where(kmeans.labels_ == j)[0]
        print(idx)
        avg.append(np.mean(idx))
        print("Thứ tự trung bình: ", round(np.mean(idx), 2))
        print("="*115)

    closest, _ = pairwise_distances_argmin_min(kmeans.cluster_centers_, X)

    print("Các câu gần", n_clusters, "tâm cụm nhất",closest)
    ordering = sorted(range(n_clusters), key=lambda k: avg[k])

    print("\nKết quả tóm tắt:\n")
    
    root_summary = ' '.join([root_sentences[closest[idx]] for idx in ordering])
    print(root_summary)

    return root_summary