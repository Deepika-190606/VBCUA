import librosa

# ---------------- DURATION ---------------- #
def get_audio_duration(audio_path):
    audio, sample_rate = librosa.load(audio_path, sr=None)
    duration = librosa.get_duration(y=audio, sr=sample_rate)
    return duration


# ---------------- SPEECH RATE ---------------- #
def get_speech_rate(text, duration):

    words = len(text.split())

    minutes = duration / 60

    if minutes == 0:
        return 0

    return words / minutes


# ---------------- FILLER WORDS ---------------- #
def count_filler_words(text):

    fillers = ["um", "uh", "like", "you know", "so", "actually"]

    text = text.lower()
    words = text.split()

    count = 0

    for word in words:
        if word in fillers:
            count += 1

    return count