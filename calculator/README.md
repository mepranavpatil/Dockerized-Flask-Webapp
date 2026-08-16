# Dockerized Flask WebApp

A containerized Python Flask web application that exposes REST API endpoints for health monitoring, version tracking, and basic calculator operations. The application is packaged using Docker, allowing it to run consistently across different environments.

This project was built to gain hands-on experience with:

- Python Flask development
- REST API creation
- Docker image creation
- Container lifecycle management
- Docker Hub image publishing
- Application containerization best practices

---

# Project Architecture

```text
Browser
   │
   ▼
Port 5000
   │
   ▼
Docker Container
   │
   ▼
Flask Application
   │
   ├── Home Endpoint
   ├── Health Endpoint
   ├── Version Endpoint
   ├── Addition API
   ├── Subtraction API
   ├── Multiplication API
   └── Division API
```

---

# Project Objectives

The primary objectives of this project are:

- Build a Python web application using Flask
- Learn API development fundamentals
- Containerize an application using Docker
- Understand Docker Images and Containers
- Publish Docker images to Docker Hub
- Practice container management commands
- Prepare for real-world application deployment

---

# Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Application Development |
| Flask | Web Framework |
| Docker | Containerization |
| Docker Hub | Image Registry |
| Git | Version Control |
| GitHub | Source Code Hosting |

---

# Features

### Web Application

- Landing Page
- Health Check Endpoint
- Version Endpoint

### Calculator APIs

- Addition
- Subtraction
- Multiplication
- Division
- Division-by-zero validation

### Docker Features

- Docker Image Creation
- Container Deployment
- Port Mapping
- Image Versioning
- Docker Hub Integration

---

# Project Structure

```text
dockerized-flask-webapp/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── README.md
│
└── screenshots/
    ├── homepage.png
    ├── health-endpoint.png
    ├── docker-build.png
    ├── docker-ps.png
    └── dockerhub-repository.png
```

---

# Application Endpoints

## Home Page

### Request

```http
GET /
```

### Response

```html
Dockerized Flask WebApp
Cloud Engineer Calculator API
```

---

## Health Check

Health endpoints are commonly used in production environments to verify whether an application is running properly.

### Request

```http
GET /health
```

### Response

```json
{
  "status": "healthy"
}
```

---

## Version Endpoint

Displays the current application version.

### Request

```http
GET /version
```

### Response

```json
{
  "version": "1.0"
}
```

---

## Addition

### Request

```http
GET /add/10/5
```

### Response

```json
{
  "operation": "addition",
  "result": 15
}
```

---

## Subtraction

### Request

```http
GET /subtract/10/5
```

### Response

```json
{
  "operation": "subtraction",
  "result": 5
}
```

---

## Multiplication

### Request

```http
GET /multiply/10/5
```

### Response

```json
{
  "operation": "multiplication",
  "result": 50
}
```

---

## Division

### Request

```http
GET /divide/10/5
```

### Response

```json
{
  "operation": "division",
  "result": 2
}
```

---

## Division by Zero Handling

### Request

```http
GET /divide/10/0
```

### Response

```json
{
  "error": "division by zero not allowed"
}
```

---

# Local Setup

## Clone Repository

```bash
git clone https://github.com/<your-username>/dockerized-flask-webapp.git

cd dockerized-flask-webapp
```

---

## Create Virtual Environment

```bash
python3 -m venv venv
```

Activate:

### Linux/macOS

```bash
source venv/bin/activate
```

### Windows

```powershell
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
python app.py
```

Application will be available at:

```text
http://localhost:5000
```

---

# Docker Overview

Docker packages the application, dependencies, and runtime environment into a single portable image.

Benefits include:

- Consistent deployments
- Environment portability
- Faster application delivery
- Simplified dependency management

---

# Dockerfile Explanation

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

### FROM

Uses an official lightweight Python base image.

### WORKDIR

Creates and sets `/app` as the working directory inside the container.

### COPY

Copies application files into the container.

### RUN

Installs required Python dependencies.

### EXPOSE

Documents that the application listens on port 5000.

### CMD

Starts the Flask application when the container launches.

---

# Build Docker Image

Create a Docker image from the Dockerfile.

```bash
docker build -t flask-webapp:v1 .
```

Verify:

```bash
docker images
```

Expected:

```text
REPOSITORY     TAG
flask-webapp   v1
```

---

# Run Docker Container

```bash
docker run -d -p 5000:5000 flask-webapp:v1
```

Explanation:

| Option | Description |
|----------|------------|
| -d | Detached Mode |
| -p | Port Mapping |
| 5000:5000 | Host Port → Container Port |

Verify:

```bash
docker ps
```

---

# Docker Commands Used

## View Running Containers

```bash
docker ps
```

---

## View Container Logs

```bash
docker logs <container-id>
```

---

## Enter Container Shell

```bash
docker exec -it <container-id> bash
```

---

## Stop Container

```bash
docker stop <container-id>
```

---

## Remove Container

```bash
docker rm <container-id>
```

---

## Remove Image

```bash
docker rmi flask-webapp:v1
```

---

# Docker Hub Integration

Docker Hub is a cloud-based container registry used to store and distribute Docker images.

---

## Login

```bash
docker login
```

---

## Tag Image

```bash
docker tag flask-webapp:v1 <dockerhub-username>/dockerized-flask-webapp:v1
```

---

## Push Image

```bash
docker push <dockerhub-username>/dockerized-flask-webapp:v1
```

---

## Pull Image

```bash
docker pull <dockerhub-username>/dockerized-flask-webapp:v1
```

---

## Run Pulled Image

```bash
docker run -d -p 5000:5000 <dockerhub-username>/dockerized-flask-webapp:v1
```

---

# Image Versioning

Versioning helps manage application releases.

Example:

```text
v1
v2
v3
latest
```

Benefits:

- Rollback capability
- Release management
- Safer deployments

---

# Screenshots

Add screenshots of:

### Home Page

```text
http://localhost:5000
```

### Health Endpoint

```text
http://localhost:5000/health
```

### Docker Build Output

```bash
docker build -t flask-webapp:v1 .
```

### Running Container

```bash
docker ps
```

### Docker Hub Repository

Repository page showing image tags.

---

# Learning Outcomes

Through this project, I gained hands-on experience with:

- Python Flask Development
- REST API Design
- Docker Image Creation
- Docker Container Management
- Docker Networking
- Docker Hub Registry
- Application Versioning
- Containerized Application Deployment
- Git and GitHub Workflows

---

# Future Improvements

Planned enhancements include:

- Deploy on AWS EC2
- Add Nginx Reverse Proxy
- Use Docker Compose
- Add CI/CD with GitHub Actions
- Deploy on Kubernetes
- Add Monitoring and Logging
- Add Unit Testing
- Add Authentication

---

# Author

**Pranav Patil**

Aspiring Cloud & DevOps Engineer

GitHub: https://github.com/mepranavpatil