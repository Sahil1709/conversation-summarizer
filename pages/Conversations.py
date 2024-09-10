import streamlit as st
from streamlit_chatbox import *
import time
import simplejson as json
from groq import Groq
from dotenv import load_dotenv
import os
load_dotenv()

TEST_RESPONSE = [
  {
    "distance": 0.3404202461242676,
    "duration": 62.24,
    "entities": {
      "GPE": [
        ""
      ],
      "ORG": [
        "Pinecone"
      ],
      "PERSON": [
        "Baviate",
        "Sahil",
        "Puranjay"
      ],
      "PRODUCT": [
        ""
      ],
      "TECH": [
        "Any Particular Vector Database Systems",
        "Vector Databases",
        "Recommendation Systems",
        "Traditional Relational Databases"
      ]
    },
    "id": "67b049dd-de1a-449b-974e-a9354a98d5a2",
    "keywords": {
      "databases": 0.4685212856658182,
      "good": 0.31234752377721214,
      "great": 0.31234752377721214,
      "puranjay": 0.15617376188860607,
      "recognition": 0.15617376188860607,
      "recommend": 0.15617376188860607,
      "search": 0.31234752377721214,
      "systems": 0.31234752377721214,
      "vector": 0.4685212856658182,
      "yes": 0.31234752377721214
    },
    "language": "English",
    "score": 0.6595797538757324,
    "topics": [
      {
        "id": 0,
        "terms": []
      },
      {
        "id": 1,
        "terms": []
      },
      {
        "id": 2,
        "terms": []
      }
    ],
    "transcript": " Hey Puranjay, great to see you at the conference. I heard you've been working with vector databases lately. Hi Sahil. Yes, that's right. We've been exploring the potential for improving our search capabilities. That's fascinating. What advantages have you found in using vector databases over traditional relational databases? Well, the main advantage is their ability to perform similarity searches efficiently. They're great for tasks like semantic search, recommendation systems, and image recognition. Interesting. Have you faced any challenges in implementing them? Yes. Scaling them can be tricky, especially when dealing with high-dimensional data. Also, there's a learning curve in terms of designing effective embedding models. I can imagine. Are there any particular vector database systems you'd recommend? We've had good experiences with Pinecone and Baviate. They both offer good performances and have solid documentation."
  },
  {
    "distance": 0.3404202461242676,
    "duration": 62.24,
    "entities": {
      "GPE": [
        ""
      ],
      "ORG": [
        "Pinecone"
      ],
      "PERSON": [
        "Puranjay",
        "Sahil",
        "Baviate"
      ],
      "PRODUCT": [
        ""
      ],
      "TECH": [
        "Any Particular Vector Database Systems",
        "Recommendation Systems",
        "Vector Databases",
        "Traditional Relational Databases"
      ]
    },
    "id": "0ddfdfdc-180c-48af-b5f9-650a36f42f89",
    "keywords": {
      "databases": 0.4685212856658182,
      "good": 0.31234752377721214,
      "great": 0.31234752377721214,
      "puranjay": 0.15617376188860607,
      "recognition": 0.15617376188860607,
      "recommend": 0.15617376188860607,
      "search": 0.31234752377721214,
      "systems": 0.31234752377721214,
      "vector": 0.4685212856658182,
      "yes": 0.31234752377721214
    },
    "language": "English",
    "score": 0.6595797538757324,
    "topics": [
      {
        "id": 0,
        "terms": []
      },
      {
        "id": 1,
        "terms": []
      },
      {
        "id": 2,
        "terms": []
      }
    ],
    "transcript": " Hey Puranjay, great to see you at the conference. I heard you've been working with vector databases lately. Hi Sahil. Yes, that's right. We've been exploring the potential for improving our search capabilities. That's fascinating. What advantages have you found in using vector databases over traditional relational databases? Well, the main advantage is their ability to perform similarity searches efficiently. They're great for tasks like semantic search, recommendation systems, and image recognition. Interesting. Have you faced any challenges in implementing them? Yes. Scaling them can be tricky, especially when dealing with high-dimensional data. Also, there's a learning curve in terms of designing effective embedding models. I can imagine. Are there any particular vector database systems you'd recommend? We've had good experiences with Pinecone and Baviate. They both offer good performances and have solid documentation."
  },
  {
    "distance": 0.3404202461242676,
    "duration": 62.24,
    "entities": {
      "GPE": [
        ""
      ],
      "ORG": [
        "Pinecone"
      ],
      "PERSON": [
        "Puranjay",
        "Sahil",
        "Baviate"
      ],
      "PRODUCT": [
        ""
      ],
      "TECH": [
        "Any Particular Vector Database Systems",
        "Recommendation Systems",
        "Vector Databases",
        "Traditional Relational Databases"
      ]
    },
    "id": "35f8757e-8582-4b61-a5f1-a2fcd8daf4ed",
    "keywords": {
      "databases": 0.4685212856658182,
      "good": 0.31234752377721214,
      "great": 0.31234752377721214,
      "puranjay": 0.15617376188860607,
      "recognition": 0.15617376188860607,
      "recommend": 0.15617376188860607,
      "search": 0.31234752377721214,
      "systems": 0.31234752377721214,
      "vector": 0.4685212856658182,
      "yes": 0.31234752377721214
    },
    "language": "English",
    "score": 0.6595797538757324,
    "topics": [
      {
        "id": 0,
        "terms": []
      },
      {
        "id": 1,
        "terms": []
      },
      {
        "id": 2,
        "terms": []
      }
    ],
    "transcript": " Hey Puranjay, great to see you at the conference. I heard you've been working with vector databases lately. Hi Sahil. Yes, that's right. We've been exploring the potential for improving our search capabilities. That's fascinating. What advantages have you found in using vector databases over traditional relational databases? Well, the main advantage is their ability to perform similarity searches efficiently. They're great for tasks like semantic search, recommendation systems, and image recognition. Interesting. Have you faced any challenges in implementing them? Yes. Scaling them can be tricky, especially when dealing with high-dimensional data. Also, there's a learning curve in terms of designing effective embedding models. I can imagine. Are there any particular vector database systems you'd recommend? We've had good experiences with Pinecone and Baviate. They both offer good performances and have solid documentation."
  },
  {
    "distance": 0.3404202461242676,
    "duration": 62.24,
    "entities": {
      "GPE": [
        ""
      ],
      "ORG": [
        "Pinecone"
      ],
      "PERSON": [
        "Baviate",
        "Sahil",
        "Puranjay"
      ],
      "PRODUCT": [
        ""
      ],
      "TECH": [
        "Vector Databases",
        "Traditional Relational Databases",
        "Recommendation Systems",
        "Any Particular Vector Database Systems"
      ]
    },
    "id": "1d97653e-48cd-4b39-9d91-2eee8ef7573e",
    "keywords": {
      "databases": 0.4685212856658182,
      "good": 0.31234752377721214,
      "great": 0.31234752377721214,
      "puranjay": 0.15617376188860607,
      "recognition": 0.15617376188860607,
      "recommend": 0.15617376188860607,
      "search": 0.31234752377721214,
      "systems": 0.31234752377721214,
      "vector": 0.4685212856658182,
      "yes": 0.31234752377721214
    },
    "language": "English",
    "score": 0.6595797538757324,
    "topics": [
      {
        "id": 0,
        "terms": []
      },
      {
        "id": 1,
        "terms": []
      },
      {
        "id": 2,
        "terms": []
      }
    ],
    "transcript": " Hey Puranjay, great to see you at the conference. I heard you've been working with vector databases lately. Hi Sahil. Yes, that's right. We've been exploring the potential for improving our search capabilities. That's fascinating. What advantages have you found in using vector databases over traditional relational databases? Well, the main advantage is their ability to perform similarity searches efficiently. They're great for tasks like semantic search, recommendation systems, and image recognition. Interesting. Have you faced any challenges in implementing them? Yes. Scaling them can be tricky, especially when dealing with high-dimensional data. Also, there's a learning curve in terms of designing effective embedding models. I can imagine. Are there any particular vector database systems you'd recommend? We've had good experiences with Pinecone and Baviate. They both offer good performances and have solid documentation."
  },
  {
    "distance": 0.3404202461242676,
    "duration": 62.24,
    "entities": {
      "GPE": [
        ""
      ],
      "ORG": [
        "Pinecone"
      ],
      "PERSON": [
        "Puranjay",
        "Baviate",
        "Sahil"
      ],
      "PRODUCT": [
        ""
      ],
      "TECH": [
        "Vector Databases",
        "Any Particular Vector Database Systems",
        "Traditional Relational Databases",
        "Recommendation Systems"
      ]
    },
    "id": "78ffe568-65d0-4dd5-82eb-dbbe5c627034",
    "keywords": {
      "databases": 0.4685212856658182,
      "good": 0.31234752377721214,
      "great": 0.31234752377721214,
      "puranjay": 0.15617376188860607,
      "recognition": 0.15617376188860607,
      "recommend": 0.15617376188860607,
      "search": 0.31234752377721214,
      "systems": 0.31234752377721214,
      "vector": 0.4685212856658182,
      "yes": 0.31234752377721214
    },
    "language": "English",
    "score": 0.6595797538757324,
    "topics": [
      {
        "id": 0,
        "terms": []
      },
      {
        "id": 1,
        "terms": []
      },
      {
        "id": 2,
        "terms": []
      }
    ],
    "transcript": " Hey Puranjay, great to see you at the conference. I heard you've been working with vector databases lately. Hi Sahil. Yes, that's right. We've been exploring the potential for improving our search capabilities. That's fascinating. What advantages have you found in using vector databases over traditional relational databases? Well, the main advantage is their ability to perform similarity searches efficiently. They're great for tasks like semantic search, recommendation systems, and image recognition. Interesting. Have you faced any challenges in implementing them? Yes. Scaling them can be tricky, especially when dealing with high-dimensional data. Also, there's a learning curve in terms of designing effective embedding models. I can imagine. Are there any particular vector database systems you'd recommend? We've had good experiences with Pinecone and Baviate. They both offer good performances and have solid documentation."
  }
]


def get_answer(context, query):

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
                "content": f"""Following are the top 5 results from my vector db:\n{context}
                    Based on the above results, answer the user's query:\n{query}
                    \nFrom entities Include details like ORG, PERSONS, PRODUCT and TECH. Give your answer in form of a paragraph.
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
        get_answer(TEST_RESPONSE, "What did I talked about vector databased to puranjay?")


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
    params = {'query': query, 'limit': 5}
    api_response = requests.get(f"http://localhost:5000/search", params=params)
    text = get_answer(TEST_RESPONSE, query) 
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

