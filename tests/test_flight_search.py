from pages.flight_search_page import FlightSearchPage
from utils.excel_utils import save_flight_data

def test_flight_search(page):
    flight_page = FlightSearchPage(page)

    flight_page.open_site()
    flight_page.search_flight("Delhi", "Mumbai")

    flights = flight_page.extract_flight_details()

    save_flight_data(flights, "reports/flight_results.xlsx")

    assert len(flights) > 0

    for flight in flights:
        assert flight["Stops"] == 1
        assert 4000 <= flight["Price"] <= 8000

