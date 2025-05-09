import streamlit as st 
import requests 

backend_url = "http://localhost:8000"

st.set_page_config(page_title="Smart PDF QA Bot (Client)", layout="wide")
st.title("📄 Smart PDF QA Bot (Streamlit + FastAPI)")

# upload pdf to backend
uploaded_file = st.file_uploader("Upload a pdf file : ",type=["pdf"])

if uploaded_file:
    api_key = st.text_input("Enter your OpenAI api key: ",type="password")
    
    if api_key:
        st.session_state.api_key= api_key
        
        if st.button("Read PDF"):
            with st.spinner("Reading and chunking PDF..."):
                files = {"file": (uploaded_file.name,uploaded_file,"application/pdf")}
                
                response = requests.post(f"{backend_url}/pdf-file", files=files)
                
                if response.status_code == 200:
                    
                    result = response.json()
                    content= result['contents']
                    st.session_state.content = content 
                    
                    # CHUNKING
                    response2 = requests.post(f"{backend_url}/chunk-text",json={'text':content})
                    
                    result2 = response2.json()['chunks']
                    st.session_state.chunks = result2
                    st.success("PDF Uploaded and Chunked Successfully!")
                
                else:
                    st.error("Error reading the PDF")
            
    if "chunks" in st.session_state:
        user_question = st.text_input("Ask a question about the pdf ")
        
        if user_question:
            with st.spinner("Finding Answer..."):
                response3 = requests.post(f"{backend_url}/find-chunks",
                                          json={
                                              "chunks":st.session_state.chunks,
                                              "question":user_question,
                                              "top_k":3
                                          })

                result3 = response3.json()['top_chunks']
                context = "\n\n".join(result3)
                
                #ASKING GPT
                
                response4 = requests.post(
                    f"{backend_url}/ask-gpt",
                    json={
                        'question':user_question,
                        'context':context,
                        'api_key':st.session_state.api_key
                    }
                )
                
                if response4.status_code == 200:
                    result5 = response4.json()["answer"]
                    st.subheader("💬 Answer:")
                    st.write(result5)

                    with st.expander("📜 Retrieved Context"):
                        st.write(context)
                else:
                    st.error("Error from GPT API")
            
        
