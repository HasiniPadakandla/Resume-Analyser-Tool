Resume Analyzer tool

📌 Project Overview

An AI-powered application that analyzes a resume against a job description and computes a resume–job match score using NLP and machine learning techniques. The project is cloud-deployed for easy access and demonstrates real-world AI engineering practices.

🚀 Features

Upload resume (PDF)

Paste job description

Clean and preprocess text data

Compute match score using TF-IDF + cosine similarity

Display match strength (Low / Moderate / Strong)

Public cloud deployment using Streamlit

🧠 How It Works

Resume PDF + Job Description
        ↓
Text Cleaning & Preprocessing
        ↓
TF-IDF Vectorization
        ↓
Cosine Similarity
        ↓
Match Score (%)

🛠️ Tech Stack

Python

NLP (text preprocessing)

Machine Learning (TF-IDF, cosine similarity)

Streamlit (UI & deployment)

pdfplumber (PDF parsing)

📁 Project Structure

resume-analyzer-ai/
├── backend/
│   ├── resume_parser.py
│   ├── jd_parser.py
│   └── skill_matcher.py
├── frontend/
│   └── app.py
├── requirements.txt
└── README.md

☁️ Deployment

Deployed on Streamlit Cloud

Cloud version focuses on resume–job match scoring

LLM-based feedback is implemented locally (not deployed due to resource constraints)

🎯 Skills Demonstrated

NLP

ML-based similarity scoring

Modular backend design

Streamlit UI development

Cloud deployment

Engineering trade-offs (local vs cloud AI)

🔮 Future Improvements

Semantic matching using embeddings

Cloud-based LLM feedback

Skill extraction using NLP models