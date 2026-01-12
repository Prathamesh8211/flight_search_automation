import os
import pandas as pd


def save_flight_data(data, file_path):

    directory = os.path.dirname(file_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    df = pd.DataFrame(data)


    df_sorted = df.sort_values(by="Price")


    df_grouped = df_sorted.groupby("Airline", as_index=False).min()

    with pd.ExcelWriter(file_path, engine="openpyxl") as writer:
        df_sorted.to_excel(writer, sheet_name="All Flights", index=False)
        df_grouped.to_excel(writer, sheet_name="Grouped By Airline", index=False)
