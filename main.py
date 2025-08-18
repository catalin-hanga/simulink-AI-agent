from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

import matlab.engine
eng = matlab.engine.start_matlab()

import streamlit as st
import speech_recognition as sr

from agent import agent_executor
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler

st.set_page_config(page_title = "SimuLang", page_icon = ":robot_face:")

st.markdown("""
        <style>
               .block-container {
                    padding-top:    2.8rem;
                    padding-bottom: 0.5rem;
                }
        </style>
        """, unsafe_allow_html = True)

def stream_data(answer : str):
    import time
    for word in answer.split(" "):
        yield word + " "
        time.sleep(0.03)

emojis = {"user": "👨‍🔬", "assistant": "🤖"}

@st.fragment
def main_loop():

    container = st.container(border = True, height = 550)

    if "messages" not in st.session_state:
        st.session_state["messages"] = []
    else:
        with container:
            for message in st.session_state["messages"]:
                with st.chat_message(name = message["role"], avatar = emojis[message["role"]]):
                    st.markdown(body = message["content"])

    (col1, col2) = st.columns([0.9, 0.1])

    with col1:
        user_messge = st.chat_input(placeholder = "Please enter your query here")

    with col2:
        if st.button(label = ":studio_microphone:"):
            recognizer = sr.Recognizer()
            microphone = sr.Microphone()
            with microphone as source:
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)
            user_messge = recognizer.recognize_openai(audio)

    if user_messge:
        with container:

            with st.chat_message(name = "user", avatar = emojis["user"]):
                st.markdown(body = user_messge)

            with st.chat_message(name = "assistant", avatar = emojis["assistant"]):
                st_callback = StreamlitCallbackHandler(
                                                        parent_container = st.container(),
                                                        expand_new_thoughts = False,
                                                        collapse_completed_thoughts = True,                                   
                                                    )
            
                response = agent_executor.invoke(
                        {"input": user_messge, "chat_history": st.session_state["messages"]}, 
                        {"callbacks": [st_callback]},
                    )
                
                st.write_stream(stream_data(response["output"]))

            st.session_state["messages"].append({"role": "user",      "content": response["input"]})    
            st.session_state["messages"].append({"role": "assistant", "content": response["output"]})

main_loop()