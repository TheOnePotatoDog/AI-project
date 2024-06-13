from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/api/getBots', methods=['GET'])
def get_bots():
    bots = [
        {"name": "Alignment Bot", "description": "Ensures AI alignment with human values."},
        {"name": "Misalignment Bot", "description": "Simulates AI misalignment scenarios."},
        {"name": "Testing Bot", "description": "Tests AI for alignment issues."},
        # Add more bots as needed
    ]
    return jsonify(bots)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)