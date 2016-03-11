#!/usr/bin/env python

from flask import Flask, jsonify
from flask import make_response
from flask.ext.script import Manager

app = Flask(__name__)
manager = Manager(app)

rhymes = {
    "all": [
        "decalogue",
        "demagogue",
        "antilog",
        "apologue",
        "backlog",
        "bulldog",
        "dialog",
        "dialogue",
        "duologue",
        "emmenagogue",
        "epilogue",
        "firedog",
        "galactagogue",
        "hangdog",
        "hog",
        "hogg",
        "ideologue",
        "log",
        "monologue",
        "sheepdog",
        "sundog",
        "underdog",
        "warthog",
        "waterdog"
    ]
}

@app.route('/words/dog/rhymes', methods=['GET'])
def get_rhymes():
    return jsonify({"rhymes": rhymes})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/')
def index():
    return "Hello, World! Greeting from python."


if __name__ == '__main__':
    manager.run()
