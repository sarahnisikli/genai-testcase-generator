import gradio as gr
from prompts import generate_prompt

def mock_genai_response(prompt):
    return f"Generated test cases for:\n{prompt}"

def handle_input(text, file):
    stories = []
    if text:
        stories.append(text)
    if file:
        stories.extend(file.read().decode("utf-8").splitlines())

    results = []
    for story in stories:
        prompt = generate_prompt(story)
        response = mock_genai_response(prompt)
        results.append(response)

    return "\n\n".join(results)

demo = gr.Interface(
    fn=handle_input,
    inputs=[
        gr.Textbox(label="Paste a user story"),
        gr.File(label="Upload .txt file with user stories")
    ],
    outputs="text",
    title="GenAI Test Case Generator",
    description="Paste or upload user stories to generate test cases"
)

demo.launch()