import streamlit as st
from modules.speech_to_text import transcribe_audio
# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="VBCUA",
    page_icon="🎤",
    layout="wide"
)

# ---------------- TITLE ---------------- #
st.title("🎤 Voice-Based Concept Understanding Analyser")

st.write(
    "Evaluate conceptual understanding using AI-powered speech and semantic analysis."
)

st.divider()

# ---------------- STUDENT DETAILS ---------------- #
student_name = st.text_input(
    "👤 Student Name",
    placeholder="Enter your name"
)

# ---------------- TOPIC ---------------- #
topic = st.selectbox(
    "Select Concept",
    (
        "Machine Learning",
        "Cloud Computing",
        "Artificial Intelligence",
        "Data Science"
    )
)

# ---------------- AUDIO ---------------- #
audio_file = st.file_uploader(
    "Upload Audio",
    type=["wav", "mp3", "m4a"]
)

# Show audio player
if audio_file is not None:
    st.success("Audio uploaded successfully!")
    st.audio(audio_file)

st.divider()

# ---------------- BUTTON ---------------- #
analyze = st.button("🔍 Analyze Explanation")
if analyze:

    if audio_file is None:
        st.error("Please upload an audio file.")

    else:
        with open("uploads/audio.wav", "wb") as f:
            f.write(audio_file.getbuffer())

        st.info("Transcribing audio...")

        text = transcribe_audio("uploads/audio.wav")

        st.success("Transcription Completed!")

        st.subheader("Transcribed Text")

        st.write(text)