import re

def chatbot():
    print("Bot: Hello! I'm ChatBot. How can I help you today?")
    
    while True:
        user_input = input("You: ").lower()

        if user_input in ['exit', 'quit', 'bye']:
            print("Bot: Goodbye! Have a great day!")
            break

        elif re.search(r'\b(hi|hello|hey)\b', user_input):
            print("Bot: Hello there! How can I assist you?")

        elif re.search(r'\bhow are you\b', user_input):
            print("Bot: I'm just a program, but I'm functioning as expected!")

        elif re.search(r'\bwhat.*your name\b', user_input):
            print("Bot: I'm ChatBot, your virtual assistant.")

        elif re.search(r'\bhelp\b', user_input):
            print("Bot: Sure! You can ask me about the weather, time, or just chat.")

        elif re.search(r'\b(time|date)\b', user_input):
            from datetime import datetime
            now = datetime.now()
            print(f"Bot: The current date and time is {now.strftime('%Y-%m-%d %H:%M:%S')}.")

        else:
            print("Bot: I'm sorry, I don't understand that. Can you rephrase?")

chatbot()