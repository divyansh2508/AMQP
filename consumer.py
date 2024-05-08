import pika
import pymongo
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

try:
    client = MongoClient('mongodb+srv://dsinghal250802:C90WzMntXobMCBCK@cluster0.hawxfrf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
    db = client['messages']
    collection = db['receive']
    print("Connection to MongoDB is Successfull!!")

except ConnectionFailure as e:
    print("Connection Failed: ", e)

def on_message_received(ch, method, properties, body):
    message = body.decode('utf-8')
    print(message)
    if len(message) < 2:
        print("Message is too short!!")
        return
    else:
        document = {"message": message}
        collection.insert_one(document)
        print(f"Received and Saved new message: {message}")

connection_params = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_params)

channel = connection.channel()

channel.queue_declare(queue = 'letterbox')

channel.basic_consume(queue = 'letterbox', auto_ack = True, on_message_callback = on_message_received)

print("Start Consuming")

try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()

connection.close()