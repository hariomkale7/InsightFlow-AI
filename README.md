# 🚀 InsightFlow AI

An AI-Powered Automated Data Analyst and Insight Engine that transforms raw CSV datasets into clean, structured insights, visualizations, and reports.

## 📌 Project Overview

InsightFlow AI automates the complete data analysis workflow:

```text
CSV Dataset
    ↓
Data Cleaning
    ↓
Exploratory Data Analysis (EDA)
    ↓
AI Insight Generation
    ↓
Data Visualization
    ↓
Analysis Report
```

The goal is to reduce manual data analysis effort and provide instant insights from uploaded datasets.

---

## ✨ Features

### 1. Data Cleaning Engine

* Column name standardization
* Duplicate removal
* Missing value handling
* Data type conversion
* Outlier detection using IQR

### 2. EDA Engine

* Dataset Summary
* Numerical Summary
* Categorical Summary

### 3. AI Insights Engine

* Dataset-level insights
* Outlier analysis
* Distribution analysis
* Categorical pattern analysis
* Automatic insight generation

### 4. Visualization Engine

* Dynamic bar chart generation
* Automatic chart generation for categorical columns
* Box plot generation for numeric columns
* PNG chart export
* Dataset-independent visualization creation

### 5. FastAPI Backend

* CSV upload endpoint
* Swagger UI integration
* JSON response generation
* Static file serving
* Frontend-ready API architecture

---

## 🏗️ Project Architecture

```text
InsightFlow-AI/
│
├── main.py
│
├── src/
│   ├── cleaner.py
│   ├── eda.py
│   ├── visualizer.py
│   ├── reporting.py
│   └── pipeline.py
│
├── charts/
├── uploads/
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* FastAPI
* Uvicorn

---

## 🔥 Current API Output

The `/analyze` endpoint returns:

* Cleaned Dataset
* Cleaning Report
* Outlier Report
* Dataset Summary
* Numerical Summary
* Categorical Summary
* AI Insights
* Generated Chart Paths

---

## 🧠 Engineering Decisions

### Modular Architecture

Instead of a monolithic script, the project is divided into reusable modules:

* cleaner.py
* eda.py
* visualizer.py
* reporting.py
* pipeline.py

This improves:

* Maintainability
* Scalability
* Testing
* Code readability

### Summary-Based AI Design

Future LLM integration will use dataset summaries instead of sending entire datasets to the model.

Benefits:

* Lower token usage
* Faster responses
* Better scalability
* Reduced API costs

---

## 📚 Learning Outcomes

Through this project I have learned:

* Data Cleaning Techniques
* Exploratory Data Analysis
* Data Visualization
* FastAPI Development
* REST APIs
* File Upload Handling
* JSON Serialization
* Modular Software Architecture
* Backend Development
* Frontend-Backend Communication

---

## 🛣️ Future Roadmap

### Phase 1

* LLM Integration
* AI-powered Dataset Q&A
* Executive Summary Generation

### Phase 2

* Dataset Chat Interface
* Context-Aware Analysis

### Phase 3

* Agentic AI Workflow
* Automatic Report Generation
* Business Recommendation Engine

### Phase 4

* Database Integration
* Analysis History
* User Management

### Phase 5

* React Dashboard
* Interactive Visualizations
* Cloud Deployment

---

## 👨‍💻 Author

Hariom Kale

B.Tech CSE | Python Developer | AI Automation Enthusiast

Building projects publicly and learning by creating real-world systems.
