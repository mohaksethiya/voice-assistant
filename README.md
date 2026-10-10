## Prerequisites

Before running the application, make sure you have:

- Python installed.
- A working microphone.
- A Gemini API key.
- The required Vosk speech recognition model.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/mohaksethiya/voice-assistant.git
cd voice-assistant
```

### 2. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 3. Configure the Gemini API

The application uses Google's Gemini API to generate AI responses.

1. Obtain your API key from the [Google AI Studio API key page](https://aistudio.google.com/apikey).
2. Create a file named `.env` in the project's root directory.
3. Add your API key to the file:

```env
GEMINI_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your own API key.

### 4. Download the Vosk Speech Recognition Model

The application uses Vosk for speech recognition.

1. Visit the [official Vosk models page](https://alphacephei.com/vosk/models).
2. Download the `vosk-model-small-en-us-0.15` model.
3. Extract the downloaded archive.
4. Place the extracted model folder in the location expected by the application.

Ensure that the model folder name and path match the configuration in the source code.

### 5. Run the Application

Start the voice assistant with:

```bash
python main.py
```

## Security

- Keep your Gemini API key private.
- Never commit or upload your `.env` file.
- The `.env.example` file provides a template for the required environment variable.
