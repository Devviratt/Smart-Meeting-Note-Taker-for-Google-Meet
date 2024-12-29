from google.cloud import speech_v1 as speech

# Convert audio file to a compatible format (Mono, 16KHz)
def convert_audio_to_wav(input_file, output_file):
    from pydub import AudioSegment
    audio = AudioSegment.from_file(input_file)
    audio = audio.set_channels(1).set_frame_rate(16000)
    audio.export(output_file, format="wav")

# Transcribe the audio file using Google Speech-to-Text API
def transcribe_audio(audio_path):
    client = speech.SpeechClient()

    with open(audio_path, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US"
    )

    response = client.recognize(config=config, audio=audio)

    transcript = " ".join([result.alternatives[0].transcript for result in response.results])
    return transcript
