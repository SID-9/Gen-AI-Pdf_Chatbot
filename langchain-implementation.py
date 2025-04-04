import os
import gradio as gr
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.document_loaders import PyPDFLoader
from langchain.llms import Ollama
from langchain.chains import RetrievalQA
from langchain.text_splitter import CharacterTextSplitter

# Embedding model
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Load LLaMA 2 from Ollama
llm = Ollama(model="llama2")

def process_pdf_and_create_chain(pdf_path):
    # Load and split PDF
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()
    
    # Optional: Split into chunks (important for large docs)
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.split_documents(documents)

    # Create FAISS vector store
    vector_store = FAISS.from_documents(docs, embedding_model)

    # Create Retrieval QA Chain
    chain = RetrievalQA.from_chain_type(llm=llm, retriever=vector_store.as_retriever())
    return chain

# Gradio interface function
def chatbot_interface(pdf, query):
    if pdf is not None:
        pdf_path = pdf.name
        qa_chain = process_pdf_and_create_chain(pdf_path)
        result = qa_chain.run(query)
        return result
    return "Please upload a PDF."

# Launch Gradio UI
demo = gr.Interface(
    fn=chatbot_interface,
    inputs=[gr.File(label="Upload PDF"), gr.Textbox(label="Ask a Question")],
    outputs=gr.Textbox(label="Chatbot Response"),
    title="LangChain PDF Chatbot with LLaMA 2"
)

demo.launch()
