import whisper

# Load the Whisper model once
model = whisper.load_model("base")

def transcribe_audio(audio_path):
    """
    Converts an audio file into text.

    Parameters:
        audio_path (str): Path of the audio file

    Returns:
        str: Transcribed text
    """

    result = model.transcribe(audio_path)

    return result["text"]