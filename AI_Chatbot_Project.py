print("====================================")
print("        AI CHATBOT SYSTEM")
print("====================================")
print("Type 'bye' to exit the chatbot")

while True:

    user = input("\nYou: ").lower()

    if user == "hello":
        print("Bot: Hello! Welcome to AI Chatbot.")

    elif user == "hi":
        print("Bot: Hi! Nice to meet you.")

    elif user == "how are you":
        print("Bot: I am doing great. Thank you for asking!")

    elif user == "what is your name":
        print("Bot: My name is AI ChatBot.")

    elif user == "what is ai":
        print("Bot: AI stands for Artificial Intelligence.")

    elif user == "who created you":
        print("Bot: I was created using Python programming.")

    elif user == "what can you do":
        print("Bot: I can answer simple questions and chat with users.")

    elif user == "tell me a joke":
        print("Bot: Why do programmers prefer dark mode? Because light attracts bugs!")

    elif user == "what is python":
        print("Bot: Python is a popular programming language.")

    elif user == "what is machine learning":
        print("Bot: Machine Learning is a branch of AI that helps computers learn from data.")

    elif user == "what is data science":
        print("Bot: Data Science is the study of data to gain useful insights.")

    elif user == "what is github":
        print("Bot: GitHub is a platform used to store and manage code.")

    elif user == "what is linkedin":
        print("Bot: LinkedIn is a professional networking platform.")

    elif user == "thank you":
        print("Bot: You're welcome!")

    elif user == "good morning":
        print("Bot: Good Morning! Have a great day.")

    elif user == "good afternoon":
        print("Bot: Good Afternoon!")

    elif user == "good evening":
        print("Bot: Good Evening!")

    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that question.")