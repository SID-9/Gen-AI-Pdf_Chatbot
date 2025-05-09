**🧠 Smart PDF Q&A Bot with Semantic Search & GPT**
Upload any PDF and ask questions about its content using sentence embeddings for retrieval and GPT-3.5 for answers. Powered by FastAPI, Streamlit, and Docker.
________________________________________
**🚀 Features**
•	📄 Upload and read PDF documents
•	✂️ Chunk long PDFs for better processing
•	🔍 Retrieve semantically relevant chunks using MiniLM embeddings
•	🤖 Ask questions and get GPT-3.5 answers based on context
•	🧪 Streamlit UI + FastAPI backend
•	🐳 Fully Dockerized for deployment
________________________________________
**🧱 Tech Stack**
Component	Technology
Frontend	Streamlit
Backend	FastAPI
PDF Parser	PyMuPDF (fitz)
Embeddings	sentence-transformers MiniLM
Similarity	Cosine Similarity (sklearn)
LLM	OpenAI GPT-3.5
Containerization	Docker
________________________________________
**📁 Project Structure**
.
├── app.py            # Streamlit frontend
├── main.py           # FastAPI backend
├── Dockerfile        # Docker container config
├── requirements.txt  # Python dependencies
└── README.md
________________________________________
**🔧 Local Installation (Without Docker)**
1. Clone the repo

git clone https://github.com/your-username/smart-pdf-qa-bot.git
cd smart-pdf-qa-bot

2. Create a virtual environment

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Run the app

# Run FastAPI
uvicorn main:app --reload

# In another terminal, run Streamlit
streamlit run app.py
________________________________________
**🐳 Docker Deployment (Recommended)**
1. Build the Docker image
docker build -t pdf-qa-bot .

2. Run the container
docker run -p 8000:8000 -p 8501:8501 pdf-qa-bot
•	📍 Access FastAPI docs at: http://localhost:8000/docs
•	📍 Access the Streamlit app at: http://localhost:8501
________________________________________
**📌 Notes**
•	You must provide your OpenAI API key in the UI after uploading the PDF.
•	The app selects top-3 semantically similar chunks before calling GPT.
•	Make sure your OpenAI key has sufficient credits.

