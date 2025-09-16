# 💬 Conversation Analyzer - Customer Call Transcript Analysis App

A simple **FastAPI**-based web app that analyzes customer call transcripts using the **Groq AI API**. The app summarizes conversations and extracts customer sentiment (positive, neutral, negative) and saves the results in a CSV file. 

---

## 🚀 Features

- 🌐Web interface to input customer call transcripts.
- 🤖 Uses Groq API's LLaMA 3.1 model for:
  - ✍️ Generating concise summary of the transcript.
  - 😊 Extracting customer sentiment (Positive, Neutral, Negative).
- 📊 Displays original transcript, summary, and color-coded sentiment result.
- 💾 Saves all analyses to a CSV file (`conversations.csv`) for record keeping.

---

## 🛠️ Tech Stack

- Python 
- FastAPI - lightweight web framework for API and UI 
- Pandas - CSV file handling 
- Groq API - AI-powered text analysis 
- Uvicorn - ASGI server to run FastAPI 

---

## ⚙️ Getting Started

### Prerequisites

- Python 
- Groq API key (signup required)


Open your web browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/). Enter a customer call transcript in the text area and click **Analyze**.

---

## 📝 Usage Example

Input:

> “Hi, I was trying to book a slot yesterday but the payment failed…”

Output:

- Summary → “Customer faced a payment failure while booking a slot.”
- Sentiment → “Negative” (displayed in red on the results page)

The output line is saved to `conversations.csv` as a new entry.

---

## 📂 Output Storage

- All analyzed transcripts, summaries, and sentiments are saved in `conversations.csv`.
- This CSV file has the following columns:
  - Transcript
  - Summary
  - Sentiment
- This format supports easy data tracking and further data analysis.

---
