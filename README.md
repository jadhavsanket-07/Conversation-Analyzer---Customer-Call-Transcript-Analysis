# Conversation Analyzer - Customer Call Transcript Analysis App

A simple FastAPI-based web app that analyzes customer call transcripts using the Groq AI API. The app summarizes conversations and extracts customer sentiment (positive, neutral, negative), then saves the results in a CSV file.

---

## Features

- Web interface to input customer call transcripts.
- Uses Groq API's LLaMA 3.1 model for:
  - Generating a concise summary of the transcript.
  - Extracting customer sentiment.
- Displays original transcript, summary, and color-coded sentiment result.
- Saves all analyses to a CSV file (`conversations.csv`) for record keeping.

---

## Tech Stack

- **Python 3.8+**
- **FastAPI** - lightweight web framework for API and UI.
- **Pandas** - handling CSV file operations.
- **Groq API** - for AI-powered text analysis.
- **Uvicorn** - ASGI server to run the FastAPI app.

---

## Getting Started

### Prerequisites

- Python 
- Groq API key (you need to sign up and obtain your own API key)

