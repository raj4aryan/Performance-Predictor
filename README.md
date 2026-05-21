# Student Performance Predictor

A full-stack Machine Learning web application that predicts a student's Math Score based on demographic and academic information. 

This project demonstrates how Machine Learning models can be integrated into a modern production-style architecture using React for the frontend, Node.js/Express for the backend API, and Python/FastAPI for the ML inference service.

## Project Architecture

```text
[ React Frontend ] 
        ↓
[ Node/Express Backend ]
        ↓
[ Python FastAPI ML Service ]
        ↓
[ Scikit-learn Model ]
```

## Features
Modern React frontend UI for intuitive user interaction.

REST API using Express.js to act as an API gateway.

Separate ML microservice built with FastAPI for scalable inference.

Scikit-learn prediction pipeline including data preprocessing and trained model integration.

Real-time prediction results served back to the client.

Modular production-style architecture separating concerns across the stack.

## Tech Stack
Frontend: React, Vite, Axios, CSS

Backend: Node.js, Express.js, CORS

ML Service: Python, FastAPI, Scikit-learn, Pandas, NumPy

## Project Structure
Plaintext
student-performance-app/
│
├── client/                 # React Frontend
│
├── server/                 # Express Backend
│
├── ml-service/             # Python ML Service
│   │
│   ├── artifacts/          # Serialized models and preprocessors
│   ├── notebook/           # Jupyter notebooks for EDA and training
│   ├── src/                # ML source code
│   │   ├── components/     # Data ingestion, transformation, model training
│   │   ├── pipeline/       # Prediction and training pipelines
│   │   ├── utils.py        # Utility functions
│   │   ├── logger.py       # Custom logging
│   │   └── exceptions.py   # Custom exception handling
│   │
│   ├── app.py              # FastAPI application entry point
│   └── requirements.txt    # Python dependencies
│
├── .gitignore
└── README.md

## System Overview
Machine Learning Pipeline
The ML workflow consists of a complete lifecycle:

Data Ingestion: Reading and splitting the dataset.

Data Transformation: Handling categorical encoding and numerical scaling.

Model Training: Evaluating multiple algorithms to find the best performer.

Model Serialization: Saving the model (model.pkl) and preprocessor (preprocessor.pkl).

Prediction Pipeline: Loading artifacts to transform new data and make predictions.

API Inference: Exposing the pipeline via FastAPI.

### Frontend
The frontend allows users to:

Select categorical student details (gender, ethnicity, parental education, lunch, test prep).

Enter numerical reading and writing scores.

Submit a prediction request.

View the predicted math score.

### Backend
The Express backend acts as:

An API gateway and request handler.

A communication bridge between the client-side frontend and the Python ML service.

### ML Service
The FastAPI ML service:

Loads the trained model and preprocessor.

Receives JSON input from the Express backend.

Converts the input into a Pandas DataFrame.

Applies preprocessing steps.

Generates and returns the prediction response.

Installation & Setup
1. Clone Repository
Bash
git clone <YOUR_GITHUB_REPO_URL>
cd student-performance-app
2. Setup Frontend
Open a terminal and run:

Bash
cd client
npm install
npm run dev
Note: Frontend runs on http://localhost:5173

3. Setup Backend
Open a second terminal:

Bash
cd server
npm install
npm run dev
Note: Backend runs on http://localhost:3500

4. Setup ML Service
Open a third terminal:

Bash
cd ml-service
Create and activate a virtual environment (Windows):

Bash
python -m venv venv
venv\Scripts\activate
Install dependencies:

Bash
pip install -r requirements.txt
Run the FastAPI server:

Bash
uvicorn app:app --reload
Note: ML service runs on http://127.0.0.1:8000

API Endpoint
Predict Student Performance
Endpoint: POST /predict

Description: Accepts student data and returns the predicted math score.

Request Body:

JSON
{
  "gender": "male",
  "race_ethnicity": "group B",
  "parental_level_of_education": "bachelor's degree",
  "lunch": "standard",
  "test_preparation_course": "completed",
  "reading_score": 72,
  "writing_score": 74
}
Response:

JSON
{
  "prediction": 76.42
}
Important Concepts Implemented
MVC-inspired architecture

ML Pipeline Engineering

API Integration and Backend-to-ML communication

React State Management & Component-based UI

Production-style Backend Design

Modular ML System Design (Service-based Architecture)

Future Improvements
User Authentication & Prediction History

Database Integration for storing logs and user data

Docker Deployment & Cloud Hosting (AWS/GCP/Azure)

CI/CD Pipeline integration

Model Monitoring & Data Drift Detection

Advanced UI/UX with Charts & Analytics Dashboard

Learning Outcomes
This project solidifies the understanding of:

Transitioning from Jupyter Notebook ML scripts to production-ready ML code.

Designing full-stack ML application architecture.

Serving ML models via REST APIs.

Establishing reliable communication between Node.js backends and Python microservices.

Implementing production engineering best practices.
