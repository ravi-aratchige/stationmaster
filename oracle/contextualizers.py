from langchain_core.tools import tool
from oracle.retrievers import RetrieverFactory


@tool
def get_trains_between_stations(departure_station: str, arrival_station: str) -> str:
    """Find out which trains are available between a departure station and an arrival station.

    Args:
        departure_station (str): The name of the departure station
        arrival_station (str): The name of the arrival station

    Returns:
        str: Information about all trains between the aforementioned stations.
    """

    # String to return to LLM with train information
    train_information = f"The following trains are available from {departure_station} to {arrival_station}:\n\n"

    # Setup retriever
    retriever = RetrieverFactory()

    # Fetch train information from retriever
    trains = retriever.get_all_trains(
        departure_station=departure_station,
        arrival_station=arrival_station,
    )

    if trains == None:
        return "An error occured and train data could not be fetched."

    # Iterate through all trains and add to string of train info
    for train in trains:
        train_information += (
            f"TRAIN\n"
            f"Departure time: {train["departure_time"]}\n"
            f"Arrival time: {train["arrival_time"]}\n"
            f"Time taken: {train["time_taken"]}\n"
            f"Train ends at: {train["train_ends_at"]}\n"
            f"Train Number: {train["train_number"]}\n"
            f"Train type: {train["train_type"]}\n"
        )

    return train_information


@tool
def get_ticket_prices(departure_station: str, arrival_station: str) -> str:
    """Get ticket prices for trains based on their departure and arrival stations.

    Args:
        departure_station (str): The name of the departure station
        arrival_station (str): The name of the arrival station

    Returns:
        str: Information about ticket prices of trains between the aforementioned stations.
    """

    # String to return to LLM with ticket information
    ticket_price_information = f"Here are the ticket prices for trains from {departure_station} to {arrival_station}:\n\n"

    # Setup retriever
    retriever = RetrieverFactory()

    # Fetch train information from retriever
    ticket_prices = retriever.get_ticket_prices(
        departure_station=departure_station,
        arrival_station=arrival_station,
    )

    if ticket_prices == None:
        return "An error occured and ticket pricing data could not be fetched."

    # Add ticket pricing data to string of ticket info
    if "first_class" in ticket_prices:
        ticket_price_information += f"First class: {ticket_prices["first_class"]}\n"
    if "second_class" in ticket_prices:
        ticket_price_information += f"Second class: {ticket_prices["second_class"]}\n"
    if "third_class" in ticket_prices:
        ticket_price_information += f"Third class: {ticket_prices["third_class"]}\n"

    return ticket_price_information


# Make module safely exportable
if __name__ == "__main__":
    pass
