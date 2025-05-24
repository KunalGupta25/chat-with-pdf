import os
import gradio as gr
from smolagents import CodeAgent, tool, LiteLLMModel
from pypdf import PdfReader
from dotenv import load_dotenv

# Load environment variables (for local dev)
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not set. Please set it in your .env or Hugging Face Space secrets.")

# --------- TOOLS ---------
@tool
def process_pdf(file_path: str) -> str:
    """
    Extract text from a PDF file.
    Args:
        file_path (str): Path to the PDF file.
    Returns:
        str: Extracted text from the PDF.
    """
    try:
        reader = PdfReader(file_path)
        return "\n".join([page.extract_text() or "" for page in reader.pages])
    except Exception as e:
        return f"PDF extraction failed: {str(e)}"

@tool
def chat_with_pdf(query: str, pdf_text: str) -> str:
    """
    Answer questions about the PDF content.
    Args:
        query (str): The user's question.
        pdf_text (str): Text extracted from the PDF.
    Returns:
        str: The answer to the question based on the PDF content.
    """
    # The actual logic is handled by the agent's LLM
    pass

# --------- AGENT SETUP ---------
model = LiteLLMModel(
    model_id="gemini/gemini-1.5-flash",  # Use "gemini/gemini-1.5-pro" if you have access
    api_key=GEMINI_API_KEY
    # Do NOT set api_base for Gemini AI Studio keys!
)

agent = CodeAgent(
    tools=[process_pdf, chat_with_pdf],
    model=model
)

# --------- GRADIO INTERFACE ---------
def process_pdf_ui(file):
    if not file:
        return ""
    return process_pdf(file.name)

def chat_ui(message, history, pdf_text):
    if not pdf_text:
        return [{"role": "assistant", "content": "Please upload a PDF first."}]
    # Compose a prompt for the agent
    prompt = f"PDF Content:\n{pdf_text}\n\nUser Question: {message}"
    try:
        response = agent.run(prompt)
        # Return response in OpenAI-style message format for Gradio
        history = history or []
        history.append({"role": "user", "content": message})
        history.append({"role": "assistant", "content": response})
        return history
    except Exception as e:
        history = history or []
        history.append({"role": "assistant", "content": f"Error: {str(e)}"})
        return history

with gr.Blocks() as demo:
    gr.Markdown("# 📄 Chat with your PDF")
    with gr.Row():
        with gr.Column(scale=1):
            pdf_input = gr.File(label="Upload PDF", file_types=[".pdf"])
            pdf_text = gr.Textbox(visible=False)
        with gr.Column(scale=3):
            chatbot = gr.Chatbot(label="PDF Chat", height=400, type="messages")
            msg = gr.Textbox(label="Ask a question about the PDF", placeholder="Type your question and hit Enter...")
    gr.Markdown("**Note:** This app uses the Gemini AI model to process your PDF and answer questions. Make sure to upload a PDF first and add your Google API in secrets. You can get it from [Gemini AI Studio](https://aistudio.google.com/apikey).")
    pdf_input.upload(
        fn=process_pdf_ui,
        inputs=pdf_input,
        outputs=pdf_text
    )

    msg.submit(
        fn=chat_ui,
        inputs=[msg, chatbot, pdf_text],
        outputs=chatbot
    )

if __name__ == "__main__":
    demo.launch()
