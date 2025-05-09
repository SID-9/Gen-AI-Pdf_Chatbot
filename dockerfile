# Use the official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app


# Install pip requirements
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

# Expose ports
EXPOSE 8000
EXPOSE 8501

# Start FastAPI backend and Streamlit frontend in parallel
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port 8000 & streamlit run app.py --server.port 8501 --server.address 0.0.0.0"]
