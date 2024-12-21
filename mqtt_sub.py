import asyncio
from gmqtt import Client as MQTTClient

# Define the MQTT broker details
BROKER = 'localhost'  # Replace with your broker's address if not localhost
PORT = 1884  # Default MQTT port
TOPIC = '/events'  # Topic to listen to

# Define the client ID
CLIENT_ID = 'mqtt_listener'

# Create the message handler
async def on_message(client, topic, payload, qos, properties):
    print(f"Received message on topic '{topic}': {payload.decode()}")

# Create the connection handler (regular function instead of async)
def on_connect(client, flags, rc, properties):
    print("Connected to the broker!")
    # Subscribe to the topic upon successful connection
    client.subscribe(TOPIC, qos=1)

# Create the disconnection handler
def on_disconnect(client, packet, exc=None):
    print("Disconnected from the broker.")

async def main():
    # Create the MQTT client
    client = MQTTClient(CLIENT_ID)

    # Assign event handlers
    client.on_connect = on_connect  # Regular function
    client.on_message = on_message  # Async function
    client.on_disconnect = on_disconnect  # Regular function

    # Connect to the broker
    await client.connect(BROKER, PORT)

    # Run the loop to keep the connection alive and listen for messages
    try:
        await asyncio.Future()  # Keep the program running
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        await client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
