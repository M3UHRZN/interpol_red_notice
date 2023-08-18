from flask import Flask, render_template
import pika
import json
import os
from datetime import datetime
from database import Database

app = Flask(__name__)

RABBITMQ_HOST = "container_c"  
QUEUE_NAME = "interpol_data_queue"  

db = Database()

@app.route("/")
def index():
    messages = db.get_messages()
    return render_template("index.html", messages=messages)

def get_messages_from_queue():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
    channel = connection.channel()

    channel.queue_declare(queue=QUEUE_NAME, durable=True)

    messages = []

    def process_message(ch, method, properties, body):
        data = json.loads(body)
        timestamp = data.get('timestamp')
        content = data.get('content')
        
        db.save_message(timestamp=timestamp, content=content)

        messages.append(data)


    channel.basic_consume(queue=QUEUE_NAME, on_message_callback=process_message, auto_ack=True)

    print("Veri dinleniyor. Çıkmak için CTRL+C tuşlarını kullanabilirsiniz.")
    channel.start_consuming()

    return messages

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
