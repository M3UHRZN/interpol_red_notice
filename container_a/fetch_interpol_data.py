import requests
import pika
import json
import time

INTERPOL_API_URL = "https://ws-public.interpol.int/notices/v1/red"
RABBITMQ_HOST = "container_c"
QUEUE_NAME = "interpol_data_queue"

class InterpolDataFetcher:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST, port=5672))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=QUEUE_NAME, durable=True)

    def fetch_interpol_data(self):
        try:
            response = requests.get(INTERPOL_API_URL)
            if response.status_code == 200:
                data = response.json()
                return data
            else:
                print("Failed to fetch Interpol data:", response.status_code)
                return None
        except Exception as e:
            print("Error fetching Interpol data:", e)
            return None

    def publish_to_queue(self, data):
        self.channel.basic_publish(
            exchange="",
            routing_key=QUEUE_NAME,
            body=json.dumps(data),
            properties=pika.BasicProperties(delivery_mode=2)
        )
        print("Veri RabbitMQ kuyruğuna gönderildi")

    def close_connection(self):
        self.connection.close()

def main():
    interpol_fetcher = InterpolDataFetcher()

    while True:
        data = interpol_fetcher.fetch_interpol_data()
        if data:
            interpol_fetcher.publish_to_queue(data)
        time.sleep(3600)

        interpol_fetcher.close_connection()


if __name__ == "__main__":
    main()
