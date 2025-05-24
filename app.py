import gradio as gr
from smolagents import LiteLLMModel, CodeAgent, tool
import os
from pypdf import PdfReader
from litellm import completion

#Initialize the Model
model = LiteLLMModel(
    model_name="gemini/gemini-1.5-flash",
    api_key=os.environ.get("GEMINI_API_KEY")
)

#tool to extract text from PDF
@tool
def process_pdf(file_path: str) -> str:
    """
    Extract text from a PDF file.
    Args:
        file_path (str): Path to the PDF file.
    Returns:
        str: Extracted text from the PDF.
    """
    reader = PdfReader(file_path)
    return "\n".join([page.extract_text() for page in reader.pages])

#tool to analysis the pdf for answering question
@tool
def chat_with_pdf(query: str, pdf_text: str, chat_history: list) -> str:
    """
    Answer questions about the PDF content.
    Args:
        query (str): The question to answer.
        pdf_text (str): The text extracted from the PDF.
        chat_history (list): Previous chat history.
    Returns:
        str: Answer to the question.
    """
    pass

#Agent to handle the chat with PDF
agent = CodeAgent(
    model=model,
    model_kwargs={
        "model": "gemini/gemini-pro",
        "api_base": "https://generativelanguage.googleapis.com/v1beta",  # Correct Google API endpoint
        "api_key": os.getenv("GEMINI_API_KEY")  # Ensure key is set in environment
    },
    tools=[process_pdf, chat_with_pdf]
)
#Gradio Interface
def process_pdf_ui(file):
    pdf_text = process_pdf(file.name)
    return pdf_text

def chat_ui(query, history, pdf_text):
    response = agent.run(
        f"PDF Context: {pdf_text}\nUser Query: {query}\nChat History: {history}"
    )
    return response, history + [(query, response)]

with gr.Blocks() as demo:
    gr.Markdown("# PDF Chatbot")
    with gr.Row():
        pdf_input = gr.File(label="Upload PDF", file_types=[".pdf"])
        pdf_text = gr.Textbox(visible=False)

        chatbot = gr.Chatbot(type="messages")
        msg = gr.Textbox(placeholder="Ask a question about the PDF")

        pdf_input.upload(process_pdf_ui, inputs=pdf_input, outputs=pdf_text)
        msg.submit(chat_ui, inputs=[msg, chatbot, pdf_text], outputs=[chatbot, msg])

if __name__ == "__main__":
    demo.launch()
