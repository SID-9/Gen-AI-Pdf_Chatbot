import os
import ollama
import faiss
import gradio as gr
import numpy as np
import PyPDF2
from sentence_transformers import SentenceTransformer

# load embedding model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# extract text from the pdf
def extract_text_from_pdf(pdf_path):
    with open(pdf_path,"rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
        
    return text
        
# create FAISS index
def create_faiss_index(texts):
    embeddings = model.encode(texts, normalize_embeddings=True)
    dimension = embeddings.shape[1]
    index=faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    
    return index,texts

# function to retrieve similar text from faiss index
def retrieve_similar_text(query, index, texts, top_k=2):
    query_embedding = model.encode([query], normalize_embeddings=True)
    distances, indices = index.search(query_embedding, top_k)
    
    return [texts[i] for i in indices[0]]

# function to generate response using ollama
def chat_with_llama(context,question):
    prompt = f"Context: {context}\nUser: {question}\nAI:"
    response = ollama.chat(model='llama2',messages=[{'role':'user','content':prompt}])
    
    return response['message']['content']

# gradio UI function
def chatbot_interface(pdf,query):
    if pdf is not None:
        pdf_path = pdf.name
        text = extract_text_from_pdf(pdf_path)
        index, texts = create_faiss_index([text])
        retrieved_text = " ".join(retrieve_similar_text(query,index,texts))
        
        return chat_with_llama(retrieved_text,query)
    return "Please upload a PDF file."



# launch gradio UI
demo = gr.Interface(
    fn=chatbot_interface,
    inputs=[gr.File(label="Upload PDF"), gr.Textbox(label="Ask a Question ? ")],
    outputs=gr.Textbox(label="Chatbot Response : ")
)

demo.launch()