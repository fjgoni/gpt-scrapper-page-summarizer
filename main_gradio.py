import gradio as gr
from scrapper.web_scrapper import WebScraper
from open_ai.openai_client import OpenAIClient
from open_ai.gpt_assistant import GPTAgent

html_extractor_prompt =  """
You are an HTML text extraction agent. Your task is to extract only the visible textual content from a given HTML document.
Ignore all HTML tags, attributes, and non-textual elements such as <script>, <style>, <meta>, buttons, anchor tags (<a>), forms, or any other structural or interactive HTML elements.
Do not include any tag names, hrefs, class names, or IDs—only return the text that would be visible to a human user when the HTML is rendered in a browser.
Preserve the reading order and hierarchy of content (e.g., headings before paragraphs, paragraphs before list items, etc.), but do not include any formatting markup.
Your output should be a clean, plain-text version of the content, ready for further natural language processing or indexing.
"""
summarizer_prompt = "You are an assistant that receives technical texts and produces well-structured, detailed summaries. \
      Instead of shortening the content too much, you should explain each important concept clearly and thoroughly. \
          Organize your response into sections or bullet points when appropriate. Provide practical, easy-to-understand \
            examples to illustrate complex ideas. Your goal is to make technical content accessible to smart readers \
                who may not be experts. Avoid excessive simplification, but keep explanations readable and efficient."

summarizer_page_prompt = "You are an assistant that analyzes the contents of several relevant pages from a company website \
and creates a short brochure about the company for prospective customers, investors and recruits. Respond in text format\
Include details of company culture, customers and careers/jobs if you have the information."

def process_url(url: str) -> str:
    try:
        scraper = WebScraper(url)
        html = scraper.scrape_full_page_html()
        openai_client = OpenAIClient()

        visible_text = GPTAgent(client=openai_client, system_prompt=html_extractor_prompt).run(html)
        summarized_page = GPTAgent(client=openai_client, system_prompt=summarizer_page_prompt).run(visible_text)

        return summarized_page
    except Exception as e:
        return f"An error occurred: {str(e)}"

demo = gr.Interface(
    fn=process_url,
    inputs=gr.Textbox(label="Enter Website URL"),
    outputs=gr.Textbox(label="Summarized Content", lines=30),
    title="Website Summarizer",
    description="Paste a company URL to get a summarized brochure-style text of its content."
)

demo.launch()
