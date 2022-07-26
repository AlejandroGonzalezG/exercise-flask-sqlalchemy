from flask import Flask, jsonify, request, json
app = Flask(__name__)


todos = [
    {"label":"My first task", "done": False},
    {"label":"My second task", "done": True}
    ]

@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    decodedObject = json.loads(request.data)
    todos.append(decodedObject)
    print("Incoming request with the following body", decodedObject)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    decodedObject = json.loads(request.data)
    todos.pop(position)
    print("Incoming request with the following body", todos)
    return jsonify(todos)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)