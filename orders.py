from flask import Flask, jsonify

app = Flask(__name__)

# Assuming you have a list of orders (order_data) from your database or elsewhere
order_data = [
    {"order_id": 1, "customer_id": 1, "product_id": 2, "quantity": 3},
    {"order_id": 2, "customer_id": 2, "product_id": 3, "quantity": 2},
    # Add more order data here
]

@app.route('/orders', methods=['GET'])
def list_orders():
    # Return the list of orders as JSON
    return jsonify(order_data)

if __name__ == '__main__':
    app.run(debug=True)