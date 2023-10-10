from agent import generate_response

def main():
    # Display the agent's personality description when the program starts
    print("Agent: I am a helpful assistant. What can I do for you today?")

    while True:
        # Get user input
        user_input = input("You: ")

        # Exit condition
        if user_input.lower() == 'quit':
            print("Agent: Goodbye!")
            break

        # Generate agent's response
        agent_response = generate_response(user_input)

        # Display agent's response
        print(f"Agent: {agent_response}")

if __name__ == "__main__":
    main()
