
def show_messages(messages):
    print("Showing messages:")
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    print("\nSending messages:")
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

messages = ["How are u?", "What are you doing?", "Hello!", "wya?"]
show_messages(messages)

sent_messages = []
send_messages(messages, sent_messages)

print("\nFinal lists:")
print(messages)
print(sent_messages)
