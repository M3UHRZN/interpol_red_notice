# interpol_red_notice

This project periodically retrieves data from the Interpol Red Notice website and sends it to a web server using the Flask module.

# Prerequisites to run the project:
#### Docker Desktop or Docker should be active on your computer.
  
#### To also make the RabbitMQ server operational, follow these steps:

Open the RabbitMQ command prompt by navigating to 
```
C:\Program Files (x86)\RabbitMQ Server\rabbitmq_server-3.2.3\sbin".
```
Enter the following command: 
```
rabbitmq-plugins enable rabbitmq_management".
```

#Usage:

First, ensure that Docker and RabbitMQ are up and running. Then, in the project's terminal, execute the following commands:
```
docker-compose build
# Afterward, run
docker-compose up
```
If you encounter issues with Docker installation or face errors, I recommend uninstalling Docker and then reinstalling it. You can achieve this by running the following command in the terminal:
```
docker-compose down
```

After running the code, data will be fetched and sent to your web server every hour. The communication port for RabbitMQ is 5672, and you can access its interface through "http://localhost:15672".

The web server can be accessed at "http://127.0.0.1:5000".
