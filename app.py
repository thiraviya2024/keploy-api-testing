from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory menu storage
menu = []

# ✅ Backend logic function for unit testing
def create_item(name, category, price, availability):
    item = {
        "name": name,
        "category": category,
        "price": price,
        "availability": availability
    }
    menu.append(item)
    return item

# ➕ Add a new item via API
@app.route('/menu', methods=['POST'])
def add_item():
    data = request.get_json()
    item = {
        "name": data.get("name"),
        "category": data.get("category"),
        "price": data.get("price"),
        "availability": data.get("availability")
    }
    menu.append(item)
    return jsonify({"message": "Item added successfully", "item": item}), 201

# 📄 View all items
@app.route('/menu', methods=['GET'])
def get_menu():
    return jsonify(menu), 200

# ✏️ Update an item by name
@app.route('/menu/<name>', methods=['PUT'])
def update_item(name):
    data = request.get_json()
    for item in menu:
        if item["name"].lower() == name.lower():
            item["category"] = data.get("category", item["category"])
            item["price"] = data.get("price", item["price"])
            item["availability"] = data.get("availability", item["availability"])
            return jsonify({"message": "Item updated", "item": item}), 200
    return jsonify({"error": "Item not found"}), 404

# ❌ Delete an item by name
@app.route('/menu/<name>', methods=['DELETE'])
def delete_item(name):
    for item in menu:
        if item["name"].lower() == name.lower():
            menu.remove(item)
            return jsonify({"message": "Item deleted"}), 200
    return jsonify({"error": "Item not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
