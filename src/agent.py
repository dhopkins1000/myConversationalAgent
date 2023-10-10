from ..plugins.internet_query import query_internet
import openai
import datetime
from settings import OPENAI_API_KEY

# Handling the Authentication
openai.api_key = OPENAI_API_KEY

# Defining the Agent Personality
personality = "I am a helpful assistant who can answer your questions, help you with tasks, and even tell jokes. What can I do for you today?"

# Function to Generate Response
def generate_response(prompt):
    # Generate a response using OpenAI API
    model_engine = "gpt-3.5-turbo"  # Update this to your chosen engine
    response = openai.ChatCompletion.create(
        model=model_engine,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
            {"role": "assistant", "content": personality}
        ]
    )

    # Check if the assistant should query the internet
    if "should I query the internet?" in response:
        internet_response = query_internet(prompt)
        response += f"\nHere's what I found: {internet_response}"

    return response['choices'][0]['message']['content'].strip()

# Main Loop for Conversation
print("Agent: ", personality)
while True:
    user_input = input("You: ")
    
    # Exit condition
    if user_input.lower() == "quit":
        print("Agent: Goodbye!")
        break
    
    # Generate prompt with personality and user input
    prompt = f"You: {user_input}\nAgent:"
    
    # Generate and print agent's response
    agent_response = generate_response(prompt)
    print("Agent: ", agent_response)
