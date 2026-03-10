**Wisecow DevOps Project
Project Overview**

This project demonstrates the containerization and deployment of the Wisecow application using Docker and Kubernetes.

The application is packaged into a Docker container, deployed to a Kubernetes cluster, and exposed securely using NGINX Ingress with TLS support. A CI/CD pipeline using GitHub Actions automatically builds and pushes the Docker image whenever changes are pushed to the repository.

**Technologies Used**

Docker – Containerization of the application

Kubernetes – Container orchestration

NGINX Ingress Controller – External access to the application

GitHub Actions – CI/CD pipeline

GitHub Container Registry (GHCR) – Container image storage

Linux – Base environment

Architecture
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
Docker Container (Wisecow App)

**Project Structure**
wisecow-DevOps-project
│
├── Dockerfile
├── wisecow.sh
├── README.md
│
├── k8s
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── ingress.yaml
│   └── tls.yaml
│
└── .github
    └── workflows
        └── cicd.yaml
Docker Image

The Docker image is automatically built and pushed to:

ghcr.io/sambireddy93/wisecow:latest
CI/CD Pipeline

**A GitHub Actions workflow automatically:**

Checks out the repository

Builds the Docker image

Pushes the image to GitHub Container Registry (GHCR)

Pipeline location:

.github/workflows/cicd.yaml

**Pipeline flow:**

Git Push
   │
   ▼
GitHub Actions
   │
   ▼
Build Docker Image
   │
   ▼
Push Image to GHCR
Kubernetes Deployment
Deploy the Application
kubectl apply -f deployment.yaml
Create the Service
kubectl apply -f service.yaml
Configure Ingress
kubectl apply -f ingress.yaml
TLS Configuration

**TLS communication is enabled using Kubernetes Ingress.**

Files used:

ingress.yaml
tls.yaml

Ingress uses a TLS secret to provide HTTPS access to the Wisecow application.

Verify Deployment
kubectl get pods
kubectl get svc
kubectl get ingress
Access the Application
https://<ingress-host>

**Learning outcomes**

Through this project the following DevOps skills were practiced:

Docker containerization

Kubernetes deployments

Kubernetes services

NGINX ingress configuration

GitHub Actions CI/CD pipeline

Secure communication using TLS

**Author**
Sambireddy
