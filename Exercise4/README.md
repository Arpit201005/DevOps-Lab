# Exercise 4: Docker Networking with Multiple Containers

## Objective

Understand Docker networking concepts and configure a multi-container application using a custom bridge network.

## Steps of Execution

Create a custom bridge network to allow communication between the Flask, MySQL, and Redis containers.

### Command to create a bridge network:

```bash
docker network create --driver bridge my-bridge-net
```

### Command to verify the network:

```bash
docker network ls
```

### Command to inspect the network:

```bash
docker network inspect my-bridge-net
```

## Create the Flask Application

Create an `app.py` file with the following code:

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/about', methods=['GET'])
def about():
    return jsonify({
        "name": "Simple REST API",
        "version": "1.0",
        "description": "This is a simple REST API built with Flask."
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
```

Create a `requirements.txt` file:

```text
Flask==2.0.1
Werkzeug==2.0.3
```

Create a `Dockerfile`:

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
COPY app.py .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5001

CMD ["python", "app.py"]
```

### Command to build the Flask Docker image:

```bash
docker build -t flask-api .
```

## Launch the Containers

Start the MySQL container:

```bash
docker run -d --name mysql --network my-bridge-net -e MYSQL_ROOT_PASSWORD=LabPass123! mysql:8.0
```

Start the Redis container:

```bash
docker run -d --name redis --network my-bridge-net redis:latest
```

Start the Flask container:

```bash
docker run -d --name flask --network my-bridge-net -p 5001:5001 flask-api
```

### Command to verify the running containers:

```bash
docker ps
```

## Test the Flask Application

Open the following URL in a browser:

```text
http://localhost:5001/about
```

The application returns information about the REST API in JSON format.

## Test Connectivity Between Containers

Enter the Flask container:

```bash
docker exec -it flask sh
```

### Check the IP addresses of MySQL and Redis:

```bash
python -c "import socket; print(socket.gethostbyname('mysql')); print(socket.gethostbyname('redis'))"
```

### Test connectivity to MySQL:

```bash
python -c "import socket; s=socket.create_connection(('mysql',3306),5); print('MySQL connection successful'); s.close()"
```

### Test connectivity to Redis:

```bash
python -c "import socket; s=socket.create_connection(('redis',6379),5); print('Redis connection successful'); s.close()"
```

Exit the Flask container:

```bash
exit
```

## Clean Up

Stop the containers:

```bash
docker stop flask mysql redis
```

Remove the containers:

```bash
docker rm flask mysql redis
```

Remove the custom bridge network:

```bash
docker network rm my-bridge-net
```

## Conclusion

Docker networking was demonstrated by connecting Flask, MySQL, and Redis containers to a custom bridge network. Container name resolution and connectivity to the MySQL and Redis service ports were verified successfully.