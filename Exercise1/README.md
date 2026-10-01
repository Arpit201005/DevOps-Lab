\# Exercise 1



\## Steps of Execution



Run the following commands:



```bash

minikube start --driver=docker

kubectl run hello-k8s --image=nginx --port=80

kubectl get pods

kubectl expose pod hello-k8s --type=NodePort --port=80

minikube service hello-k8s
```
Description:-
In this exercise, an Nginx container is deployed as a Pod in a local Kubernetes cluster using Minikube.
The Pod is then exposed using a NodePort Service, allowing the Nginx application to be accessed through a web browser.

Output:-
1\. Minikube Cluster

!\[Minikube Cluster](./Screenshot_1.png)

2\. Nginx Pod

!\[Nginx Pod](./Screenshot_2.png)

3\. Nginx Service

!\[Nginx Service](./Screenshot_3.png)


Result:-
The Nginx welcome page was successfully deployed and accessed through Kubernetes using Minikube.

