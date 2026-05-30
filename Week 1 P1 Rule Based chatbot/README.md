# DecodeBot - Rule-Based AI Chatbot

DecodeBot is a simple rule-based chatbot written in Python. It responds to a small set of user inputs such as greetings, name questions, mood questions, time requests, and exit commands.

## Features

- Responds to greetings like `hi`, `hello`, and `hey`
- Answers when asked for its name
- Replies to `how are you`
- Shows the current time when the user mentions `time`
- Exits cleanly with `bye`, `exit`, or `quit`

## Requirements

- Python 3.x

## How To Run

1. Open a terminal in the project folder.
2. Run the chatbot script:

```bash
python rule_based_ai_chatbot.py
```

## Example Conversation

```text
🤖 DecodeBot Started!
Type 'bye' to exit.

You: hello
Bot: Hello! How can I help you?

You: what is your name?
Bot: I am DecodeBot, your AI assistant.

You: what time is it?
Bot: Current time is 03:42 PM

You: bye
Bot: Goodbye! Have a great day.
```

## Project Structure

- `rule_based_ai_chatbot.py` - main chatbot script
- `Artificial intelligence P1.pdf` - related project document

## Notes

- The chatbot uses simple keyword matching, so responses depend on the exact text entered by the user.
- Input is converted to lowercase before checking, which makes the bot case-insensitive for the supported phrases.
