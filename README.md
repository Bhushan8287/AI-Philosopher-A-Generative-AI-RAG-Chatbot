# AI Philosopher Chatbot

An AI-powered question-answering application built with Streamlit and LangChain.  
It leverages local text document about philosophy to provide context-based answers using a Retrieval-Augmented Generation (RAG) pipeline.  
This project demonstrates foundational skills in GenAI application development, including LLM integration, embeddings, and vector search.


## Project Structure
````
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
````

## Installation
1. Clone the repository
2. Create and activate a virtual enviornment
   -> python -m venv venv
      # How to run it:
      # On Windows
      .\venv\Scripts\activate
3. Install dependencies
   ````
   -> pip install -r requirements.txt
   ````
   
5. ## Ollama Setup
   -> This project uses Ollama to run local language models for both embeddings and language generation.
   Prerequisites:
   -> Download and install Ollama from offical website
   Ensure Ollama is running before launching the app
   # Required Models
   Run these commands in the cmd
   ````
   -> ollama run nomic-embed-text
   -> ollama run gemma3:1b(LLM of your choice)
   -> You only need to do this once. Ollama will handle the rest during runtime
   ````
   
7. Run the application
   -> streamlit run app.py

## Demo Screenshot
See `Screenshot.png` in the root directory for a preview of the application interface.
