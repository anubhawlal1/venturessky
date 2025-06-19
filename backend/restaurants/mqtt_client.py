import paho.mqtt.client as mqtt
import json
from typing import Callable, Dict, Any

class MQTTClient:
    def __init__(self, broker: str = "localhost", port: int = 1883):
        self.client = mqtt.Client()
        self.broker = broker
        self.port = port
        self.setup_callbacks()

    def setup_callbacks(self):
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_disconnect = self.on_disconnect

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
            # Subscribe to the restaurant orders topic
            client.subscribe("restaurant/orders")
        else:
            print(f"Failed to connect, return code {rc}")

    def on_message(self, client, userdata, msg):
        try:
            payload = json.loads(msg.payload.decode())
            print(f"Received message on topic {msg.topic}: {payload}")
            # Here you can add your message handling logic
        except json.JSONDecodeError:
            print(f"Invalid JSON message received: {msg.payload}")

    def on_disconnect(self, client, userdata, rc):
        print(f"Disconnected with result code: {rc}")

    def connect(self):
        try:
            self.client.connect(self.broker, self.port, 60)
            self.client.loop_start()
        except Exception as e:
            print(f"Failed to connect to MQTT broker: {e}")

    def disconnect(self):
        self.client.loop_stop()
        self.client.disconnect()

    def publish_order(self, order_data: Dict[str, Any]):
        """
        Publish a new order to the MQTT topic.
        
        Args:
            order_data: Dictionary containing order information
        """
        try:
            payload = json.dumps(order_data)
            self.client.publish("restaurant/orders", payload)
            print(f"Published order: {order_data}")
        except Exception as e:
            print(f"Failed to publish order: {e}")

# Example usage
if __name__ == "__main__":
    # Create MQTT client instance
    mqtt_client = MQTTClient()
    
    # Connect to the broker
    mqtt_client.connect()
    
    # Example order data
    order = {
        "restaurant_id": 1,
        "items": [
            {"name": "Pizza", "quantity": 2, "price": 12.99}
        ],
        "total": 25.98
    }
    
    # Publish the order
    mqtt_client.publish_order(order)
    
    # Keep the script running
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Disconnecting...")
        mqtt_client.disconnect() 