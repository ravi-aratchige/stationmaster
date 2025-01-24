import time
from fastapi import APIRouter
from langchain_core.messages import HumanMessage
from langchain_core.messages import AIMessage
from chat.payloads import ChatPayload, ContentOnlyMessagePayload, MessageAuthor
from chat.agents import ToolBoundAgentBuilder
from oracle.retrievers import RetrieverFactory

# Setup chatbot router
router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


# --------------------------------
#             ROUTES
# --------------------------------


# Test router health
@router.get("/ping")
def test_router():
    return {
        "message": "StationMaster Chat router is up and running.",
    }


# Test chatbot response for train info between two stations
@router.get("/test-response-train-info/", tags=["Debug"])
def test_response_train_info():
    start_time = time.time()
    message = "Are there trains available from Ja-ela to Colombo Fort?"
    agent = ToolBoundAgentBuilder()
    response = agent.invoke({"input": message})
    print(f"Execution time: {time.time() - start_time}")
    return {
        "data": response,
    }


# Test chatbot response for ticket info between two stations
@router.get("/test-response-ticket-info/", tags=["Debug"])
def test_response_ticket_info():
    start_time = time.time()
    message = "How much would a ticket from Negombo to Colombo Fort cost?"
    agent = ToolBoundAgentBuilder()
    response = agent.invoke({"input": message})
    print(f"Execution time: {time.time() - start_time}")
    return {
        "data": response,
    }


# Get response from chatbot for user input
@router.post("/get-response/", tags=["Live"])
def get_response_from_chatbot(input: ContentOnlyMessagePayload):
    message = input.content
    agent = ToolBoundAgentBuilder()
    response = agent.invoke({"input": message})
    return {
        "data": response,
    }


# Test retrievers as required
@router.get("/test-retriever/", tags=["Debug"])
def test_retriever():
    departure_station = "Ja-ela"
    arrival_station = "Colombo Fort"
    retriever = RetrieverFactory()
    output = retriever.get_ticket_prices(departure_station, arrival_station)
    return {
        "data": output,
    }


# Get chat history
@router.post("/test-chat-history/")
def get_chat_history(chat: ChatPayload):
    # Instatiate empty list to store chat history
    # in a format the agent can understand
    chat_history = []

    # Iterate through messages in chat (except last message)
    for message in chat.messages[:-1]:
        if message.sender == MessageAuthor.HUMAN:
            formatted_msg = HumanMessage(content=message.content)
        elif message.sender == MessageAuthor.STATIONMASTER:
            formatted_msg = AIMessage(content=message.content)
        # Add formatted message to chat history
        chat_history.append(formatted_msg)

    print(chat_history)

    # Setup stationmaster agent
    agent = ToolBoundAgentBuilder()

    # Invoke agent with last message in the chat (the user's latest input)
    # and the formatted chat history
    response = agent.invoke(
        {
            "input": chat.messages[-1].content,
            "chat_history": chat_history,
        }
    )

    return {
        "data": response,
    }


# Make module safely exportable
if __name__ == "__main__":
    pass
