active = True
while active:
    message = input ("Enter your message. Enter quit the loop.")
    message = message.strip()
    if message == 'quit':
        active = False
    else:
        print(active)
