# RAG with Langchain for PDF Question Answering

This project demonstrates the implementation of Retrieval-Augmented Generation (RAG) using Langchain for answering questions from a PDF document. The model retrieves relevant information from the document and generates answers based on the retrieved context.

## Features

- **PDF Question Answering**: This system allows you to ask questions based on the content of a PDF file.
- **Langchain Integration**: Uses Langchain to handle the language model interface, document retrieval, and question answering.
- **Retrieval-Augmented Generation (RAG)**: Combines retrieval of relevant document parts with language model generation to answer questions accurately.
- **Easy Setup**: Simple configuration to get started with minimal setup.
- **Efficient PDF Processing**: Extracts text from PDF documents and processes it for question answering.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/hoangphuu/RAG-with-Langchain-for-PDF-question-answering.git
    cd RAG-with-Langchain-for-PDF-question-answering
    ```

2. Create a virtual environment:
    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Ensure that you have the necessary API keys and environment variables configured:
    - Set up Langchain API key (if applicable).
    - Install additional dependencies for PDF text extraction if needed (e.g., PyPDF2 or pdfminer).

## Usage

### Step 1: Prepare Your PDF
Make sure your PDF file is accessible in the project directory or provide the full path to the file in the configuration.

### Step 2: Configure the Question Answering System
Edit the configuration file or directly update the script to point to your PDF file and set up Langchain with your preferred language model.

### Step 3: Run the Question Answering Script
Run the following command to start the system:
```bash
python question_answering.py
```

### Step 4: Ask Questions
Once the script is running, you can enter questions related to the content of the PDF. The system will retrieve relevant sections of the document and provide an answer based on the context.
Example:
```bash
> What is the main topic of the document?
> The main topic of the document is ...
