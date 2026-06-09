# 🚀 InsightFlow AI

An AI-Powered Automated Data Analyst and Conversational Insight Engine that transforms raw CSV datasets into clean data, visualizations, AI-generated reports, and context-aware analytical conversations.

---

## 📌 Project Overview

InsightFlow AI automates the complete data analysis workflow while allowing users to interact with their datasets using natural language.

### Workflow

CSV Dataset

→ Data Cleaning

→ Exploratory Data Analysis (EDA)

→ AI Insight Generation

→ Visualization Generation

→ Report Generation

→ Dataset Chat

→ Context-Aware AI Responses

---

## ✨ Features

### 🧹 Data Cleaning Engine

* Column name standardization
* Duplicate removal
* Missing value handling
* Data type conversion
* Outlier detection using IQR

### 📊 EDA Engine

* Dataset Summary
* Numerical Summary
* Categorical Summary

### 🧠 AI Insights Engine

* Dataset-level insights
* Outlier analysis
* Distribution analysis
* Categorical pattern analysis
* Automated insight generation

### 📈 Visualization Engine

* Dynamic bar chart generation
* Automatic chart generation for categorical columns
* Box plot generation for numerical columns
* PNG chart export
* Dataset-independent visualization creation

### ⚡ FastAPI Backend

* CSV upload endpoint
* Swagger UI integration
* JSON response generation
* Static file serving
* Frontend-ready architecture

### 🤖 Gemini AI Integration

* AI-powered report generation
* Natural language analysis summaries
* Business-friendly insights

### 💬 Dataset Question Answering

Users can ask questions directly about uploaded datasets.

Examples:

* What are the top-selling products?
* Which city generated the highest revenue?
* What trends are visible in the dataset?

### 🧠 Conversational Memory

* Remembers previous questions
* Context-aware follow-up responses
* Multi-turn analytical conversations

### 📜 Chat History API

* Conversation storage
* Historical chat retrieval
* Foundation for future chat interfaces

---

## 🏗️ Project Architecture

InsightFlow-AI/

├── main.py

├── src/

│ ├── cleaner.py

│ ├── eda.py

│ ├── visualizer.py

│ ├── reporting.py

│ ├── pipeline.py

│ ├── ai_report_generator.py

│ ├── chat_engine.py

│ └── memory_manager.py

├── charts/

├── uploads/

├── reports/

├── chat_history/

├── requirements.txt

├── README.md

└── .gitignore

---

## ⚙️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* FastAPI
* Uvicorn
* Gemini API
* JSON Storage

---

## 🔥 Current API Capabilities

The `/analyze` endpoint provides:

* Cleaned Dataset
* Cleaning Report
* Outlier Report
* Dataset Summary
* Numerical Summary
* Categorical Summary
* AI Insights
* Generated Charts
* AI Report Generation

Additional APIs:

* Dataset Chat API
* Chat History API
* Report Retrieval API

---

## 🧠 Key Engineering Decisions

### Modular Architecture

The project follows a modular design pattern:

* cleaner.py
* eda.py
* visualizer.py
* reporting.py
* pipeline.py
* chat_engine.py
* memory_manager.py

Benefits:

* Maintainability
* Scalability
* Easier Testing
* Reusability

### Summary-Based LLM Architecture

Instead of sending entire datasets to Gemini:

Dataset

→ EDA Summary

→ AI Prompt

→ Response

Benefits:

* Lower token consumption
* Faster responses
* Better scalability
* Reduced API costs

### Conversational Analytics Design

Conversation history is stored and reused to provide context-aware responses.

This allows InsightFlow AI to behave like an AI Data Analyst instead of a traditional analytics dashboard.

---

## 📚 Learning Outcomes

Through this project I learned:

* Data Cleaning
* Exploratory Data Analysis
* Data Visualization
* FastAPI Development
* REST APIs
* File Upload Handling
* JSON Serialization
* Static File Serving
* Gemini API Integration
* Prompt Engineering
* Conversational Memory Systems
* Backend Development
* Software Architecture
* Frontend-Backend Communication

---

## 🛣️ Future Roadmap

### Phase 1

* React Frontend
* Interactive Dashboard
* Professional Report Viewer

### Phase 2

* Advanced Dataset Chat Interface
* Context-Aware Analytics

### Phase 3

* Agentic AI Workflow
* Automatic Report Generation
* Business Recommendation Engine

### Phase 4

* Database Integration
* Analysis History
* User Authentication

### Phase 5

* Cloud Deployment
* Multi-User Support
* Enterprise Reporting Features

---

## 👨‍💻 Author

Hariom Kale

B.Tech CSE | Python Developer | AI Automation Enthusiast

Building real-world AI systems publicly and learning software engineering through practical projects.
