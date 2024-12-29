import os
from record_audio import record_audio  # Import the recording function
from audio_to_text import convert_audio_to_wav, transcribe_audio  # Import the necessary functions
from summarize_text import summarize_text  # For summarizing the transcript
from extract_actions import extract_action_items  # For extracting action items
from generate_pdf import generate_pdf  # For generating the final PDF output

# Ensure that Google Cloud credentials are set before proceeding
def set_google_credentials():
    # Path to your service account credentials (change this to your actual file path)
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\devvi\Downloads\smart-meeting-note-taker-a318708d1ccf.json"  # Update with correct path

# Function to record audio
def record_and_process_audio(output_audio_file="meeting_recording.wav", duration=300):
    print("Starting recording...")
    record_audio(output_audio_file, duration)  # Record audio for the specified duration
    print(f"Recording completed! File saved as {output_audio_file}")
    
    # Convert the recorded audio to WAV format
    output_audio_converted = "converted_meeting.wav"
    print(f"Converting audio from {output_audio_file} to WAV format...")
    convert_audio_to_wav(output_audio_file, output_audio_converted)
    print(f"Audio saved as {output_audio_converted}")

    return output_audio_converted

# Main process flow
def main():
    set_google_credentials()  # Set Google credentials
    
    input_audio_file = "meeting_recording.wav"  # This will be the input file after recording
    converted_audio_file = record_and_process_audio(input_audio_file, duration=300)  # Record and convert audio

    try:
        # Transcribe the audio
        print("Transcribing the audio...")
        transcript = transcribe_audio(converted_audio_file)
        print(f"Transcript: {transcript[:200]}...")  # Display first 200 characters of the transcript
        
        # Summarize the transcription
        print("Summarizing the transcription...")
        summary = summarize_text(transcript)
        print(f"Summary: {summary[:200]}...")  # Display first 200 characters of the summary
        
        # Extract action items from the transcript
        print("Extracting action items...")
        actions = extract_action_items(transcript)
        print(f"Actions: {actions}")

        # Generate a PDF with the summary and action items
        print("Generating PDF...")
        generate_pdf(summary, actions)
        print("PDF generated successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

# Run the main function
if __name__ == "__main__":
    main()
