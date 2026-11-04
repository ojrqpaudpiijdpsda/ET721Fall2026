from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
# in-memory database (dictionary)
items = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/items', methods =['POST'])
def create_item():
    " " " get_json method is used to read JSON data sent by the client in an HTTP request " " "
    data = request.get_json()
    " " " generate a new unique ID for the new item " " "

    item_id = str(len(items)+1)
    " " " add the data collected for the new item " " "
    items[item_id] = data
    " " " jsonify converts a Python dictionary into a json response, and returns status code as 201 (your request worked and new resource was created) " " "
    return jsonify({'id':item_id, 'item': data}), 201

# READ ALL ITEMS
@app.route('/items', methods = ['GET'])
def get_items():
    return jsonify(items)
# READ, UPDATE, DELETE SINGLE ITEM
@app.route('/items/<item_id>', methods=['GET','PUT', 'DELETE'])
def handle_item(item_id):
    item = items.get(item_id)
# READ
    if request.method == 'GET':
        if not item:
            return jsonify({'Error':"Item not found"}), 404
        
        return jsonify(item)
if __name__ == "__main__":
    app.run(debug=True)