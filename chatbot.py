from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
    MessagesPlaceholder
)
import streamlit as st
from streamlit_chat import message
#from utils import *
st.set_page_config(page_title="AU-Bot")
st.title('Admissions Guide')
st.subheader("Chatbot with Langchain, OpenAI,FAISS, HF and Streamlit")
st.markdown("""
---
Made with 🤖 by [Abdula Beyg](https://github.com/Hooded-dev/)""")