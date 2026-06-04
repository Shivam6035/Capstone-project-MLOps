# 🎬 Movie Review Sentiment Analysis – Production-Grade MLOps Pipeline

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10-blue)
![AWS](https://img.shields.io/badge/AWS-Cloud-orange)
![MLflow](https://img.shields.io/badge/MLflow-Experiment%20Tracking-blue)
![DVC](https://img.shields.io/badge/DVC-Data%20Versioning-green)
![Docker](https://img.shields.io/badge/Docker-Containerization-blue)
![Kubernetes](https://img.shields.io/badge/Kubernetes-EKS-326CE5)
![GitHub Actions](https://img.shields.io/badge/CI%2FCD-Automated-success)

### From Notebook Experimentation to Production Deployment

An industry-grade, end-to-end Machine Learning Operations (MLOps) project that bridges the gap between a Jupyter Notebook experiment and a scalable, production-ready Kubernetes deployment.

This project performs sentiment analysis on movie reviews. However, the primary focus is on the engineering architecture: implementing robust data versioning, comprehensive experiment tracking, automated CI/CD pipelines, and highly available cloud deployment.
</div>

---

# 🚀 Key Engineering Highlights

* Data as Code: Integrated DVC (Data Version Control) linked to AWS S3 to ensure full data reproducibility. If the model degrades, we know exactly what dataset version it was trained on.

* Eliminated Guesswork: Utilized MLflow (hosted on DagsHub) for tracking hyperparameter tuning, comparing runs, and managing the model registry.

* Automated Pipelines: Configured a reproducible pipeline using dvc.yaml (Ingestion ➡️ Preprocessing ➡️ Feature Engineering ➡️ Training ➡️ Evaluation).

* Robust CI/CD: Built automated testing and deployment workflows using GitHub Actions.

* Scalable Production: Containerized the Flask application with Docker, pushed to AWS ECR, and deployed via standard manifests to an AWS EKS (Kubernetes) cluster.

# 📌 Project Overview

Most Machine Learning projects stop after training a model in a Jupyter notebook.

However, real-world ML systems require:

* Reproducibility
* Data Lineage
* Experiment Tracking
* Automated Pipelines
* Cloud Deployment
* Monitoring & Logging

This project addresses these challenges by building a complete production-ready MLOps workflow around a Movie Review Sentiment Analysis model.

---

# 🚀 Key Features

### Machine Learning

* Movie Review Sentiment Classification
* TF-IDF Feature Engineering
* Bag of Words Representation
* Multiple Model Comparison
* Automated Model Selection

### MLOps

* MLflow Experiment Tracking
* DVC Data Versioning
* DVC Pipeline Automation
* Model Registry
* Structured Logging
* Reproducible Training Pipeline

### Cloud & DevOps

* AWS S3 Data Storage
* Docker Containerization
* GitHub Actions CI/CD
* Amazon ECR
* Amazon EKS (Kubernetes)
* Automated Deployment Pipeline

---

# 🏗️ System Architecture

```text
                    ┌─────────────────┐
                    │   AWS S3 Data   │
                    └────────┬────────┘
                             │
                             ▼
                ┌────────────────────────┐
                │   Data Ingestion       │
                └────────┬───────────────┘
                         │
                         ▼
                ┌────────────────────────┐
                │ Data Preprocessing     │
                └────────┬───────────────┘
                         │
                         ▼
                ┌────────────────────────┐
                │ Feature Engineering    │
                │ TF-IDF / BoW           │
                └────────┬───────────────┘
                         │
                         ▼
                ┌────────────────────────┐
                │ Model Training         │
                └────────┬───────────────┘
                         │
                         ▼
                ┌────────────────────────┐
                │ Model Evaluation       │
                └────────┬───────────────┘
                         │
                         ▼
                ┌────────────────────────┐
                │ Model Registry         │
                │ MLflow + DagsHub       │
                └────────┬───────────────┘
                         │
                         ▼
                ┌────────────────────────┐
                │ Docker Container       │
                └────────┬───────────────┘
                         │
                         ▼
                ┌────────────────────────┐
                │ Amazon EKS             │
                │ Kubernetes Deployment  │
                └────────────────────────┘
```

---

# 🔄 End-to-End MLOps Workflow

```text
Data → DVC → Training → MLflow → Docker → ECR → EKS → Production
```

### Step 1: Data Versioning

DVC tracks datasets independently from Git.

Benefits:

* Dataset reproducibility
* Dataset lineage
* Version rollback
* Cloud-backed storage using AWS S3

---

### Step 2: Experiment Tracking

MLflow records:

* Parameters
* Metrics
* Artifacts
* Models
* Training Runs

This enables systematic comparison of multiple algorithms and hyperparameters.

---

### Step 3: Automated Pipelines

The entire workflow is orchestrated using DVC pipelines.

```bash
dvc repro
```

Single command execution:

* Data Ingestion
* Preprocessing
* Feature Engineering
* Model Training
* Evaluation

---

### Step 4: CI/CD Automation

GitHub Actions automatically:

* Run Tests
* Validate Code
* Build Docker Images
* Push Images to ECR
* Deploy to Kubernetes

---

# 📊 Experiment Tracking with MLflow

The project evaluates multiple machine learning models and compares them through MLflow.

Metrics Tracked:

* Accuracy
* Precision
* Recall
* F1 Score

Benefits:

* Faster model selection
* Experiment reproducibility
* Centralized tracking
* Better collaboration

# 📊 Experiment Tracking & Model Performance

The project leverages **MLflow** integrated with **DagsHub** to track experiments, compare models, and manage model artifacts.

## Model Comparison

| Model | Accuracy | F1 Score |
|---------|---------|---------|
| XGBoost | **85.0%** | **85.98%** |
| Random Forest | 82.0% | 82.0% |
| Gradient Boosting | 80.0% | 80.0% |
| Logistic Regression | 79.0% | 79.0% |
| Multinomial Naive Bayes | 78.0% | 78.0% |

### Best Performing Model

🏆 **XGBoost**

- Accuracy: **85.0%**
- F1 Score: **85.98%**
- Selected as the production model
- Registered through the MLflow Model Registry

## Experiment Tracking Workflow

Each experiment run tracks:

- Algorithm
- Hyperparameters
- Accuracy
- F1 Score
- Model Artifacts
- Training Metadata

This enables reproducibility and data-driven model selection.

### MLflow Experiment Visualization
<img width="2540" height="1390" alt="image" src="https://github.com/user-attachments/assets/23ef2a55-a1ad-45a0-98fc-cb3da2708782" />



The Parallel Coordinates Plot provides a visual comparison of model parameters and evaluation metrics across multiple runs, helping identify the best-performing configuration.
---

# 📂 Project Structure

```text
Movie-Review-MLOps/
│
├── data/
├── models/
├── notebooks/
├── src/
│   ├── logger/
│   ├── data_ingestion.py
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── model_building.py
│   ├── model_evaluation.py
│   └── register_model.py
│
├── flask_app/
│
├── tests/
├── scripts/
│
├── dvc.yaml
├── params.yaml
├── requirements.txt
├── Dockerfile
└── .github/workflows/
```

---

# 📝 Logging & Observability

A centralized logging system captures:

* Pipeline execution details
* Training events
* Errors & exceptions
* Runtime information

Benefits:

* Easier debugging
* Better traceability
* Faster issue resolution

---

# ☁️ AWS Infrastructure

### Services Used

| Service        | Purpose                     |
| -------------- | --------------------------- |
| AWS S3         | Dataset Storage             |
| ECR            | Docker Registry             |
| EKS            | Kubernetes Deployment       |
| IAM            | Secure Access Management    |
| CloudFormation | Infrastructure Provisioning |

---

# 🐳 Containerization

Application packaged using Docker.

```bash
docker build -t sentiment-app .
docker run -p 5000:5000 sentiment-app
```

Benefits:

* Environment consistency
* Portability
* Faster deployments

---

# ☸️ Kubernetes Deployment

Amazon EKS provides:

* High Availability
* Scalability
* Self-Healing Infrastructure
* Production-grade Deployment

---

# 📈 Why This Project Matters

Traditional ML Projects:

❌ Notebook-centric

❌ Difficult to reproduce

❌ No experiment history

❌ No deployment strategy

❌ Limited scalability

This Project:

✅ Reproducible

✅ Version Controlled

✅ Experiment Tracked

✅ Automated CI/CD

✅ Containerized

✅ Cloud Native

✅ Kubernetes Deployed

---

# 🛠️ Technology Stack

### Machine Learning

* Python
* Scikit-Learn
* Pandas
* NumPy
* NLP
* TF-IDF

### MLOps

* MLflow
* DVC
* DagsHub

### DevOps & Cloud

* Docker
* GitHub Actions
* AWS S3
* Amazon ECR
* Amazon EKS
* Kubernetes

---

# 🎯 Future Improvements

* Model Monitoring
* Data Drift Detection
* Prometheus Metrics
* Grafana Dashboards
* Blue-Green Deployments
* Canary Releases

---

# 👨‍💻

If you found this project interesting, feel free to connect and collaborate.
