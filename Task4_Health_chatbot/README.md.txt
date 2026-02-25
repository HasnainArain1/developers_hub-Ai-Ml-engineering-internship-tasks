# Health LLM Chatbot

A simple health-focused chatbot built using a Large Language Model (LLM) via OpenRouter API.

## Features

- Provides general health information
- Avoids diagnosis and prescriptions
- Implements a safety filter for harmful queries
- Built with Streamlit for a simple web interface
- Uses OpenRouter to access Mistral-7B-Instruct model

## Project Structure

health-llm-chatbot/
│
├── notebook.ipynb      # Development and testing
├── app.py              # Streamlit web application
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation


## Setup Instructions

1. Clone the repository:

   git clone <your-repo-link>
   cd health-llm-chatbot

2. Install dependencies:

   pip install -r requirements.txt

3. Set your OpenRouter API key as environment variable:

   Windows:
   setx HF_TOKENN "your_api_key"

   Mac/Linux:
   export HF_TOKENN="your_api_key"

4. Run the application:

   streamlit run app.py

## Usage

- Enter a general health-related question.
- The chatbot provides informational responses.
- Unsafe or harmful queries are blocked.

## Disclaimer

This chatbot provides general health information only.
It does not provide medical diagnosis, prescriptions, or emergency advice.
Always consult a qualified healthcare professional for medical concerns.