#!/usr/bin/env python3

import os
import random
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hotdice', methods = ['GET', 'POST'])
def hotdice():
    request_json = request.get_json(force=True)
    text_input = str(request_json["text"])

    dicerange_array = text_input.split()
    
    user_name = str(request_json["user_name"])
    diceroll = random.randint(0, 100)
    diceroll_result = user_name + " rolled a %s out of %s" % (str(diceroll), str(100))
    diceroll_out = {
                        "response_type": "ephemeral",
                        "icon_url": "https://funcamp.net/w/dice.png",
                        "username": "vegas",
                        "text": diceroll_result
                   }
    return jsonify(diceroll_out)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8090, debug=True)
