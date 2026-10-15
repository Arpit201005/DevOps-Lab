# Exercise 2: Flask Deployment on Minikube using Kubernetes

## Objective
To deploy a Python Flask web application using Docker and Kubernetes on a local Minikube cluster.

## Technologies Used
- Python
- Flask
- Docker
- Kubernetes
- Minikube
- kubectl
- Ubuntu on WSL2
- Visual Studio Code

## Project Structure

```text
Exercise2/
├── app.py
├── Dockerfile
├── flask-deployment.yaml
├── README.md
└── screenshots/
```

## Application Description

This exercise deploys a simple Flask web application inside a Kubernetes Pod. The application listens on port `15000` and returns the message:

`Hello from Flask on Kubernetes!`

## Implementation Steps

### 1. Start Minikube

```bash
minikube start --driver=docker
```

### 2. Verify the Kubernetes Cluster

```bash
minikube status
kubectl get nodes
```

The Minikube node was verified to be in the `Ready` state.

### 3. Build the Docker Image

```bash
docker build -t flask-app:latest .
```

### 4. Load the Image into Minikube

```bash
minikube image load flask-app:latest
```

### 5. Deploy the Application

```bash
kubectl apply -f flask-deployment.yaml
```

This creates the Kubernetes Deployment and Service.

### 6. Check Deployment Status

```bash
kubectl get deployments
```

The `flask-app` Deployment reached `1/1` ready and available.

### 7. Verify the Pod

```bash
kubectl get pods -l app=flask-app
```

The Flask Pod reached the `Running` state with `1/1` ready.

### 8. Describe the Deployment

```bash
kubectl describe deployment flask-app
```

This command displays the container image, replica count, deployment conditions, and events.

### 9. View Application Logs

```bash
kubectl logs deployment/flask-app
```

The logs confirmed that the Flask development server started and was listening on port `15000`.

### 10. Check the Kubernetes Service

```bash
kubectl get services
```

### 11. Access the Application

```bash
minikube service flask-app-service --url
```

Open the generated URL in a browser to access the Flask application. Keep the terminal open while using the URL if required by the Docker driver.

## Results

- Minikube cluster started successfully.
- Docker image was made available to Minikube.
- Kubernetes Deployment and Service were created successfully.
- One Flask Pod was running and ready.
- Flask application startup was verified using Kubernetes logs.

Expected browser response after successful access:

`Hello from Flask on Kubernetes!`

## Screenshots

Add screenshots of the following results to the `screenshots/` directory:

1. Minikube cluster status.
2. Docker image build.
3. Kubernetes Deployment and Pod status.
4. Deployment description and Flask logs.
5. Kubernetes Service.
6. Flask application running in the browser.

## Conclusion

The Flask web application was containerized using Docker and deployed successfully on a local Minikube Kubernetes cluster. Kubernetes Deployment and Service resources were used to run and access the application.