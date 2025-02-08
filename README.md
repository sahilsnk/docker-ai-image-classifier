# Docker AI Image Classifier

## Overview
This project is an AI-powered image classification web application built using **Flask** and **MobileNetV2**. It allows users to upload images, which are then classified into different categories using a pre-trained deep learning model. The application is containerized using **Docker** and deployed on **Render** with a CI/CD pipeline.

## Features
- Upload images via a simple web interface
- Classify images using **MobileNetV2** (pre-trained on ImageNet)
- Display classification results in a user-friendly UI
- Dockerized for easy deployment
- Integrated CI/CD pipeline for automated deployment

## Tech Stack
- **Backend:** Flask
- **Machine Learning Model:** MobileNetV2 (TensorFlow/Keras)
- **Frontend:** HTML, CSS
- **Containerization:** Docker
- **CI/CD:** GitHub Actions
- **Hosting:** Render

## Setup and Installation
### Prerequisites
Ensure you have the following installed:
- Python (3.8 or later)
- pip
- Docker
- Git

### Clone the Repository
```sh
 git clone https://github.com/your-username/docker-ai-image-classifier.git
 cd docker-ai-image-classifier
```

### Install Dependencies
```sh
pip install -r requirements.txt
```

### Run the Application
```sh
python app.py
```
The application will be accessible at `http://127.0.0.1:5000/`.

## Docker Instructions
### Build the Docker Image
```sh
docker build -t docker-ai-image-classifier .
```

### Run the Docker Container
```sh
docker run -d -p 5000:5000 --name image_classifier docker-ai-image-classifier
```

### Stop and Remove the Container
```sh
docker stop image_classifier
docker rm image_classifier
```

## CI/CD Pipeline
### GitHub Actions Workflow
This project includes a **GitHub Actions** workflow that automates testing, building, and deployment.

1. **On push to `main` branch:**
   - The workflow runs tests (if available).
   - Builds a Docker image and pushes it to **Docker Hub**.
   - Triggers deployment to **Render**.

2. **Secrets Required:**
   - `DOCKERHUB_USERNAME` and `DOCKERHUB_PASSWORD`
   - `RENDER_DEPLOY_HOOK`

### Deployment to Render
- Create a new **Web Service** on Render.
- Connect your GitHub repository.
- Set the **Build Command:** `docker build -t your-username/docker-ai-image-classifier .`
- Set the **Start Command:** `docker run -p 5000:5000 your-username/docker-ai-image-classifier`

## Usage
1. Open the web application.
2. Upload an image.
3. The model classifies the image and displays the top predictions.

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests.

## License
This project is licensed under the MIT License.

## Contact
For any questions, reach out via email: [sahilsnaik00@gmail.com]
