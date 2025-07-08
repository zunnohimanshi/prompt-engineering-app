import streamlit as st
import openai
import requests
import json

st.set_page_config(page_title="Prompt Engineering Playground", layout="centered")

prompts = [
    {"task": "Text Classification", "prompt": "Classify the following email into one of the categories: Work, Personal, Promotion, Spam.\n\nEmail: 'Hey! Our annual sale is live now. Grab 50% off!'"},
    {"task": "Summarization", "prompt": "Summarize this paragraph into 2-3 lines for a newsletter: 'Banasthali Vidyapith is a women's university...'"},
    {"task": "Few-Shot Reasoning", "prompt": "Guess the pattern: 🟥 ➡️ 🟧 ➡️ 🟨 ➡️ ?"},
    {"task": "Tool Calling (JSON Output)", "prompt": "Extract the product complaint from this message and format it as JSON:\n\n'Bought this laptop last week, battery dies in 2 hours.'"},
    {"task": "Chain-of-Thought Reasoning", "prompt": "Solve this: A client had ₹1,000. They spent ₹250 on repair and refunded ₹100. What's left? Show step-by-step."}
]

st.title("🧠 Prompt Engineering Playground")
st.markdown("Select a task and run the prompt using OpenAI or DeepSeek APIs.")

task_list = [p["task"] for p in prompts]
task_choice = st.selectbox("🎯 Choose an NLP Task", task_list)

selected_prompt = next((p["prompt"] for p in prompts if p["task"] == task_choice), "")
st.subheader("📄 Prompt Preview")
st.code(selected_prompt, language="markdown")

col1, col2 = st.columns(2)

with col1:
    if st.button("🚀 Run with OpenAI"):
        try:
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=selected_prompt,
                max_tokens=150
            )
            st.success(response.choices[0].text.strip())
        except Exception as e:
            st.error(f"OpenAI Error: {e}")

with col2:
    if st.button("🛰️ Run with DeepSeek"):
        try:
            url = "https://api.deepseek.com/chat/completions"
            headers = {
                "Authorization": "Bearer YOUR_DEEPSEEK_KEY",
                "Content-Type": "application/json"
            }
            payload = {
                "model": "deepseek-chat",
                "messages": [{"role": "user", "content": selected_prompt}]
            }
            response = requests.post(url, headers=headers, json=payload)
            result = response.json()
            st.success(result["choices"][0]["message"]["content"])
        except Exception as e:
            st.error(f"DeepSeek Error: {e}")
