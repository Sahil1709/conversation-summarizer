# Conversation Summarizer
## Conversation Summarizer Speech to Text

The Conversation Summarizer Speech to Text is a web application that allows users to convert spoken conversations into written text and generate summaries of those conversations. It utilizes Streamlit, FastApi, and Groq to provide a seamless user experience.

With this app, users can easily summarize and analyze their conversations by following a few simple steps. The app supports both the frontend and backend components, allowing users to run them separately in different terminal windows or tabs.

Experience the power of converting speech to text and generating conversation summaries with the Conversation Summarizer Speech to Text app.


## Tech Stack 
- Streamlit
- FastApi
- Groq

## Usage
To run the frontend and backend of the conversation summarizer, please follow these steps:

1. Ensure that you have [Poetry](https://python-poetry.org/) installed on your system. If not, please install it first.

2. Open a terminal and navigate to the project directory.

3. Install the project dependencies by running `poetry install`.

4. Activate the Poetry shell by running the command `poetry shell`.

5. To run the frontend, execute the command `streamlit run stt.py` from within the Poetry shell.

6. To run the backend, execute the command `fastapi dev backend.py` also from within the Poetry shell.

Remember to run both the frontend and backend commands separately in different terminal windows or tabs.
