from flask import Flask, jsonify, request

app = Flask(__name__)

# Пример данных
data = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"},
]

# Главная страница
@app.route('/')
def index():
    return jsonify({"message": "Люплю типя, люплю типя"})

# Получение всех элементов
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(data)

# Получение элемента по ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in data if item["id"] == item_id), None)
    return jsonify(item) if item else jsonify({"error": "Item not found"}), 404

# Добавление нового элемента
@app.route('/items', methods=['POST'])
def add_item():
    new_item = request.json
    new_item['id'] = len(data) + 1
    data.append(new_item)
    return jsonify(new_item), 201

if __name__ == '__main__':
    app.run(debug=True)
