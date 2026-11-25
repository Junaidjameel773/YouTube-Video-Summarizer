import streamlit as st
from dotenv import load_dotenv

load_dotenv() ##load all the nevironment variables
import os
import google.generativeai as genai

from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

prompt="""You are Yotube video summarizer. You will be taking the transcript text
and summarizing the entire video and providing the important summary in points
within 250 words. Please provide the summary of the text given here:  """


## extract the video id from watch, youtu.be, shorts and embed links
def get_video_id(url):
    url = url.strip()
    if "://" not in url:
        url = "https://" + url
    u = urlparse(url)
    if u.hostname == "youtu.be":
        return u.path.lstrip("/").split("/")[0] or None
    if u.path.startswith(("/shorts/", "/embed/")):
        return u.path.split("/")[2] or None
    return parse_qs(u.query).get("v", [None])[0]

## getting the transcript data from yt videos
def extract_transcript_details(youtube_video_url):
    try:
        video_id=get_video_id(youtube_video_url)
        
        transcript_text=YouTubeTranscriptApi.get_transcript(video_id)

        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]

        return transcript

    except Exception as e:
        raise e
    
## getting the summary based on Prompt from Google Gemini Pro
def generate_gemini_content(transcript_text,prompt):

    model=genai.GenerativeModel("gemini-2.0-flash")
    response=model.generate_content(prompt+transcript_text)
    return response.text

st.title("YouTube Transcript to Detailed Notes Converter")
youtube_link = st.text_input("Enter YouTube Video Link:")

video_id = get_video_id(youtube_link) if youtube_link else None
if youtube_link and not video_id:
    st.error("Could not find a video ID in that link.")
if video_id:
    st.image(f"https://img.youtube.com/vi/{video_id}/0.jpg", use_container_width=True)

if st.button("Get Detailed Notes") and video_id:
    transcript_text=extract_transcript_details(youtube_link)

    if transcript_text:
        summary=generate_gemini_content(transcript_text,prompt)
        st.markdown("## Detailed Notes:")
        st.write(summary)
