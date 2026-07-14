import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import librosa
import librosa.display
import plotly.express as px
import os
from modules.speech_to_text import transcribe_audio
from modules.semantic_similarity import compare_text, understanding_level
from modules.audio_features import get_audio_duration, get_speech_rate, count_filler_words
from modules.database import create_database, save_result, get_history
from modules.pdf_generator import generate_pdf

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="VBCUA",
    page_icon="🎤",
    layout="wide"
)

# Create database automatically
create_database()

# ---------------- STYLING ---------------- #
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .block-container {
        padding-top: 2rem;
    }
    h1 {
        text-align: center;
        color: #4CAF50;
    }
    .subtitle {
        text-align: center;
        color: gray;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #
st.markdown("#  Voice Based Concept Understanding Analyser ")
st.markdown("<p class='subtitle'>Speech + Understanding + Fluency Evaluation Engine</p>", unsafe_allow_html=True)

st.divider()

# ---------------- REFERENCE ---------------- #
reference_concepts = {
    "Machine Learning": "Machine Learning is a branch of Artificial Intelligence that enables computers to learn from data without being explicitly programmed.",
    "Cloud Computing": "Cloud Computing is the delivery of computing services like storage, servers, and software over the internet.",
    "Artificial Intelligence": "Artificial Intelligence is the simulation of human intelligence in machines that can learn, reason, and solve problems.",
    "Data Science": "Data Science is the field of extracting meaningful insights and knowledge from structured and unstructured data."
}

# ---------------- INPUT SECTION ---------------- #
col1, col2 = st.columns(2)

with col1:
    student_name = st.text_input("Student Name")

with col2:
    topic = st.selectbox("Select Concept", list(reference_concepts.keys()))

audio_file = st.file_uploader("Upload Audio", type=["wav", "mp3", "m4a"])

if audio_file:
    st.audio(audio_file)

st.divider()

# ---------------- ANALYZE ---------------- #
analyze = st.button("Analyze Explanation")

if analyze:

    if not audio_file:
        st.error("Please upload an audio file.")
    else:
        os.makedirs("uploads", exist_ok=True)

        with open("uploads/audio.wav", "wb") as f:
            f.write(audio_file.getbuffer())

        with st.spinner("Analyzing audio... Please wait..."):
            # ---------------- TRANSCRIPTION ---------------- #
            text = transcribe_audio("uploads/audio.wav")

            st.success("Transcription Completed")

            # ---------------- SEMANTIC ANALYSIS ---------------- #
            reference_text = reference_concepts[topic]
            score = compare_text(reference_text, text)
            level = understanding_level(score)

            # ---------------- AUDIO FEATURES ---------------- #
            duration = get_audio_duration("uploads/audio.wav")
            wpm = get_speech_rate(text, duration)
            fillers = count_filler_words(text)

            fluency_score = 100 - (fillers * 5)

            if wpm < 90:
                fluency_score -= 10
            elif wpm > 170:
                fluency_score -= 10

            fluency_score = max(0, min(100, fluency_score))

        # ---------------- RESULTS UI ---------------- #
        st.divider()
        st.markdown("## Results Dashboard")
        
        st.write(f"### Student: **{student_name}**")
        st.write(f"### Concept: **{topic}**")
        
        st.markdown("---")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Understanding Score", f"{score*100:.1f}%")
            st.progress(int(score * 100))
            st.success(level)

        with col2:
            st.metric("Fluency Score", f"{fluency_score}/100")
            st.progress(fluency_score)
            st.write(f"**Filler Words:** {fillers}")
        
        with col3:
            st.metric("Speech Rate", f"{wpm:.1f} WPM")
            st.write(f"**Duration:** {duration:.2f} sec")
            
        st.markdown("---")
        st.subheader("Transcript")
        st.write(text)

        st.divider()
        
        st.subheader("Overall Performance")
        
        overall_score = ((score * 100) + fluency_score) / 2

        if overall_score >= 90: 
            st.success(f"Excellent Performance ({overall_score:.1f}%)")
        elif overall_score >= 75:
            st.info(f"Good Performance ({overall_score:.1f}%)")
        elif overall_score >= 60:
            st.warning(f"Moderate Performance ({overall_score:.1f}%)")
        else:
            st.error(f"Needs Improvement ({overall_score:.1f}%)")
        
                # ---------------- SAVE TO DATABASE ---------------- #
        save_result(
            student_name,
            topic,
            text,
            score * 100,
            fluency_score,
            wpm,
            duration,
            fillers,
            overall_score
        )
        
        st.divider()
        
        st.subheader("AI Feedback")
        
        feedback = []
        if score >= 0.90:
            feedback.append("Excellent conceptual understanding.")
        elif score >= 0.75:
            feedback.append("Good explanation, but some concepts can be expanded.")
        else:
            feedback.append("Your explanation needs more conceptual details.")
        
        if fillers == 0:
            feedback.append("No filler words detected.")
        elif fillers < 3:
            feedback.append("Very few filler words detected.")
        else:
            feedback.append("Too many filler words detected.")
        
        if wpm < 100:
            feedback.append("Try speaking slightly faster.")
        elif wpm > 170:
            feedback.append("Try slowing down slightly.")
        else:
            feedback.append("Your speaking speed is appropriate.")
            
        for line in feedback: 
            st.write("✅", line)
        
        pdf_file = generate_pdf(
            student_name,
            topic,
            text,
            score * 100,
            level,
            fluency_score,
            wpm,
            duration,
            fillers,
            overall_score,
            feedback
        )
        st.divider()

        st.subheader("Reference Concept")

        st.info(reference_text)

        st.divider()

        st.subheader("Evaluation Summary")

        summary = pd.DataFrame({
            "Metric": [
                "Student Name",
                "Concept",
                "Understanding Score",
                "Understanding Level",
                "Fluency Score",
                "Speech Rate",
                "Audio Duration",
                "Filler Words"
            ],
            "Value": [
                student_name,
                topic,
                f"{score*100:.2f}%",
                level,
                f"{fluency_score}/100",
                f"{wpm:.1f} WPM",
                f"{duration:.2f} sec",
                fillers
            ]
        })

        st.dataframe(summary, use_container_width=True)

        st.divider()

        st.subheader("Performance Chart")

        chart_data = pd.DataFrame({
            "Metric": [
                "Understanding",
                "Fluency"
            ],
            "Score": [
                score * 100,
                fluency_score
            ]
        })

        fig = px.bar(
            chart_data,
            x="Metric",
            y="Score",
            text="Score",
            color="Metric",
            title="Performance Comparison"
        )

        fig.update_traces(textposition="outside")

        fig.update_layout(
            yaxis_title="Score",
            xaxis_title="Metric",
            height=450
        )

        st.plotly_chart(fig, use_container_width=True)

        st.divider()

        st.subheader("Audio Waveform")

        audio, sr = librosa.load("uploads/audio.wav", sr=None)

        fig, ax = plt.subplots(figsize=(12,3))

        librosa.display.waveshow(audio, sr=sr)

        plt.title("Uploaded Audio Waveform")
        plt.xlabel("Time (seconds)")
        plt.ylabel("Amplitude")

        st.pyplot(fig)

        st.divider()
        st.subheader("Previous Evaluations")

        history = get_history()

        if history:
            history_df = pd.DataFrame(
                history,
                columns=[
                    "Student",
                    "Concept",
                    "Overall Score",
                    "Date"
                ]
            )

            st.dataframe(history_df, use_container_width=True)
        else:
            st.info("No previous evaluations found.")

        st.divider()

        with open(pdf_file, "rb") as pdf:
            st.download_button(
                label="Download PDF Report",
                data=pdf,
                file_name=f"{student_name}_Report.pdf",
                mime="application/pdf"
            )

        st.caption("© 2026 Voice Based Concept Understanding Analyser (VBCUA)")