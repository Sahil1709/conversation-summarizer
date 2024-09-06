import streamlit as st
from streamlit_chatbox import *
import time
import simplejson as json


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
    # if streaming:
    #     generator = llm.chat_stream(query)
    #     elements = chat_box.ai_say(
    #         [
    #             # you can use string for Markdown output if no other parameters provided
    #             Markdown("thinking", in_expander=in_expander,
    #                      expanded=True, title="answer"),
    #             Markdown("", in_expander=in_expander, title="references"),
    #         ]
    #     )
    #     time.sleep(1)
    #     text = ""
    #     for x, docs in generator:
    #         text += x
    #         chat_box.update_msg(text, element_index=0, streaming=True)
    #     # update the element without focus
    #     chat_box.update_msg(text, element_index=0, streaming=False, state="complete")
    #     chat_box.update_msg("\n\n".join(docs), element_index=1, streaming=False, state="complete")
    #     chat_history_id = "some id"
    #     chat_box.show_feedback(**feedback_kwargs,
    #                             key=chat_history_id,
    #                             on_submit=on_feedback,
    #                             kwargs={"chat_history_id": chat_history_id, "history_index": len(chat_box.history) - 1})
        
    # text: response from llm
    # docs: list of references
    chat_box.ai_say(
        [
            # you can use string for Markdown output if no other parameters provided
            Markdown("thinking", in_expander=in_expander,
                        expanded=True, title="answer"),
            Markdown("", in_expander=in_expander, title="references"),
        ]
    )
    text, docs = llm.chat(query)
    time.sleep(1) # simulate thinking
    chat_box.update_msg(text, element_index=0, streaming=False, state="complete")
    chat_box.update_msg("\n\n".join(docs), element_index=1, streaming=False, state="complete")
    # chat_box.ai_say(
    #     [
    #         Markdown(text, in_expander=in_expander,
    #                  expanded=True, title="answer"),
    #         Markdown("\n\n".join(docs), in_expander=in_expander,
    #                  title="references"),
    #     ]
    # )

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


# if show_history:
#     st.write(st.session_state)
