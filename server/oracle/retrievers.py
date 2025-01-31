from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.browser import BrowserOptionsFactory
from selenium.webdriver.common.keys import Keys


class RetrieverFactory:
    def __init__(self):
        # Initialize webdriver with relevant options
        self.driver = webdriver.Chrome(
            options=BrowserOptionsFactory.get_browser_options("chrome")
        )

    def _query_info_for_stations(self, departure_station: str, arrival_station: str):
        """Private method to query information based on departure and arrival stations.

        This method is used by other public methods that read information
        from the results page of the website.

        Args:
            departure_station (str): The name of the departure station
            arrival_station (str): The name of the arrival station
        """

        # ----- INITIALIZATION -----

        # Get webdriver from class members
        driver = self.driver

        # Open website in browser
        driver.get("https://trainschedule.lk/")

        # ----- DEPARTURE SELECTION -----

        # Locate the departure station input field and click it
        driver.find_element(By.CSS_SELECTOR, "button[data-id='drStartStation']").click()

        # Locate the departure station input field and enter the station name
        driver.switch_to.active_element.send_keys(departure_station + Keys.ENTER)

        print("INFO: Departure station entered successfully.")

        # ----- ARRIVAL SELECTION -----

        # Locate the arrival station input field and click it
        driver.find_element(By.CSS_SELECTOR, "button[data-id='drEndStation']").click()

        # Locate the arrival station input field and enter the station name
        driver.switch_to.active_element.send_keys(arrival_station + Keys.ENTER)

        print("INFO: Arrival station entered successfully.")

        # Locate the "Search" button and click it
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    def get_all_trains(self, departure_station: str, arrival_station: str):
        try:
            # Query information using private retriever method
            self._query_info_for_stations(
                departure_station=departure_station, arrival_station=arrival_station
            )

            # ----- RESULTS PAGE -----

            results_table = self.driver.find_element(
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

        except Exception as e:
            print("ERROR: Something went wrong while scraping data...")
            print(f"The error:\n{e}")

            # Close the browser
            print("INFO: Closing the browser and stopping ChromiumDriver executable...")
            self.driver.quit()

            return None

        else:
            # Close the browser
            print("INFO: Closing the browser and stopping ChromiumDriver executable...")
            self.driver.quit()

            return all_available_trains

    def get_ticket_prices(self, departure_station: str, arrival_station: str):
        try:
            # Query information using private retriever method
            self._query_info_for_stations(
                departure_station=departure_station, arrival_station=arrival_station
            )

            # ----- RESULTS PAGE -----

            # Locate table with ticket prices
            price_table_body = self.driver.find_element(
                By.XPATH, "/html/body/div/main/div[2]/div/table/tbody"
            )

            # Dict to store ticket prices
            prices = {}

            rows_in_table = price_table_body.find_elements(By.TAG_NAME, "tr")

            for row in rows_in_table:
                # Split content in a single row into class and price
                data = row.text.lower().split(" class rs. ")

                # NOTE
                # e.g. "2nd Class Rs. 150.00" is split into a list as ["2nd", "150.00"]

                # Change class in list into camel case string
                if data[0] == "1st":
                    data[0] = "first_class"
                elif data[0] == "2nd":
                    data[0] = "second_class"
                elif data[0] == "3rd":
                    data[0] = "third_class"

                # Convert string ticket price into float
                data[1] = float(data[1])

                # Add processed data to prices dict
                prices[data[0]] = data[1]

        except Exception as e:
            print("ERROR: Something went wrong while scraping data...")
            print(f"The error:\n{e}")

            # Close the browser
            print("INFO: Closing the browser and stopping ChromiumDriver executable...")
            self.driver.quit()

            return None

        else:
            # Close the browser
            print("INFO: Closing the browser and stopping ChromiumDriver executable...")
            self.driver.quit()

            return prices


# Make module safely exportable
if __name__ == "__main__":
    pass
