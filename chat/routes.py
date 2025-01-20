import time
from fastapi import APIRouter
from chat.payloads import MessagePayload
from chat.agents import ToolBoundAgentBuilder
from oracle.retrievers import retrieve_ticket_prices

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
def get_response_from_chatbot(input: MessagePayload):
    message = input.content
    agent = ToolBoundAgentBuilder()
    response = agent.invoke({"input": message})
    return {
        "data": response,
    }


# Test retrievers as required
@router.get("/test-retriever/")
def test_retriever():
    departure_station = "Ja-ela"
    arrival_station = "Colombo Fort"
    output = retrieve_ticket_prices(departure_station, arrival_station)
    return {
        "data": output,
    }


# Make module safely exportable
if __name__ == "__main__":
    pass
