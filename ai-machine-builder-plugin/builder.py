from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/v1/build', methods=['POST'])
def build_model():
    data = request.get_json()
    # Add your machine building logic here
    return jsonify({"status": "success", "data": data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8004)