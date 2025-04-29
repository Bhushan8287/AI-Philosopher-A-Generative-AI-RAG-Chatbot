# AI Philosopher Chatbot

An AI-powered question-answering application built with Streamlit and LangChain.  
It leverages local text documents about philosophy to provide context-based answers using a Retrieval-Augmented Generation (RAG) pipeline.  
This project demonstrates foundational skills in GenAI application development, including LLM integration, embeddings, and vector search.


## Project Structure
GEN AI PROJECT/
├── genaivenv/         # Virtual environment (excluded from version control)
├── .gitignore         # Git configuration to exclude files/folders
├── requirements.txt   # Python dependencies
├── Project/           # Project folder containing source files
│   ├── app.py         # Main Streamlit application
│   ├── building.py    # Script for prototyping or processing
│   ├── .env           # Environment variables (excluded)
│   ├── data.txt       # Knowledge base or data source
│   └── chroma_db/     # Vector database for embeddings

## Installation
1. Clone the repository
2. Create and activate a virtual enviornment
    -> python -m venv venv
      # Activate it:
      # On Windows
      .\venv\Scripts\activate
3. Install dependencies
   -> pip install -r requirements.txt
4. Run the application
5. -> streamlit run app.py
