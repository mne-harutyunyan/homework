from messaging_application import User,TextMessage, MultimediaMessage

if __name__ == "__main__":

    mane = User("Mane", "mane@example.com")
    nane = User("Nane", "nane@inbox.ru")

    conv = mane.create_conversation(nane)

    message1 = TextMessage(mane, conv, "Hello Nane")
    mane.send_message(message1, conv)

    message2 = TextMessage(nane, conv, "Hello Mane, how are you?")
    nane.send_message(message2, conv)

    message1 = MultimediaMessage(mane, conv, "/Users/mena/Desktop/Homeworks_python-main 2", "homework folder")
    mane.send_message(message1, conv)
    mane.manage_settings()
    Mane_whole_conversation =  mane.view_conversation_history(conv)
    for message in Mane_whole_conversation:
        message.display_content()