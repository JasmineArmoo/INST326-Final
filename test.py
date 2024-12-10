import json
import argparse
import matplotlib.pyplot as plt

class Demographic:
    """
    A class for loading and analyzing demographic data from a JSON file.

    Attributes:
        demographics (dict): Dictionary containing demographic data for different locations.

    Methods:
        - load_demographics: Loads demographic data from a JSON file into a dictionary.
        - filter_locations: Filters locations based on age, income, and employment criteria.

    Author: Lynell 
    """

    def __init__(self, filename):
        """
        Initializes the Demographic object and loads demographic data from the specified file.

        Args:
            filename (str): The path to the JSON file containing demographic data.

        Author: Lynell
        """
        self.demographics = self.load_demographics(filename)

    def load_demographics(self, filename):
        """
        Loads demographic data from a JSON file into a dictionary.

        Opens the JSON file and parses its content. Handles errors such as missing files or invalid JSON formatting.

        Args:
            filename (str): The path to the JSON file.

        Returns:
            dict: A dictionary with location names as keys and demographic information as values. Returns an empty dictionary if the file is missing or invalid.

        Techniques:
            - use of json.load()

        Author: Lynell
        """
        try:
            with open(filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: File {filename} not found.")
            return {}
        except json.JSONDecodeError:
            print(f"Error: File {filename} is not a valid JSON file.")
            return {}

    def filter_locations(self, target_age_range=None, target_income_range=None, min_employed_percentage=None):
        """
        Filters locations based on the provided demographic criteria.

        Applies conditional filters to demographic data. Locations are filtered by age range, income range, and minimum employed population percentage. If no criteria are provided, all locations are returned.

        Args:
            target_age_range (range): Target age range of demographic.
            target_income_range (range): Target income range of demographic.
            min_employed_percentage (float): Minimum employed population percentage (0-100).

        Returns:
            list: A list of location names that meet the criteria. Returns all locations if no filters are applied.
            
        Techniques:
            - condtional expressions
            
        Author: Lynell
        """
        if not any([target_age_range, target_income_range, min_employed_percentage]):
            return list(self.demographics.keys())

        return [
            location for location, info in self.demographics.items()
            if (target_age_range is None or int(info["age"]) in target_age_range) and
               (target_income_range is None or int(info["income"]) in target_income_range) and
               (min_employed_percentage is None or (info["employedpopulation"] / info["population"]) * 100 >= min_employed_percentage)
        ]
        