from flask import Flask, request, jsonify

app = Flask(__name__)

candidates = {}

@app.route('/register', methods=['POST'])
def register_candidate():
    name = request.json['name']
    candidates[name] = 0
    return jsonify({'message': 'Candidate registered successfully!'})

@app.route('/vote', methods=['POST'])
def vote():
    candidate = request.json['candidate']
    if candidate in candidates:
        candidates[candidate] += 1
        return jsonify({'message': 'Vote cast successfully!'})
    return jsonify({'message': 'Candidate not found!'})

@app.route('/results', methods=['GET'])
def results():
    return jsonify(candidates)

if __name__ == '__main__':
    app.run(debug=True)
