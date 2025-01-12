import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI

# Set up LangChain with OpenAI LLM
llm = OpenAI(api_key='your_openai_api_key')  # Replace with your OpenAI API key
template = "Create a multiple-choice question about {topic}. Provide four answer options and indicate the correct one."

# Streamlit app setup
st.title("Multiple Choice Quiz Bot")

# Input for topic
topic = st.text_input("Enter a topic for the quiz:")

if topic:
    # Generate a question using LangChain
    prompt = PromptTemplate(template=template, input_variables=["topic"])
    chain = LLMChain(prompt=prompt, llm=llm)
    response = chain.run(topic=topic)

    # Assuming response format: Question; Option1; Option2; Option3; Option4; Correct Option
    question, *options, correct_option = response.split(";")

    st.write("### Question:")
    st.write(question.strip())

    # Multiple choice options
    selected_option = st.radio("Choose your answer:", [opt.strip() for opt in options])

    # Submit button
    if st.button("Submit"):
        if selected_option == correct_option.strip():
            st.success("Correct!")
        else:
            st.error(f"Incorrect! The correct answer was: {correct_option.strip()}.")

# Run the Streamlit app using `streamlit run quiz_app.py`
