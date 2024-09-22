from typing import List
from datetime import datetime
import abc

class MessagingManager(abc.ABC):
    @abc.abstractmethod
    def send_message(self, message: 'Message') -> None:
        pass

    @abc.abstractmethod
    def receive_message(self, message: 'Message') -> None:
        pass

    @abc.abstractmethod
    def view_conversation_history(self, conversation: 'Conversation') -> List['Message']:
        pass

class User(MessagingManager):
    def __init__(self, name: str, contact_info: str) -> None:
        self.name = name
        self.contact_info = contact_info
        self.conversations: List[Conversation] = []

    def create_conversation(self, user: 'User') -> 'Conversation':
        conversation = Conversation([self, user])
        self.conversations.append(conversation)
        user.conversations.append(conversation)
        return conversation

    def send_message(self, message: 'Message', conversation: 'Conversation') -> None:
        conversation.add_message(message)

    def receive_message(self, message: 'Message') -> None:
        message.display_content()

    def view_conversation_history(self, conversation: 'Conversation') -> List['Message']:
        return conversation.get_messages()

    def manage_settings(self) -> None:
        print(f"{self.name} is managing settings...")

    def get_conversations(self) -> List['Conversation']:
        return self.conversations

class Conversation:
    def __init__(self, participants: List['User']):
        self.participants = participants
        self.message_history = []

    def add_message(self, message: 'Message') -> None:
        self.message_history.append(message)

    def add_user(self, user: 'User') -> None:
        self.participants.append(user)

    def get_messages(self) -> List['Message']:
        return self.message_history

class Message(abc.ABC):
    def __init__(self, sender: 'User', conversation: Conversation):
        self.sender = sender
        self.conversation = conversation
        self.timestamp = datetime.now()

    @abc.abstractmethod
    def display_content(self) -> None:
        pass

    @abc.abstractmethod
    def get_message_type(self) -> str:
        pass

class TextMessage(Message):
    def __init__(self, sender: 'User', conversation: Conversation, content: str):
        super().__init__(sender, conversation)
        self.content = content

    def display_content(self) -> None:
        print(f"{self.sender.name}: {self.content} ({self.timestamp})")

    def get_message_type(self) -> str:
        return "Text"

class MultimediaMessage(Message):
    def __init__(self, sender: 'User', conversation: Conversation, file_path: str, media_type: str):
        super().__init__(sender, conversation)
        self.file_path = file_path
        self.media_type = media_type

    def display_content(self) -> None:
        print(f"{self.sender.name}: opening {self.media_type} in {self.file_path} ({self.timestamp})")

    def get_message_type(self) -> str:
        return self.media_type
