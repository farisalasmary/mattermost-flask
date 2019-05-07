#!/usr/bin/env python3

import os
import random
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sitebot', methods = ['GET', 'POST'])
def sitebot():
    request_json = request.get_json(force=True)
    text_input = str(request_json["text"])

    dicerange_array = text_input.split()
    
    user_name = str(request_json["user_name"])
    text = f'Hello, {user_name}'
    
    response = {
                        "response_type": "ephemeral",
                        "icon_url": "https://funcamp.net/w/dice.png",
                        "username": "vegas",
                        "text": text
                   }
    return jsonify(response)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8090, debug=True)
