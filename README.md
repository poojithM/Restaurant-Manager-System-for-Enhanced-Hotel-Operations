# Restaurant Manager System for Enhanced Hotel Operations

## Overview
This project is designed to help restaurant managers improve their systems by leveraging a multi-agent framework powered by CrewAI. It processes customer review audio data to derive actionable insights for enhancing service quality. The system utilizes OpenAI's Whisper model to convert audio reviews into text and then orchestrates multiple agents to:

- **Summarize** the transcribed review.
- **Analyze Sentiment** (positive, negative, neutral) from the summary.
- **Extract Keywords** that highlight key aspects (e.g., "service is slow", "food is good").
- **Generate a Brief Report** with recommendations to improve hotel operations.

## Features
- **Audio-to-Text Conversion:** Uses the Whisper model to transcribe customer review audios.
- **Multi-Agent Processing:** 
  - **Summarizer Agent:** Condenses the review text.
  - **Sentiment Analyzer Agent:** Determines the overall sentiment and percentages.
  - **Keyword Extractor Agent:** Identifies important keywords in the text.
  - **Reporter Agent:** Compiles findings into a concise report.
- **Modular Design:** Built with CrewAI to allow easy integration and extension of additional agents/tasks.

## Project Architecture
1. **Input Stage:**  
   Audio data (customer reviews) is provided as input.
   
2. **Transcription Stage:**  
   The Whisper model transcribes audio into text.
   
3. **Processing Stage:**  
   The transcribed text is processed sequentially by a series of agents:
   - **Summarizer:** Condenses the text.
   - **Sentiment Analyzer:** Evaluates sentiment.
   - **Keyword Extractor:** Pulls out key phrases.
   - **Reporter:** Generates a final report with recommendations.
   
4. **Output Stage:**  
   A report (e.g., `report.md`) is produced that details sentiment, key insights, and suggestions for system improvements.

## Dependencies
- **CrewAI:** For orchestrating agents and tasks.
- **Pydantic:** For data validation and model creation.
- **OpenAI Python Library:** To interact with the Whisper API.
- **Pydub:** For audio processing.
- **Other Tools:** Environment management using `python-dotenv` for loading API keys and configurations.

## Setup 
**Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
```

**Install Dependencies**
```bash
pip install -r requirements.txt
```

***Environment Variables**
```bash
OPENAI_API_KEY=your_openai_api_key_here
```

## Usage
**Run the main application by executing:**
```bash
python main.py
```
**The system will:**
- Transcribe the provided audio file.
- Process the transcription through the configured CrewAI agents.
- Generate and save a report detailing sentiment analysis, extracted keywords, and recommendations.




