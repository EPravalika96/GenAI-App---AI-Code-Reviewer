from openai import OpenAI 
import streamlit as st

f = open("API_KEY.txt")
key=f.read()
client=OpenAI(api_key=key)

st.title("💬 An AI Code Reviewer")
prompt = st.text_area("Enter your python code here for review:", height=180, placeholder="Code to Review")

if st.button("Review Code") == True:
    response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an AI assistant for reviewing Python code. You should analyze the submitted code. Identify the potential bugs, errors, or areas of improvement. After Identification give bug report and fixed code snippets in a text area"},
                {"role": "user", "content": prompt}
            ]
    )

    st.write(response.choices[0].message.content)





