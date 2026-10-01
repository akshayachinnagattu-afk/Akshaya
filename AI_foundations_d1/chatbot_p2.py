from ollama import chat
import stremlit as st

st.set_page_config(page_tittle = "Llamabot App" page_icon="")
st.tittle("Llamabot -Here to talk")

personality = "You are a feiendly and patient tutor" 

if "history" not in st.session_state:
    st.session_state.history = [{"role" : "system","content" : personality}]

    with st.chat_message("assistant"):
        st.write(question)
    response = chat(mode)="ollama3.2",messages = st.session_state.history;

    reply = response["message"]["content"]
    st.session_state.history.append({"role" : "assistant","content":reply})

    with st.chat_message("assistant"):
        st.write(reply)
except Exception as e:
    st.write("ollama is not working. Try again.")


