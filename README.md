# 🕸️ Website Summarizer with Gradio + OpenAI

This project allows you to enter a website URL, scrape the full HTML content, extract only the visible text, and generate a human-readable summary (brochure-style) using OpenAI's GPT model. It includes a user-friendly interface built with **Gradio**.

## 🚀 Features

- ✅ Scrape the full HTML content of any public website  
- ✅ Clean and extract only human-visible text (ignoring tags, buttons, scripts, etc.)  
- ✅ Use OpenAI to summarize the content into an informative brochure  
- ✅ Gradio interface for easy URL input and summary output

## 📦 Installation

1. **Clone the repository**:

```bash
git clone https://github.com/your-username/website-summarizer.git
cd website-summarizer
```

2. **Create and activate a virtual environment (optional but recommended)**:

```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On Mac/Linux:
source venv/bin/activate
```

3. **Install the dependencies**:

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt`, install manually:

```bash
pip install gradio openai beautifulsoup4 requests
```

## ⚙️ How It Works

- The `WebScraper` class downloads the full HTML content of a page.  
- The `GPTAgent` uses a prompt to extract only visible text from that HTML.  
- Another prompt summarizes the extracted content as if it were a company brochure.  
- Gradio displays the summarized result in a web interface.

## 🖥️ Run the App

Just launch the Gradio interface:

```bash
python app.py
```

Replace `app.py` with the filename where your Gradio code lives.

This will open a local web server in your browser at:  
**http://localhost:7860**

## 🧠 Prompts Used

- **HTML Extractor Prompt**: Strips out all code and only keeps content visible to users.  
- **Page Summarizer Prompt**: Summarizes a website like a short brochure, including culture, customers, and job info when available.

You can customize these prompts to adapt the tone and level of detail.

## 📁 Project Structure

```
.
├── app.py                        # Gradio interface
├── scrapper/
│   └── web_scrapper.py          # Web scraper for pulling HTML content
├── open_ai/
│   ├── openai_client.py         # Wrapper for OpenAI API
│   └── gpt_assistant.py         # GPTAgent logic using system prompts
└── README.md                    # This file
```

## 🔐 API Keys

Make sure your `OpenAIClient` is configured with your OpenAI API key.  
This can be done via environment variable or configuration file.

## 📃 License

MIT License. Feel free to use, modify, and share.

## ✨ Example

Paste in a URL like `https://viainfo.com.ar/` and get back a company-style summary in seconds!

![example gif or screenshot here if available]