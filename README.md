# Voice Based Concept Understanding Analyser (VBCUA)

## Overview
Voice Based Concept Understanding Analyser (VBCUA) is a Streamlit application that evaluates a student's understanding of a concept from their spoken explanation.

## Features
- Speech-to-Text using OpenAI Whisper
- Semantic Similarity Analysis
- Fluency Score
- Speech Rate Detection
- Filler Word Detection
- AI Feedback
- Performance Dashboard
- Audio Waveform Visualization

## Technologies Used
- Python
- Streamlit
- OpenAI Whisper
- Sentence Transformers
- Librosa
- Plotly
- Pandas
- Matplotlib

## Project Structure

```
VBCUA/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── modules/
    ├── speech_to_text.py
    ├── semantic_similarity.py
    └── audio_features.py
```

## Run

```bash
pip install -r requirements.txt
streamlit run app.py
```
