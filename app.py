

import os
from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, SystemMessage

# Load environment variables
load_dotenv()

# Initialize API key and model
groq_api_key = os.getenv("groq_key")
model = ChatGroq(model="Gemma2-9b-It", groq_api_key=groq_api_key)

# Initialize output parser
parser = StrOutputParser()

# Streamlit app configuration
st.set_page_config(page_title='Q&A Demo')

# Streamlit app layout
st.header('Chatbot using Groq API key')

input_text = st.text_input('Input your question:', key='input')
submit = st.button("Ask Me", type="primary")

if submit:
    if input_text:
        # Prepare messages for the model
        messages = [
            SystemMessage(content="You are a helpful assistant."),
            HumanMessage(content=input_text)
        ]
        
        # Generate response using the model
        response = model.invoke(messages)
        response_text = parser.parse(response)
        
        st.subheader('Your answer is:')
        st.write(response_text.content)
    else:
        st.write("Please enter a question.")
        



