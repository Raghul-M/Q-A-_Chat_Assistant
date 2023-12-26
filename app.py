import streamlit as st
from langchain_helper import get_qa_chain, create_vector_db


st.title("Knowledge Base Q&A Assistant 🌱")


btn = st.button("Create Knowledgebase")
if btn:
    create_vector_db()

st.text_area("","Steps To Follow:""\n""1.Upload a csv file Contains Column Questions and Answers ""\n2. Then Hit Knowledge Base")



user_input = st.text_input("Question: ")
"[![Open in GitHub](https://github.com/codespaces/badge.svg)](https://github.com/Raghul-M/StreamChatify/)"


def github():
    badge(type="github", name="streamlit/streamlit")

if st.button("Generate Chat ", key="generate_button"):
        with st.spinner(text='In progress'):
            chain = get_qa_chain()
            response = chain(user_input)  
            st.success('Done')
            st.header("Answer: ")
            st.write(response["result"])

