import csv
import argparse
import matplotlib.pyplot as plt


class Demographic:
   """
   A class for loading and analyzing demographic data from a CSV file.


   Attributes:
       demographics (dict): Dictionary containing demographic data for different locations.


   Methods:
       - load_demographics: Loads demographic data from a CSV file into a dictionary.
       - filter_locations: Filters locations based on age, income, and employment criteria.


   Author: Lynell
   """


   def __init__(self, filename):
       """
       Initializes the Demographic object and loads demographic data from the specified file.


       Args:
           filename (str): The path to the CSV file containing demographic data.


       Author: Lynell
       """
       self.demographics = self.load_demographics(filename)


   def load_demographics(self, filename):
       """
       Loads demographic data from a CSV file into a dictionary.


       Uses the with statement to ensure the file is safely opened and closed.
       Handles missing or invalid data gracefully and skips problematic rows.


       Args:
           filename (str): The path to the CSV file.


       Returns:
           dict: A dictionary with location names as keys and demographic information as values.


       Techniques:
           - with statements for file handling.
           - Exception handling for missing files and invalid data.


       Author: Lynell
       """
       data = {}
       try:
           with open(filename, "r") as file:
               reader = csv.DictReader(file)
               for row in reader:
                   try:
                       data[row["Location"]] = {
                           "age": int(float(row["Age"])),
                           "income": int(float(row["Income"])),
                           "employedpopulation": int(float(row.get("EmployedPopulation", 0))),
                           "ad_cost": int(float(row["AdCost"])),
                           "foottraffic": int(float(row["FootTraffic"])),
                           "population": int(float(row["Population"]))
                       }
                   except ValueError:
                       print(f"Skipping row with invalid data: {row}")
           return data
       except FileNotFoundError:
           print(f"Error: File {filename} not found.")
           return {}


   def filter_locations(self, target_age_range=None, target_income_range=None, min_employed_percentage=None):
       """
       Filters locations based on the provided demographic criteria.


       Applies conditional expressions to filter locations by age range, income range,
       and minimum employed population percentage.


       Args:
           target_age_range (range, optional): Target age range.
           target_income_range (range, optional): Target income range.
           min_employed_percentage (float, optional): Minimum employed population percentage.


       Returns:
           list: A list of location names that meet the criteria.


       Techniques:
           - List comprehensions for filtering data.

       Author: Lynell
       """
       if not any([target_age_range, target_income_range, min_employed_percentage]):
           # Return all locations if no filters are provided
           return list(self.demographics.keys())


       return [
           location for location, info in self.demographics.items()
           if (target_age_range is None or info["age"] in target_age_range) and
              (target_income_range is None or info["income"] in target_income_range) and
              (min_employed_percentage is None or (info["employedpopulation"] / info["population"]) * 100 >= min_employed_percentage)
       ]




