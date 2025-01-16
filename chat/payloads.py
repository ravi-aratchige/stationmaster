from pydantic import BaseModel


# User input model
class MessagePayload(BaseModel):
    content: str


# Make module safely exportable
if __name__ == "__main__":
    pass
