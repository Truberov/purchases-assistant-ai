from langchain.chat_models.gigachat import GigaChat
from assistant.config import get_settings


def get_chat_model() -> GigaChat:
    return GigaChat(
        **get_settings().giga_chat_params
    )
