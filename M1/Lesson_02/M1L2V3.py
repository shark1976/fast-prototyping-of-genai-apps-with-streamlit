# import packages
from dotenv import load_dotenv
import openai
import streamlit as st


# load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
client = openai.OpenAI()

st.title("Hello, GenAI!")
st.write("This is your first Streamlit app.")

# response = client.responses.create(
#     model="gpt-5-mini",
#     input=[
#         {"role": "user", "content": "Explain generative AI in one sentence."}  # Prompt
#     ],
#     #temperature=0.7,  # A bit of creativity
#     #max_output_tokens=100  # Limit response length
# )

# print the response from OpenAI
#st.write(response.output_text)

st.write("This is the end of your first Streamlit app.")