import streamlit as st
import requests
import os



API_URL = "https://openrouter.ai/api/v1/chat/completions"
HF_TOKENN = os.getenv("HF_TOKENN")

SYSTEM_PROMPT = """
You are a helpful medical assistant.
Provide general health information only.
Do not provide diagnosis, prescriptions, or exact dosages.
Encourage consulting a healthcare professional for serious concerns.
Keep responses clear and friendly.
"""


def is_safe_query(user_input):
    danger_keywords = [
        "suicide",
        "kill myself",
        "overdose",
        "exact dosage",
        "emergency treatment",
        "prescription amount"
    ]
    return not any(word in user_input.lower() for word in danger_keywords)


def ask_model(user_input):
    if HF_TOKENN is None:
        return "API token not found. Please configure environment variable."

    headers = {
        "Authorization": f"Bearer {HF_TOKENN}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",
        "X-Title": "health-llm-chatbot"
    }

    data = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ],
        "max_tokens": 400
    }

    try:
        response = requests.post(API_URL, headers=headers, json=data, timeout=60)
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {str(e)}"



# Streamlit UI

st.set_page_config(page_title="Health LLM Chatbot", page_icon="🏥")

st.title("Health LLM Chatbot")
st.write("Ask general health-related questions. This chatbot does not provide diagnosis or prescriptions.")

user_input = st.text_input("Enter your question:")

if st.button("Submit"):
    if user_input.strip() == "":
        st.warning("Please enter a question.")
    elif not is_safe_query(user_input):
        st.error("Unsafe query detected. Please consult a healthcare professional.")
    else:
        with st.spinner("Generating response..."):
            answer = ask_model(user_input)
            st.success("Response:")
            st.write(answer)