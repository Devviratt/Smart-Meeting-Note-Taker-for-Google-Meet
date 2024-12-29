import pyaudio
import wave

def record_audio(file_name="meeting_recording.wav", duration=300):
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000  # 16kHz sample rate
    CHUNK = 1024
    RECORD_SECONDS = duration  # Record for 5 minutes (or adjust)

    audio = pyaudio.PyAudio()

    print("Recording started...")
    stream = audio.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

    frames = []

    try:
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)

        print("Recording stopped.")
    except KeyboardInterrupt:
        print("\nRecording stopped manually.")
    finally:
        stream.stop_stream()
        stream.close()
        audio.terminate()

    with wave.open(file_name, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

    print(f"Recording completed! File saved as {file_name}")

# Uncomment to test this function directly
# record_audio("meeting_recording.wav", 300)
