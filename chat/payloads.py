from enum import Enum
from typing import List
from pydantic import BaseModel


class MessageAuthor(str, Enum):
    STATIONMASTER = "stationmaster"
    HUMAN = "human"


# User input model (content only)
class ContentOnlyMessagePayload(BaseModel):
    content: str


# User input model (content and sender)
class ContentAndSenderMessagePayload(BaseModel):
    content: str
    sender: MessageAuthor = MessageAuthor.HUMAN


# Complete chat model
class ChatPayload(BaseModel):
    messages: List[ContentAndSenderMessagePayload]


# Make module safely exportable
if __name__ == "__main__":
    pass
