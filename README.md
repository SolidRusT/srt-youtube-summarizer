# SRT YouTube summarizer 📝

This project is an AI-powered video summarizer designed specifically for YouTube videos. Leveraging the OpenAI API, it employs advanced machine learning techniques to analyze and condense lengthy YouTube videos into concise summaries, providing users with quick insights into the video content.


## Features ✨

- Automatic extraction of key insights and timestamps from YouTube videos.
- Utilizes youtube-transcript-api for getting the transcripts/subtitles YouTube video.
- Option for users to select AI models like *GPT* for summarization.
- Efficiently summarizes videos, reducing viewing time while preserving essential information.

## Getting Started 🚀

### Prerequisites

- Python 3.11
- LLM Model API Keys [[🔑]](https://github.com/siddharthsky/ai-video-summarizer-and-timestamp-generator-LLM-p/tree/main?tab=readme-ov-file#get-api-keys)

### Usage

1. Clone the repository:
```
git clone https://github.com/SolidRusT/srt-youtube-summarizer.git
```
2. Navigate to the project directory:
```
cd srt-youtube-summarizer
```
3. Install dependencies:
```
pip install -U pip
pip install -U -r requirements.txt
```
4. Create a ".env" file ⬇️ [add whichever is available]
```
OPENAI_API_KEY = "Your-Openai-Key-Here"
```

### Get API Keys:
   
- [OpenAI ChatGPT API key](https://platform.openai.com/signup) 🔑 
   
5. Run the summarizer:
```
streamlit run app.py
```

## Contributing

Contributions are welcome from the community!, Whether it's feedback, suggestions, or code improvements, your input is valuable. 

## Acknowledgments

- [OpenAI ChatGPT](https://help.openai.com/en/) 
