from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_greeting():
    return jsonify(greeting="Hello, World!")

@app.route('/', methods=['POST'])
def post_greeting():
    data = request.get_json()
    name = data.get('name', 'World')
    return jsonify(greeting=f"Hello, {name}!")

if __name__ == '__main__':
    app.run(debug=True)
