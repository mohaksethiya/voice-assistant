# Voice Assistant 🎙️

A Python-based voice assistant that combines speech recognition with Google's Gemini API to provide an interactive voice-based experience.

## Features

- Speech recognition using Vosk.
- AI-powered responses using the Gemini API.
- Graphical user interface built with Tkinter / CustomTkinter.
- Voice input through a microphone.

## Tech Stack

- Python
- Tkinter / CustomTkinter
- Vosk
- Google Gemini API
- SoundDevice

## Prerequisites

- Python installed on your computer.
- A Gemini API key.
- A compatible Vosk speech recognition model.
- A working microphone.

## Setup

1. Clone this repository.
2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project directory and add your Gemini API key:

   ```env
   GEMINI_API_KEY=your_actual_api_key_here
   ```

4. Download the Vosk model required by the application and place it in the location expected by the code.

5. Run the application:

   ```bash
   python main.py
   ```

## Configuration

Keep your API key private. The `.env` file is excluded from version control.

Use `.env.example` as a reference for the required environment variables.

## Future Improvements

- Improve speech recognition accuracy.
- Expand assistant capabilities.
- Improve error handling and user experience.
