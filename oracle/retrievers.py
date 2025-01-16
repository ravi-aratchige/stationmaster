from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.webdriver import set_chrome_options
from selenium.webdriver.common.keys import Keys


def retrieve_all_trains(departure_station: str, arrival_station: str):
    # INITIALIZATION

    # Set time to sleep between button clicks (to avoid DOM overlapping issues)
    seconds_to_wait = 5

    # Setup the webdriver
    driver = webdriver.Chrome(options=set_chrome_options())

    # Open website in browser
    driver.get("https://trainschedule.lk/")

    # DEPARTURE SELECTION

    try:
        # Locate the departure station input field and click it
        driver.find_element(By.CSS_SELECTOR, "button[data-id='drStartStation']").click()

        # Locate the departure station input field and enter the station name
        driver.find_element(
            By.XPATH,
            "/html/body/div/main/div/div[2]/div/div/div/div/form/div[1]/div/div/div/input",
        ).send_keys(departure_station + Keys.ENTER)

        # Wait before proceeding (to over DOM overlapping issues)
        print(f"INFO: Waiting for {seconds_to_wait} seconds...")
        sleep(seconds_to_wait)

    except:
        print("ERROR: An error occured while selecting the departure station.")

    else:
        print("INFO: Departure station selected successfully.")

    # ARRIVAL SELECTION

    try:
        # Locate the arrival station input field and click it
        driver.find_element(By.CSS_SELECTOR, "button[data-id='drEndStation']").click()

        # Locate the arrival station input field and enter the station name
        driver.find_element(
            By.XPATH,
            "/html/body/div/main/div/div[2]/div/div/div/div/form/div[2]/div/div/div/input",
        ).send_keys(arrival_station + Keys.ENTER)

        # Wait before proceeding (to over DOM overlapping issues)
        print(f"INFO: Waiting for {seconds_to_wait} seconds...")
        sleep(seconds_to_wait)

    except:
        print("ERROR: An error occured while selecting the arrival station.")

    else:
        print("INFO: Arrival station selected successfully.")

    # Locate the "Search" button and click it
    driver.find_element(
        By.XPATH, "/html/body/div/main/div/div[2]/div/div/div/div/form/button"
    ).click()

    # RESULTS

    results_table = driver.find_element(
        By.XPATH, "/html/body/div/main/div[1]/div[2]/div/div/table"
    )

    # List to store all train results
    all_available_trains = []

    results_table_rows = results_table.find_elements(By.TAG_NAME, "tr")
    for row in results_table_rows:
        # Skip past the empty rows in the table structure
        if row.text == "":
            continue

        # Dict to store each train
        train_info = {
            "departure_time": "",
            "arrival_time": "",
            "time_taken": "",
            "train_ends_at": "",
            "train_number": "",
            "train_type": "",
        }

        # Select cells in each row
        cells_of_row = row.find_elements(By.TAG_NAME, "td")

        # Iterate over cells in each row
        for cell in cells_of_row:
            if cell == cells_of_row[0]:
                train_info["departure_time"] = cell.text
            elif cell == cells_of_row[1]:
                train_info["arrival_time"] = cell.text
            elif cell == cells_of_row[2]:
                train_info["time_taken"] = cell.text
            elif cell == cells_of_row[3]:
                train_info["train_ends_at"] = cell.text
            elif cell == cells_of_row[4]:
                train_info["train_number"] = cell.text
            else:
                train_info["train_type"] = cell.text

        print(f"Train info: {train_info}")
        all_available_trains.append(train_info)

    return all_available_trains


# Make module safely exportable
if __name__ == "__main__":
    pass
