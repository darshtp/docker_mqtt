Ubuntu 20.04.6 LTS is used for this Repo.

Step 1.

Install Docker
>sudo apt install docker.io -y

Verify Docker installation
>docker --version

Start Docker service
>sudo systemctl start docker
>sudo systemctl enable docker

Step 2.

Pull the Mosquitto Docker image
>docker pull eclipse-mosquitto

Run the Mosquitto container
>docker run -d --name mosquitto -p 1883:1883 -p 9001:9001 eclipse-mosquitto

Verify that the container is running
>docker ps

Step3.

Install gmqtt Library
>pip install gmqtt

Python Code
>nano mqtt_sub.py

Step4.

Create a Dockerfile to dockerize the Python Application
>nano Dockerfile

Create requirements.txt
>nano requirements.txt

Step5.

Build the Docker image
>docker build -t mqtt_sub:latest .

Run the Docker container
>docker run -d --name mqtt_sub --network host mqtt_sub

Step6.

install mosquitto-clients to use mosquitto_pub
>sudo apt install mosquitto-clients -y

Publish mqtt message manually
>mosquitto_pub -h localhost -t "/events" -m '{"sensor_value": 20.2}'

Step7.

Check the logs of your mqtt_sub Docker container
>docker logs mqtt_sub

Expected message
>Received message on /events: {"sensor_value": 20.2}
