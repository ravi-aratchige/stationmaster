from pydantic import BaseModel


# User input model
class ChatDataModel(BaseModel):
    content: str
    userId: str


# Make module safely exportable
if __name__ == "__main__":
    pass
