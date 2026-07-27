print("===================================")
print("🤖 Welcome to My AI Chatbot!")
print("===================================")
print("You can ask me simple questions.")
print("Type 'bye' or 'exit' to stop the chatbot.")

while True:

    user_input = input("\nYou: ").lower().strip()

    if user_input in ["hello", "hi", "hey"]:
        print("Bot: Hello! 👋 How can I help you?")

    elif user_input == "how are you":
        print("Bot: I am doing great! Thank you for asking. 😊")

    elif user_input in ["what is your name", "your name"]:
        print("Bot: My name is AI Assistant.")

    elif user_input == "who are you":
        print("Bot: I am a simple Rule-Based AI Chatbot.")

    elif user_input in ["what can you do", "help"]:
        print("Bot: I can respond to greetings and simple questions.")

    elif user_input == "thank you":
        print("Bot: You're welcome! 😊")

    elif user_input in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a great day! 👋")
        break

    else:
        print("Bot: Sorry, I don't understand that.")
