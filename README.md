# 🎤 Voice-Based Concept Understanding Analyser (VBCUA)

## Project Overview

The Voice-Based Concept Understanding Analyser (VBCUA) is an AI-powered web application that evaluates a user's conceptual understanding through spoken explanations.

The system converts speech into text using OpenAI Whisper, compares the explanation with a reference concept using Sentence-BERT semantic similarity, analyzes speech fluency using Librosa, and generates an overall evaluation report.

It is designed for educational assessment, interview preparation, presentation practice, and spoken learning evaluation.

---

## Features

- Speech-to-Text using OpenAI Whisper
- Semantic Similarity using Sentence-BERT
- Concept Understanding Score
- Speech Fluency Analysis
- Speech Rate Calculation
- Filler Word Detection
- Audio Waveform Visualization
- Performance Charts
- AI Feedback Generation
- Evaluation Summary
- SQLite Database Storage
- PDF Report Generation
- Previous Evaluation History

---

## Technologies Used

### Frontend
- Streamlit

### Backend
- Python

### AI Models
- OpenAI Whisper
- Sentence-BERT

### Libraries
- Librosa
- Pandas
- NumPy
- Plotly
- Matplotlib
- ReportLab

### Database
- SQLite

### Testing
- Pytest

---

## 📂 Project Structure

```
VBCUA/
│
├── app.py
├── README.md
├── requirements.txt
├── pytest.ini
├── .gitignore
│
├── modules/
│   ├── speech_to_text.py
│   ├── semantic_similarity.py
│   ├── audio_features.py
│   ├── database.py
│   └── pdf_generator.py
│
├── database/
├── uploads/
├── reports/
└── tests/
```

---

## ⚙ Installation

Clone the repository

```bash
git clone https://github.com/Deepika-190606/VBCUA.git
```

Go inside the project

```bash
cd VBCUA
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶ Run the Application

```bash
streamlit run app.py
```

---

## Workflow

1. Upload audio
2. Speech transcription using Whisper
3. Semantic similarity calculation
4. Audio feature extraction
5. Fluency evaluation
6. Understanding analysis
7. Score generation
8. Database storage
9. PDF report generation

---

## Screenshots

Add screenshots here.

Example:

- Home Page
- Results Dashboard
- Waveform
- Performance Chart
- PDF Report

---

## Future Scope

- User Login System
- Cloud Database
- Multiple Language Support
- Real-time Voice Recording
- Emotion Detection
- Dashboard Analytics
- Teacher Portal
- Student Progress Tracking

---

## Author

Deepika Annapaneni
