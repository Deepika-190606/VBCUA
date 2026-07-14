from modules.audio_features import get_speech_rate

def test_speech_rate():
    rate = get_speech_rate("This is a simple test sentence", 30)
    assert rate > 0