# AMQP
This repository aims to develop a backend system in Python that handles incoming AMQP messages via RabbitMQ and stores them in MongoDB.

AMQP - To give it a brief description, AMQP stands for Advanced Message Queuing Protocol. It is an open standard protocol used for establishing communication between different systems.
RabbitMQ  - It is an open source message broker software which implements AMQP to facilitate the connection between different systems.

There are 2 files one is the producer.py and second one is the consumer.py. Let's dive into these files and understand it's logic.

#producer.py:

In this file firstly we have imported "pika" a package, which is used to interact with "RabbitMQ" which is an open source message broker.
import pika

Then the connection parameter is being set which is "localhost".
connection_params = pika.ConnectionParameters('localhost')

After the connection is established, channel is set up to provide a medium to commmunicate.
channel = connection.channel()

A "queue" is then declared for the consumer to listen to the messages sent by the producer.
channel.queue_declare(queue='letterbox')

A test message is written in order to check for the workflow.
Used "basic_publish" to specify the exchange for the message to be sent from the publisher end. The attributes in this function are:

channel.basic_publish(exchange ='', routing_key='letterbox', body=message)

exchange: This parameter specifies which exchange is being used. In this case it hasn't got any name, but one can name it too.
routing_key: This parameter acts as a password as it determines which queue should receive a particular message.
body: This parameter contains the actual message to be sent.

Then after the completion of the work the connection is cosed or stopped.
connection.close()

#consumer.py:

In this file firstly we have imported all the required packages, like "pika", then the "pymongo" to establish the connection between the server and the MongoDB.
MongoCLient is used for setting up the connection.
ConnectionFailure is used to check for any issue occured while the connection is being established.

import pika
import pymongo
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

Implemented exceptional handling to check if the connection with the database has been established or not and created the database and the collection.

Created a function "on_message_received" to apply the decoding and the sending of message to the database.
Attributes used in the function are:

def on_message_received(ch, method, properties, body):

ch: Channel (ch) parameter is used to specify from which channel the message is coming.
method: This parameter contains all the meta data or we can say vital information to authenticate the message. For eg, routing key, exchange name, etc.
properties: This paramter contains the information about the structure of the message incoming. For eg., content type, headers, etc.
body: This parameter contains the actual message, also known as payload.

All these parameters are crucial for the working of this function.

In this function first we decoded the body into a message using "utf-8" since, it's very common and easy to implement.

Then a check has been implemented for the length of the message, like for length, the code will accept the message whose length is greater than 2 characters.

When the check is passed the data is then stored to database using the insert_one function.

For confirmation purpose the message will be displayed in the console.

Then the connections are done.

Queue is again declared.
NOTE: This does not create another queue if the queue of the same name is present, instead it will continue with the already initialized queue.

Used "basic_consume" to consume messages from a queue. It's an asynchronous consumption to avoid message blocking for the awaiting responses from the previous called methods.
The parameters it contains are:

queue: specifies which queue name in this case it is "letterbox".
auto_ack: acknowledges the message has been received automatically, in this case, it is set to "True".
on_message_callback: this parameter is used to take the function which is responsible for handling the messages and processing them.

Then the exception handling is used in case of function getting terminated due to keyboard interruption.
Then after the completion of the work the connection is cosed or stopped.

#Setup
Install the packages pika and pymongo, with the following command on Windows respectively:
pip install pika
python -m pip install "pymongo[srv]"

#How to run the project?

To run this, first go to file consumer.py, run it using the command python consumer.py

then go to file producer.py, and type the command python producer.py

#Key Outcomes:

Gained the understanding of the AQMP protocol and RabbitMQ.
Figured out the configurations setup of RabbitMQ and AMQP protocol.
Implemented the python services to establish the communication between the producer and the consumer using RabbitMQ and AMQP protocol.
Integrated MongoDB with Python to store the received messages in the database.

Thank You
