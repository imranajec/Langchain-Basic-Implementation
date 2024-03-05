import os
from constants import openai_key
from langchain.llms import OpenAI
os.environ["OPENAI_API_KEY"]=openai_key
import streamlit as st
 
st.title('Langchain Demo with OpenAI API')
input_text=st.text_input("Search the topic you want")

llm=OpenAI(temperature=0.8)


if input_text:
    st.write(llm(input_text)) 