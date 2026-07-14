# Voice-Based Concept Understanding Analyser (VBCUA)

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

## Project Structure

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

## Installation

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

## Run the Application

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

## Home Page
<img width="1469" height="873" alt="Screenshot 2026-07-14 at 6 50 08 PM" src="https://github.com/user-attachments/assets/da221c04-2964-454f-97e3-78ae511f042b" />

## Audio Upload
<img width="1469" height="873" alt="Screenshot 2026-07-14 at 6 50 32 PM" src="https://github.com/user-attachments/assets/2dac79b4-15cc-484a-9dd8-58209242a755" />

## Analysis Process
<img width="1469" height="873" alt="Screenshot 2026-07-14 at 6 50 39 PM" src="https://github.com/user-attachments/assets/372dd5d7-b86b-464a-81b0-1148737421a8" />

## Results Dashboard

<img width="1469" height="873" alt="Screenshot 2026-07-14 at 6 50 50 PM" src="https://github.com/user-attachments/assets/1f8f0e4f-5e53-44eb-b0ad-288e803f6f03" />

## Overall Performance & AI feedback
<img width="1469" height="873" alt="Screenshot 2026-07-14 at 6 51 04 PM" src="https://github.com/user-attachments/assets/181a023d-db97-4d64-8897-53127e77cd48" />

## Evaluation Summary

<img width="1469" height="640" alt="Screenshot 2026-07-14 at 6 51 15 PM" src="https://github.com/user-attachments/assets/5f4caac8-e1cf-4f9e-83eb-e663b22834d8" />

## Performance Chart
<img width="1469" height="705" alt="Screenshot 2026-07-14 at 6 51 25 PM" src="https://github.com/user-attachments/assets/2b64d947-57a2-4ac4-b476-b37c7db6f372" />

## Audio Waveform
<img width="1469" height="873" alt="Screenshot 2026-07-14 at 6 51 36 PM" src="https://github.com/user-attachments/assets/4db1edf7-b1ed-46f0-9fb0-9a0ecf475d48" />

## Previous Evaluations
<img width="1469" height="873" alt="Screenshot 2026-07-14 at 6 51 42 PM" src="https://github.com/user-attachments/assets/6265140e-30a1-4eb7-bc0d-b8764eb807f4" />

## Generate PDF Report
<img width="947" height="904" alt="Screenshot 2026-07-14 at 6 52 17 PM" src="https://github.com/user-attachments/assets/01dd64f3-5d38-447d-92d4-37bbf96fdfba" />

---

## Live Demo

Try the deployed app:
https://vbcuanalyser.streamlit.app/

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
