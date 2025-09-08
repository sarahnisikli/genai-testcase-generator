def generate_prompt(user_story):
    return f"""
You are a senior QA engineer. Your task is to generate 3 detailed test scenarios based on a user story.

Now generate 3 test cases for the following user story:

User Story: "{user_story}"

Only return the test cases. Do not repeat the prompt or input.
"""
