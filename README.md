# 📄 Chat with PDF – Gemini AI Agent

A conversational AI agent that lets you upload any PDF and chat with its contents!  
Built with [smolagents](https://github.com/smol-ai/smol-agents), [Google Gemini](https://aistudio.google.com/), [pypdf](https://pypdf.readthedocs.io/), and [Gradio](https://gradio.app/).

---

## 🌐 Try it Online

> **Live Demo:**  
> [https://huggingface.co/spaces/your-username/your-space-name](https://huggingface.co/spaces/your-username/your-space-name)

---

## 🏗️ Tech Stack

| Layer              | Technology                                | Purpose                                    |
|--------------------|-------------------------------------------|--------------------------------------------|
| LLM Orchestration  | [smolagents](https://github.com/smol-ai/smol-agents) | Agent framework, tool integration          |
| Language Model     | [Google Gemini 1.5 Flash](https://aistudio.google.com/) | Large Language Model for Q&A               |
| LLM API Adapter    | [LiteLLM](https://github.com/BerriAI/litellm)           | Unified LLM API interface                  |
| PDF Processing     | [pypdf](https://pypdf.readthedocs.io/)                  | Extracts text from uploaded PDF files      |
| Web UI             | [Gradio](https://gradio.app/)                           | Interactive chat interface                 |
| Environment Mgmt   | [python-dotenv](https://pypi.org/project/python-dotenv/) | Loads environment variables (local dev)    |
| Deployment         | [Hugging Face Spaces](https://huggingface.co/spaces)    | Cloud hosting (public demo)                |

---

## 🚀 Features

- **Upload any PDF** and extract its text instantly.
- **Ask questions** about the document—get answers powered by Google Gemini (1.5 Flash).
- **Conversational interface** using Gradio.
- **Runs locally or on Hugging Face Spaces**.

---

## 🛠️ Installation (Local)

1. **Clone this repository:**
```bash
git clone https://github.com/yourusername/pdf-chat-gemini
cd pdf-chat-gemini
```
2. **Install dependencies:**
```bash
pip install -r requirements.txt
```
3. **Set up your Gemini API Key:**
- Get your key from [Google AI Studio](https://aistudio.google.com/app/apikey).
- Create a `.env` file in the project root:
  ```
  GEMINI_API_KEY=your_actual_key_here
  ```

---
## 📝 Usage

### **Local**
```py
python app.py
```
Open [http://localhost:7860](http://localhost:7860) in your browser.

### **Hugging Face Spaces**

- Go to your Space: [https://huggingface.co/spaces/your-username/your-space-name](https://huggingface.co/spaces/your-username/your-space-name)
- Click **"Duplicate Space"** to make your own copy, or use it directly if public.
- Add your `GEMINI_API_KEY` as a secret in the Space settings (if you duplicate or deploy privately).


---

## ⚙️ Configuration

- **Model:** Uses `"gemini/gemini-1.5-flash"` by default. If you have access to `"gemini/gemini-1.5-pro"`, change the `model_id` in `app.py`.
- **API Key:** Must be a [Google AI Studio](https://aistudio.google.com/app/apikey) key, not a Vertex AI or GCP key.
- **No `api_base` needed** for Gemini AI Studio keys.

---

## 🧩 How it Works

1. **Upload a PDF**: The app extracts all text using `pypdf`.
2. **Ask a question**: Your question and the extracted text are sent to the Gemini model via smolagents.
3. **Get answers**: The agent uses Gemini to answer your question, referencing the PDF content.

---

## 🧑‍💻 For Developers

- **Add more tools**: Use the `@tool` decorator from smolagents to add custom functions.
- **Customize the UI**: Edit the Gradio blocks in `app.py`.
- **Chunking or RAG**: For large PDFs, consider splitting text into chunks and using retrieval-augmented generation.

---


## 📜 License

MIT License.  
See [LICENSE](LICENSE) for details.

---

## 🙌 Acknowledgments

- [smol-ai/smol-agents](https://github.com/smol-ai/smol-agents)
- [Google AI Studio](https://aistudio.google.com/)
- [Gradio](https://gradio.app/)
- [pypdf](https://pypdf.readthedocs.io/)

---

**Enjoy chatting with your PDFs!**  
For questions or contributions, open an issue or pull request.

---


