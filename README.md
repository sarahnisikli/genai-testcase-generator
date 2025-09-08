GenAI Test Suite Generator

Built with Python · PyTorch · Hugging Face · Gradio

This project transforms user stories into structured QA test cases using GenAI. It blends prompt engineering with real-world automation to streamline test planning and reduce manual effort.

🚀 Features

• Converts plain user stories into detailed test cases
• Uses Hugging Face Transformers (`flan-t5-large` or `mistral-7b-instruct`)
• Interactive Gradio UI for real-time generation
• Modular pipeline for batch processing with CSV support


🛠️ Tech Stack

• Python
• PyTorch
• Hugging Face Transformers
• Gradio
• Git + GitHub


📦 How to Run

pip install -r requirements.txt
python app_genai.py


Then open the Gradio interface and paste a user story to generate test cases.

📸 Sample Output

User Story:
“As a new user, I want to provide my basic information during registration, such as name and date of birth, so that I can personalize my profile.”

Generated Test Case:
Title: Verify basic info entry
Preconditions: User is on the registration page
Steps: a. Enter name and date of birth, b. Click “Submit”
Expected Results: Profile is created with personalized info

👩‍💻 About Me

I’m Sarah — a QA automation engineer and AI Practitioner exploring the intersection of GenAI and software testing. I build tools that turn frustration into innovation.
