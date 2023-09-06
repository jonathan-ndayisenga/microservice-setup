from flask import Flask, request, jsonify;

app = Flask(__name__)

@app.route('/api/shipping/receive', methods=['POST'])
def receive_shipping_order():
    data = request.json

    # Extract relevant information from the JSON data
    order_id = data.get('order_id')
    customer_id = data.get('customer_id')

    # Perform logic to alert the Shipping Service about the order

    # Return a response indicating success
    return jsonify({"message": "Order information sent to Shipping Service"})

if __name__ == '__main__':
    app.run(debug=True)
    
    
    

#notifications
@app.route('/notifications/send', methods=['POST'])
def send_notification():
    data = request.json

    # Extract relevant information from the JSON data
    customer_id = data.get('customer_id')
    message = data.get('message')

    # Perform logic to notify the Notification Service

    # Return a response indicating success
    return jsonify({"message": "Notification sent to Notification Service"})

if __name__ == '__main__':
    app.run(debug=True)
    
 

import requests;


#sending an order to the Shipping Service
shipping_url = 'https://127.0.0.1:8080/api/shipping/receive'
shipping_data = {"order_id": order_id, "customer_id": customer_id}
response = requests.post(shipping_url, json=shipping_data)

#sending a notification to the Notification Service
notification_url = 'https://127.0.0.1:8081/notifications/send'
notification_data = {"customer_id": customer_id, "message": message}
response = requests.post(notification_url, json=notification_data)
   
