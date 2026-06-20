# MoodLens — Sentiment Chrome Extension

MoodLens is an AI-powered Chrome extension that analyzes social media comments and determines whether audience reactions are Positive, Negative, or Neutral.

The extension extracts comments from platforms like YouTube and Reddit, sends them to an AI sentiment engine, and displays a clean analytics dashboard with sentiment statistics.

---

# Features

- Real-time sentiment analysis
- Positive / Negative / Neutral detection
- Chrome extension support
- Manual comment sentiment analyzer
- Smooth and calm UI
- FastAPI backend
- NLP-powered sentiment engine
- Supports hundreds of comments

---

# Supported Platforms

- YouTube
- Reddit

Future Support:
- Twitter/X
- Instagram
- Facebook
- LinkedIn

---

# Tech Stack

## Frontend
- HTML
- CSS
- JavaScript
- Chrome Extension API

## Backend
- FastAPI
- Python

## AI / NLP
- HuggingFace Transformers
- RoBERTa Sentiment Model

---

# Project Structure

```bash
sentiment-extension/
│
├── backend-api/
├── frontend-extension/
├── docs/
└── README.md
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/Riktam45/moodlens-sentiment-chrome-extension.git
```

---

# Backend Setup

```bash
cd backend-api

pip install -r requirements.txt

uvicorn main:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

---

# Load Chrome Extension

1. Open Chrome
2. Go to:

```text
chrome://extensions/
```

3. Enable Developer Mode
4. Click "Load unpacked"
5. Select:

```text
frontend-extension
```

---

# Future Improvements

- Animated sentiment graphs
- Real-time monitoring
- Multi-language sentiment analysis
- Toxicity detection
- AI-generated audience summaries
- Instagram/Facebook integration

---

# Author

GitHub: https://github.com/Riktam45