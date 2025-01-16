from oracle.retrievers import retrieve_all_trains
from langchain_core.tools import tool


@tool
def search_for_basic_information(departure_station: str, arrival_station: str):
    """Search for information about trains going from a specified departure point to an arrival point.

    Args:
        departure_station (str): The name of the departure station
        arrival_station (str): The name of the arrival station

    Returns:
        str: Information about all trains between the aforementioned stations.
    """

    # String to return to LLM with train information
    train_information = f"The following trains are available from {departure_station} to {arrival_station}:\n\n"

    # Fetch train information from retriever
    trains = retrieve_all_trains(
        departure_station=departure_station, arrival_station=arrival_station
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
