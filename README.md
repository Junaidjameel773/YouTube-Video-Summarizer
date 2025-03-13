# YouTube Video Summarizer with Gemini

## Overview
This is a Streamlit-based web application that extracts the transcript from a YouTube video and generates a concise summary using Google's Gemini AI. The summary provides key points from the video transcript in under 250 words.

## Features
- Extracts transcript from a given YouTube video URL.
- Uses Google Gemini AI to generate a summary.
- Displays the video thumbnail for better visualization.
- Provides summarized notes in an easy-to-read format.

## Requirements
Ensure you have the following dependencies installed:

```
youtube_transcript_api
streamlit
google-generativeai
python-dotenv
pathlib
```

Install them using:
```
pip install -r requirements.txt
```

## Setup and Usage
1. Clone this repository or download the project files.
2. Install the required dependencies using the command above.
3. Set up a `.env` file and add your **Google API Key**:
   ```
   GOOGLE_API_KEY=your_google_api_key
   ```
4. Run the Streamlit application:
   ```
   streamlit run app.py
   ```
5. Enter the YouTube video link in the input field and click the **Get Detailed Notes** button.
6. The app will extract the transcript, summarize it using Gemini AI, and display the summary.

## How It Works
- The app extracts the transcript from the YouTube video using `youtube_transcript_api`.
- The transcript is passed to Gemini AI with a predefined prompt.
- The summarized text is then displayed on the Streamlit UI.

## Example Output
```
### Detailed Notes:
Here's a summary of the YouTube video in concise points:

Gemma 3 Overview: The video reviews Google's Gemma 3 open-source AI model, focusing on its performance in problem-solving, math, and ethics.
Context Window: Gemma 3 has a 128k context window, but long-term memory within that window may degrade....
```

## License
This project is open-source and available for modification and distribution.

