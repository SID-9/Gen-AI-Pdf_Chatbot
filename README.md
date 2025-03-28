# 📝 AI-Based PDF Chatbot

## 📌 Overview
This project is an **AI-powered chatbot** that can **answer questions** based on the content of uploaded PDFs. It uses **LLaMA 2, FAISS, and LangChain** to implement **Retrieval-Augmented Generation (RAG)** for document-based Q&A. The chatbot works **fully offline and locally**, ensuring privacy and no API costs!

## 🚀 Features
- 📄 Upload PDF documents
- 🔎 Ask questions about the PDF content
- 🤖 Uses **LLaMA 2 (via Ollama) for local inference**
- ⚡ Efficient search with **FAISS Vector Store**
- 🛠️ Built with **LangChain** for easy integration
- 🎨 Simple **Gradio UI** for interaction

## 🛠️ Installation & Setup

### 1️⃣ Prerequisites
Ensure you have the following installed:
- **Python 3.8+**
- **Pip** (Package Manager)
- **Ollama** (For running LLaMA 2 locally) → [Download Ollama](https://ollama.com/download)

### 2️⃣ Install Dependencies
```sh
pip install faiss-cpu pypdf2 gradio langchain sentence-transformers
```

### 3️⃣ Download LLaMA 2
```sh
ollama pull llama2
```

## 🏃 Running the Chatbot
Run the following command:
```sh
python pdf_chatbot.py
```
This will launch the chatbot UI in your browser.

## 🧠 How It Works
1. 📂 **Upload a PDF** → The text is extracted and split into chunks.
2. 🔢 **Generate Embeddings** → Sentence embeddings are created using **Sentence Transformers**.
3. 📚 **Store in FAISS** → The text chunks are stored in **FAISS Vector Store** for quick retrieval.
4. 🤖 **Retrieve & Generate Answer** → When a user asks a question, relevant chunks are retrieved and passed to **LLaMA 2** for response generation.

## 🖥️ Tech Stack
- **LLaMA 2** (via Ollama) → Local LLM inference
- **LangChain** → Document processing & RAG
- **FAISS** → Vector search for document retrieval
- **Sentence Transformers** → Text embedding generation
- **PyPDF2** → PDF text extraction
- **Gradio** → UI for easy interaction

## 📸 Screenshot
<img width="959" alt="3" src="https://github.com/user-attachments/assets/96b3d9e8-8b8d-4064-8e6f-6eb0fd7bf7af" />


## 📬 Contact
If you have any questions or suggestions, feel free to reach out!

---
🚀 **Happy Coding!** 🎉


