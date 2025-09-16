from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Request
from openai import OpenAI
import pandas as pd

# Groq API client with API key and base URL
client = OpenAI(
    api_key="gsk_Mzob0S9cRzIB7FWQtcVOWGdyb3FYuYthC54VbGpiZD",
    base_url="https://api.groq.com/openai/v1"
)

app = FastAPI()

# CSV file path
CSV_FILE = "conversations.csv"

# CSV with headers if it doesn't exist
df = pd.DataFrame(columns=["Transcript", "Summary", "Sentiment"])
df.to_csv(CSV_FILE, index=False)


@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <html>
    <head>
        <title>Conversation Analyzer</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: #f0f4f8;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .container {
                background: white;
                padding: 30px 40px;
                border-radius: 12px;
                box-shadow: 0 8px 20px rgba(0,0,0,0.1);
                max-width: 600px;
                width: 100%;
            }
            h2 {
                margin-bottom: 20px;
                color: #333;
                text-align: center;
            }
            textarea {
                width: 100%;
                height: 150px;
                padding: 12px;
                border: 2px solid #ddd;
                border-radius: 8px;
                font-size: 16px;
                resize: vertical;
                transition: border-color 0.3s ease;
            }
            textarea:focus {
                border-color: #4a90e2;
                outline: none;
            }
            button {
                margin-top: 20px;
                width: 100%;
                padding: 14px;
                background-color: #4a90e2;
                border: none;
                border-radius: 8px;
                color: white;
                font-size: 18px;
                cursor: pointer;
                transition: background-color 0.3s ease;
            }
            button:hover {
                background-color: #357ABD;
            }
            .footer {
                margin-top: 15px;
                font-size: 14px;
                color: #666;
                text-align: center;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Conversation Analyzer</h2>
            <form action="/analyze" method="post">
                <textarea name="transcript" placeholder="Enter transcript here..."></textarea>
                <button type="submit">Analyze</button>
            </form>
            <div class="footer">Enter a customer call transcript and get a summary with sentiment analysis.</div>
        </div>
    </body>
    </html>
    """


@app.post("/analyze", response_class=HTMLResponse)
async def analyze(request: Request):
    form_data = await request.form()
    transcript = form_data.get("transcript")

    prompt = f"""
    You are an AI assistant. Analyze the following transcript:
    Transcript: "{transcript}"
    Provide:
    1. A concise Summary
    2. Sentiment (Positive, Neutral, Negative)
    Format: Summary -> "...", Sentiment -> "..."
    """

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )
        output = response.choices[0].message.content

        try:
            summary = output.split("Summary ->")[1].split("Sentiment ->")[0].strip().strip('"')
            sentiment = output.split("Sentiment ->")[1].strip().strip('"')
        except:
            summary = "Error parsing response"
            sentiment = "Unknown"

        # Save to CSV
        new_row = pd.DataFrame([[transcript, summary, sentiment]],
                               columns=["Transcript", "Summary", "Sentiment"])
        new_row.to_csv(CSV_FILE, mode="a", header=False, index=False)

        # Return styled HTML response
        return f"""
        <html>
        <head>
            <title>Analysis Result</title>
            <style>
                body {{
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background: #f0f4f8;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }}
                .result-container {{
                    background: white;
                    padding: 30px 40px;
                    border-radius: 12px;
                    box-shadow: 0 8px 20px rgba(0,0,0,0.1);
                    max-width: 700px;
                    width: 100%;
                }}
                h2 {{
                    color: #333;
                    margin-bottom: 20px;
                    text-align: center;
                }}
                .section {{
                    margin-bottom: 20px;
                }}
                .label {{
                    font-weight: 700;
                    color: #4a90e2;
                    margin-bottom: 6px;
                    display: block;
                    font-size: 18px;
                }}
                .content {{
                    background: #f9fafb;
                    border: 1px solid #ddd;
                    border-radius: 8px;
                    padding: 15px;
                    font-size: 16px;
                    white-space: pre-wrap;
                    color: #444;
                }}
                .sentiment {{
                    font-weight: 700;
                    font-size: 20px;
                    color: {{"#28a745" if sentiment.lower() == "positive" else "#ffc107" if sentiment.lower() == "neutral" else "#dc3545"}};
                }}
                .back-link {{
                    display: block;
                    margin-top: 30px;
                    text-align: center;
                    font-size: 16px;
                    color: #4a90e2;
                    text-decoration: none;
                }}
                .back-link:hover {{
                    text-decoration: underline;
                }}
            </style>
        </head>
        <body>
            <div class="result-container">
                <h2>Conversation Analysis Result</h2>
                <div class="section">
                    <span class="label">Transcript:</span>
                    <div class="content">{transcript}</div>
                </div>
                <div class="section">
                    <span class="label">Summary:</span>
                    <div class="content">{summary}</div>
                </div>
                <div class="section">
                    <span class="label">Sentiment:</span>
                    <div class="content sentiment">{sentiment}</div>
                </div>
                <a href="/" class="back-link">&larr; Analyze another transcript</a>
            </div>
        </body>
        </html>
        """

    except Exception as e:
        return HTMLResponse(f"<h3>Error: {str(e)}</h3>", status_code=500)

