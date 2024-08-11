import pandas as pd


class CSVLoader:

    def __init__(self, csv_file = None):
        """
        Initializes the CSVLoader with an optional path to the CSV file.

        :param csv_file: Path to the output CSV file. Can be set later if not provided at initialization.
        """
        self.csv_file = csv_file


    def load(self, data: list, csv_file = None, mode = 'w', index = False):
        """
        Loads the provided data into a Pandas DataFrame and saves it to a CSV file.

        :param data: A list of dictionaries or a list of lists where each item represents a row.
        :param csv_file: Optional path to the CSV file where the data will be saved. If not provided,
                         it will use the path set during initialization.
        :param mode: File mode for saving the CSV. Default is 'w' (write). Use 'a' (append) to add to an existing file.
        :param index: Whether to include the DataFrame index in the CSV file. Default is False.
        :return: The DataFrame created from the data.
        """
        if csv_file is None:
            csv_file = self.csv_file

        if csv_file is None:
            raise ValueError("CSV file path must be provided either at initialization or during the load call.")

        # Convert the list of data to a Pandas DataFrame
        df = pd.DataFrame(data)

        # Save the DataFrame to a CSV file
        df.to_csv(csv_file, mode=mode, index=index)

        # Return the DataFrame in case further processing is needed
        return df
