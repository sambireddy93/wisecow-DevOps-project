# Cow wisdom web server

## Prerequisites

```
sudo apt install fortune-mod cowsay -y
```

## How to use?

1. Run `./wisecow.sh`
2. Point the browser to server port (default 4499)

## What to expect?
![wisecow](https://github.com/nyrahul/wisecow/assets/9133227/8d6bfde3-4a5a-480e-8d55-3fef60300d98)

# Problem Statement
Deploy the wisecow application as a k8s app

## Requirement
1. Create Dockerfile for the image and corresponding k8s manifest to deploy in k8s env. The wisecow service should be exposed as k8s service.
2. Github action for creating new image when changes are made to this repo
3. [Challenge goal]: Enable secure TLS communication for the wisecow app.

## Expected Artifacts
1. Github repo containing the app with corresponding dockerfile, k8s manifest, any other artifacts needed.
2. Github repo with corresponding github action.
3. Github repo should be kept private and the access should be enabled for following github IDs: nyrahul


**Containerized Application Deployment using Docker & Kubernetes
Project Overview**

**Technologies Used**

Docker – Containerization of the application

Kubernetes – Container orchestration

NGINX Ingress Controller – Exposing the application to external users

AWS EC2 – Hosting the Kubernetes cluster

Linux – Server environment

Git & GitHub – Version control**

**Architecture**

User (Browser)
      │
      ▼
NGINX Ingress Controller
      │
      ▼
Kubernetes Service
      │
      ▼
Pod
      │
      ▼
Docker Container (Application)

**Architecture Explanation**
A user accesses the application through a web browser.

The request reaches the NGINX Ingress Controller.

The ingress forwards the request to the Kubernetes Service.

The service routes the request to the Pod.

The pod runs the Docker container containing the application.

**Project Structure**
 ├── Dockerfile
 ├── deployment.yaml
 ├── service.yaml
 ├── ingress.yaml
 ├── README.md
Setup and Deployment
1. Clone the Repository
git clone <your-repository-url>
cd <project-folder>
2. Build the Docker Image
docker build -t myapp .
3. Push Image to Docker Hub
docker tag myapp <dockerhub-username>/myapp
docker push <dockerhub-username>/myapp
4. Deploy Application to Kubernetes

**Apply the deployment configuration:**

kubectl apply -f deployment.yaml
5. Create Kubernetes Service
kubectl apply -f service.yaml
6. Configure NGINX Ingress
kubectl apply -f ingress.yaml
Verify Deployment

**Check the resources in the cluster:**

kubectl get pods
kubectl get svc
kubectl get ingress
Access the Application

Open your browser and use:

http://<EC2-Public-IP>
Learning Outcomes

**Through this project the following DevOps skills were practiced:**

Docker containerization

Kubernetes deployments

Kubernetes services

NGINX ingress configuration

Cloud deployment using AWS EC2

Infrastructure management using Linux

**Future Improvements**

Implement CI/CD using Jenkins or GitHub Actions

## TLS Configuration

**TLS is implemented using Kubernetes Ingress and a TLS secret.**

**Files used:**
- ingress.yaml
- tls.yaml

The ingress routes HTTPS traffic securely to the Wisecow service.


