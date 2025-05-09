from fastapi import FastAPI, status,UploadFile,File
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import fitz
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from openai import OpenAI

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = SentenceTransformer("allMiniLM-L6-v2")

class PdfRead(BaseModel):
    filename:str
    contents:str

class Chunking(BaseModel):
    text:str
    chunk_size=500

class SemanticSearch(BaseModel):
    chunks: list[str]
    question: str
    top_k: int=3

class AskGpt(BaseModel):
    question:str
    context:str
    api_key:str
    

@app.post("/pdf-file",response_model=PdfRead,status_code=status.HTTP_200_OK)
async def pdf_file(file:UploadFile=File(...)):
    pdf = await file.read()
    
    doc = fitz.open(stream=pdf,filetype="pdf")
    all_text=""
    
    for page in doc:
        all_text += page.get_text()
    
    doc.close()
    
    return PdfRead(
        filename=file.filename,
        contents=all_text.strip()
    )
    

@app.post("/chunk-text")
def chunk_text(data:Chunking):
    words = data.text.split()
    chunks = [' '.join(words[i:i+data.chunk_size]) for i in range(0,len(words),data.chunk_size)]
    
    return {'chunks':chunks}

@app.post("/find-chunks")
def find_chunks(data:SemanticSearch):
    
    chunk_embeddings= model.encode(data.chunks)
    question_embedding = model.encode([data.question])
    
    similarities = cosine_similarity(question_embedding,chunk_embeddings).flatten()
    
    top_indices = similarities.argsort()[-data.top_k:][::-1]
    top_chunks = [data.chunks[i] for i in top_indices]
    
    return {"top_chunks":top_chunks}

@app.post("/ask-gpt",status_code=status.HTTP_200_OK)
def ask_gpt(data:AskGpt):
    
    prompt=f"""
    You are a helpful assistant. Answer the question based on the provided context in a concise way.
    
    context:
    {data.context}
    
    question:
    {data.question}
    
    Answer:
    """
    
    client = OpenAI(api_key=data.api_key)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {'role':'user','content':prompt}
        ]
    )
    
    answer= response.choices[0].message.content
    return {'answer':answer}