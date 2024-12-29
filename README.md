# Smart Meeting Note-Taker for Google Meet
 This project is a smart meeting note-taking application that records meetings, transcribes the audio, summarizes the meeting, extracts action items, and generates a PDF with the meeting notes.



Here’s a detailed **README.md** file that you can use for your project on GitHub. It includes everything from setting up the project to running it successfully.

---

# Smart Meeting Note-Taker

This project is a smart meeting note-taking application that records meetings, transcribes the audio, summarizes the meeting, extracts action items, and generates a PDF with the meeting notes.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Requirements](#requirements)
- [Setup Instructions](#setup-instructions)
- [Running the Project](#running-the-project)
- [Google Cloud Speech API Setup](#google-cloud-speech-api-setup)
- [Project Structure](#project-structure)
- [Credits](#credits)

## Features

- **Audio Recording:** Records audio from the microphone for a specified duration.
- **Audio Conversion:** Converts the audio file to the correct format for transcription (WAV format).
- **Transcription:** Converts speech to text using the Google Cloud Speech-to-Text API.
- **Summarization:** Summarizes the transcription into concise meeting points.
- **Action Items Extraction:** Extracts action items from the meeting transcript.
- **PDF Generation:** Generates a PDF containing the meeting summary and action items.

## Technologies Used

- **Python**: The main programming language used for the application.
- **PyAudio**: For recording audio from the microphone.
- **Google Cloud Speech-to-Text API**: For transcribing the audio to text.
- **PyPDF2**: For generating the PDF output.
- **pydub**: For audio processing and conversion.
- **Flask/Django** (Optional): You can integrate with web frameworks if required.

## Requirements

- **Python 3.12+**
- **Google Cloud Platform account** with Speech-to-Text API enabled.
- **PyAudio**, **Google Cloud Python client**, **pydub**, **PyPDF2**, and other required libraries.

To install the required dependencies, run the following command:

```bash
pip install -r requirements.txt
```

**Note**: Make sure you have **ffmpeg** installed on your machine, as it's required for audio format conversion.

## Setup Instructions

1. **Clone this Repository**
   
   Clone the repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/Smart-Meeting-Note-Taker.git
   cd Smart-Meeting-Note-Taker
   ```

2. **Set up Google Cloud API**

   You need to create a Google Cloud project and enable the **Speech-to-Text API**. Follow these steps to set it up:

   - Go to [Google Cloud Console](https://console.cloud.google.com/).
   - Create a new project.
   - Enable the **Speech-to-Text API**.
   - Create a **Service Account** and download the **JSON credentials file**.

   **Set the environment variable for authentication:**

   ```bash
   set GOOGLE_APPLICATION_CREDENTIALS="C:\path\to\your\service-account-file.json"
   ```

   Or, you can add the following line at the beginning of your code:

   ```python
   import os
   os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\path\to\your\service-account-file.json"
   ```

3. **Install Dependencies**

   Create a `requirements.txt` file in the root of the project with the following contents:

   ```text
   google-cloud-speech
   pyaudio
   pydub
   pyPDF2
   ```

   Install the dependencies by running:

   ```bash
   pip install -r requirements.txt
   ```

4. **Install ffmpeg**

   Install **ffmpeg** to enable audio conversion with pydub:
   
   - [Download ffmpeg](https://ffmpeg.org/download.html).
   - Extract the contents and add the bin folder to your system's PATH.

   Example for Windows:

   ```bash
   set PATH=C:\path\to\ffmpeg\bin;%PATH%
   ```

## Running the Project

After you have completed the setup and installed all dependencies, run the `main.py` file to start the application.

```bash
python main.py
```

The program will:

1. Start recording the audio for 5 minutes (you can adjust the duration).
2. Convert the recorded audio to a WAV file.
3. Transcribe the audio using the Google Cloud Speech API.
4. Summarize the transcribed text.
5. Extract the action items from the summary.
6. Generate a PDF with the summary and action items.

**Note**: The program will save the audio, transcription, and PDF files in the current working directory.

## Google Cloud Speech API Setup

To set up the **Google Cloud Speech API** and obtain your service account credentials file, follow these steps:

1. Create a **Google Cloud account** at [https://cloud.google.com/](https://cloud.google.com/).
2. Create a **new project**.
3. **Enable the Speech-to-Text API** in the project.
4. Create a **service account** and download the **JSON key** file for authentication.
5. Set the **GOOGLE_APPLICATION_CREDENTIALS** environment variable to point to the location of your downloaded service account file.

For detailed instructions on setting up **Google Cloud Speech-to-Text**, refer to this guide: [Setting up Google Cloud Speech-to-Text](https://cloud.google.com/speech-to-text/docs/quickstart).

## Project Structure

Here's the structure of the project:

```
Smart-Meeting-Note-Taker/
├── audio_to_text.py            # Handles audio to text conversion (using Google Cloud Speech API)
├── extract_actions.py         # Extracts action items from transcriptions
├── generate_pdf.py            # Generates a PDF file from meeting notes
├── main.py                    # Main script to run the meeting note taker
├── record_audio.py            # Records the audio from the microphone
├── requirements.txt           # Python dependencies
├── summarize_text.py          # Summarizes the transcribed text
└── README.md                  # This file
```

### Descriptions of Key Files

- **`audio_to_text.py`**: Contains functions to convert audio files to text using Google Cloud Speech API.
- **`extract_actions.py`**: Extracts action items from the transcribed text (based on specific patterns).
- **`generate_pdf.py`**: Generates a PDF file that contains the summary and action items.
- **`record_audio.py`**: Handles the audio recording process.
- **`summarize_text.py`**: Summarizes the transcribed text into concise meeting points.
- **`main.py`**: This is the main script that integrates all the steps (recording, transcribing, summarizing, and generating a PDF).

## Credits

- **Google Cloud Speech-to-Text API**: For transcribing the audio.
- **PyAudio**: For recording the audio from the microphone.
- **pydub**: For audio conversion.
- **PyPDF2**: For generating the PDF file with meeting notes.

---

Let me know if you need any changes or clarifications.
