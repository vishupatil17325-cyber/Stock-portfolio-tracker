# Basic Chatbot

def chatbot_response(user_input):
    user_input = user_input.lower()

    if user_input == "hello":
        return "Hi! How can I help you?"

    elif user_input == "how are you":
        return "I'm fine, thanks!"

    elif user_input == "what is your name":
        return "I'm a simple Python chatbot."

    elif user_input == "bye":
        return "Goodbye! Have a nice day!"

    else:
        return "Sorry, I don't understand that."



print("===== Basic Chatbot =====")
print("Type 'bye' to exit.")

while True:
    user_input = input("You: ")

    response = chatbot_response(user_input)
    print("Bot:", response)

    if user_input.lower() == "bye":
        break