import streamlit as st
from streamlit_chatbox import *
import time
import simplejson as json
from groq import Groq
from dotenv import load_dotenv
import os
load_dotenv()

TEST_RESPONSE = {
  "query": "Who have I spoken to about vector databases?",
  "results": [
    {
      "conversation_id": "conv123",
      "timestamp": "2024-09-05T14:30:00Z",
      "location": "TechConf 2024, San Francisco",
      "participants": ["x", "y"],
      "summary": "Discussion about vector databases, their advantages, challenges, and recommended systems.",
      "relevance_score": 0.95,
      "topics": ["vector databases", "similarity search", "semantic search", "recommendation systems", "image recognition", "scaling challenges", "embedding models"],
      "entities": {
        "people": ["x", "y"],
        "technologies": ["vector databases", "Pinecone", "Weaviate"],
        "concepts": ["similarity search", "semantic search", "recommendation systems", "image recognition", "high-dimensional data", "embedding models"]
      },
      "highlights": [
        "I heard you've been working with vector databases lately",
        "We've been exploring their potential for improving our search capabilities",
        "main advantage is their ability to perform similarity searches efficiently",
        "scaling can be tricky, especially when dealing with high-dimensional data",
        "We've had good experiences with Pinecone and Weaviate"
      ]
    }
  ],
  "metadata": {
    "total_results": 1,
    "processing_time":0.05
    }
}

def get_answer(context, metadata):

    client = Groq(
        api_key=os.getenv("GROQ_API_KEY"),
    )
    completion = client.chat.completions.create(
        model="llama-3.1-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "Answer in detail"
            },
            {
                "role": "user",
                "content": f"""Below is the context of two people speaking:\n{context}
                    Here is the metadata when user gave the following query:\n{metadata}
                    \nBased on the metadata and context, provide the answer that answers the user's query 
                    """
            }
        ],
        temperature=0,
        max_tokens=1024,
        top_p=1,
        stream=False,
        stop=None,
    )

    result = completion.choices[0].message.content
    print(result)
    return result



llm = FakeLLM()
chat_box = ChatBox()
chat_box.use_chat_name("chat1") # add a chat conversatoin

def on_chat_change():
    chat_box.use_chat_name(st.session_state["chat_name"])
    chat_box.context_to_session() # restore widget values to st.session_state when chat name changed


with st.sidebar:
    st.header('Start to chat with your conversations')
    # chat_name = st.selectbox("Chat Session:", ["default", "chat1"], key="chat_name", on_change=on_chat_change)
    # chat_box.use_chat_name(chat_name)
    # streaming = st.checkbox('streaming', key="streaming")
    in_expander = st.checkbox('show messages in expander', key="in_expander")
    # show_history = st.checkbox('show session state', key="show_history")
    chat_box.context_from_session(exclude=["chat_name"]) # save widget values to chat context

    st.divider()

    btns = st.container()

    file = st.file_uploader(
        "chat history json",
        type=["json"]
    )

    if st.button("Load Json") and file:
        data = json.load(file)
        chat_box.from_dict(data)

    if st.button("test"):
        get_answer(os.getenv("TEST_TRANSCRIPTION"), TEST_RESPONSE)


chat_box.init_session()
chat_box.output_messages()

def on_feedback(
    feedback,
    chat_history_id: str = "",
    history_index: int = -1,
):
    reason = feedback["text"]
    score_int = chat_box.set_feedback(feedback=feedback, history_index=history_index) # convert emoji to integer
    # do something
    st.session_state["need_rerun"] = True


feedback_kwargs = {
    "feedback_type": "thumbs",
    "optional_text_label": "wellcome to feedback",
}

if query := st.chat_input('input your question here'):
    chat_box.user_say(query)
    chat_box.ai_say(
        [
            Markdown("thinking", in_expander=in_expander,
                        expanded=True, title="answer"),
            Markdown("", in_expander=in_expander, title="references"),
        ]
    )
    # text, docs = llm.chat(query)
    text = get_answer(os.getenv("TEST_TRANSCRIPTION"), TEST_RESPONSE) # take user query here
    chat_box.update_msg(text, element_index=0, streaming=False, state="complete")
    # chat_box.update_msg("\n\n".join(docs), element_index=1, streaming=False, state="complete")

btns.download_button(
    "Export Markdown",
    "".join(chat_box.export2md()),
    file_name=f"chat_history.md",
    mime="text/markdown",
)

btns.download_button(
    "Export Json",
    chat_box.to_json(),
    file_name="chat_history.json",
    mime="text/json",
)

if btns.button("clear history"):
    chat_box.init_session(clear=True)
    st.rerun()

