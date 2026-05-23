from datetime import datetime # The datetime module provides classes for manipulating dates and times. We import the datetime class from this module to work with date and time in our chatbot.

print("🤖 DecodeBot Started!")
print("Type 'bye' to exit.\n")

while True:

    user = input("You: ").lower()

    # Greetings
    if user in ["hi", "hello", "hey"]:
        print("Bot: Hello! How can I help you?")

    # About Bot
    elif ["your name", "what is your name"] in user:
        print("Bot: I am DecodeBot, your AI assistant.")

    # How are you
    elif "how are you" in user:
        print("Bot: I'm functioning perfectly!")

    # Time
    elif ["time", "what time is it"] in user:
        current_time = datetime.now().strftime("%I:%M %p")
        # Note: The above line gets the current time and formats it as hours:minutes AM/PM. %i for 12-hour format, %M for minutes, and %p for AM/PM. You can adjust the format as needed.
        print("Bot: Current time is", current_time)

    # Exit
    elif user in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a great day.")
        break

    # Unknown
    else:
        print("Bot: Sorry, I don't understand that yet.")