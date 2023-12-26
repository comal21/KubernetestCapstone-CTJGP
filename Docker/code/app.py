#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
import os

from flask import Flask, jsonify, request

app = Flask(__name__)

notes = [
    {
        "author": "hightower",
        "title": "Kubernetes up and Running"
    },
    {
        "author": "navathe",
        "title": "Database Fundamentals"
    },
    {
        "author": "ritchie",
        "title": "Let us C"
    }
]

@app.route("/")
def hello():
    return "Welcome to my bookstore!"

@app.route("/v1/books/")
def list_all_books():
    list = []
    for item in notes:
       list.append({'book':item['title']})
    return jsonify(list)

@app.route("/v1/books/<string:author>")
def get_by_author(author):
    for item in notes:
	    if item['author'] == author:
	       data = item
    return jsonify(data)
    if not item:
        return jsonify({'error': 'Author does not exist'}), 404

@app.route("/v1/books/", methods=["POST"])
def add_book():
    author = request.json.get('author')
    book = request.json.get('title')
    if not author or not book:
        return jsonify({'error': 'Please provide Author and Title'}), 400
    else:
        data = request.get_json()
        notes.append(data)
        return jsonify({'message': 'Added book successfully','author':author,'book': book}),200

if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=5000)
