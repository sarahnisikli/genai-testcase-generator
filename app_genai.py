import gradio as gr
from transformers import pipeline
from prompts import generate_prompt

# Load the GenAI model
generator = pipeline("text2text-generation", model="google/flan-t5-large")

# Generate test cases from user story
def generate_test_cases(user_story):
    prompt = generate_prompt(user_story)
    output = generator(prompt, max_length=512)[0]["generated_text"]
    return output

# Gradio UI
demo = gr.Interface(
    fn=generate_test_cases,
    inputs="text",
    outputs="text",
    title="GenAI Test Case Generator (Real Model)",
    description="Paste a user story and get structured test cases powered by Hugging Face."
)

demo.launch()