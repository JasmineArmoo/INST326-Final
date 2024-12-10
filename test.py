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

class Ranker:
   """
   A class used to evaluate and rank advertising locations based on cost efficiency and audience reach.


   This class helps businesses identify the most cost-effective locations to place ads by calculating metrics
   like audience reach and cost efficiency. Locations are ranked based on their ability to reach an audience
   relative to the ad cost, enabling optimized ad spend allocation.


   Attributes:
       locations (list): A list that holds dictionaries, each containing location details such as ad cost,
                         audience reach, and cost efficiency score.


   Author: Prince Osei
   """


   def __init__(self):
       """
       Initializes the Ranker instance.


       This method creates an empty list to store the evaluated location data, which includes location name,
       ad cost, audience reach, and cost efficiency score.


       Side effects:
           Initializes the locations attribute as an empty list.


       Author: Prince Osei
       """
       self.locations = []


   def add_location(self, location_name, ad_cost, foottraffic, employedpopulation, population):
       """
       Adds a location with its calculated audience reach and cost efficiency score to the list of locations.


       This method calculates the audience reach based on foot traffic, employed population, and the total
       population, and then computes the cost efficiency score based on the audience reach and the ad cost.


       Args:
           location_name (str): The name of the location being evaluated.
           ad_cost (float): The cost of running an advertisement in the location.
           foottraffic (int): The foot traffic data representing the number of people passing through the location.
           employedpopulation (int): The number of employed individuals in the location.
           population (int): The total population of the location.


       Side effects:
           Adds a dictionary representing the location to the locations list.


       Author: Prince Osei
       """
       audience_reach = self.audience_reach(foottraffic, employedpopulation, population)
       cost_efficiency_score = self.cost_efficiency_score(audience_reach, ad_cost)


       self.locations.append({
           "location_name": location_name,
           "ad_cost": ad_cost,
           "audience_reach": audience_reach,
           "cost_efficiency_score": cost_efficiency_score
       })


   def audience_reach(self, foottraffic, employedpopulation, population):
       """
       Calculates the audience reach for a location based on foot traffic, employed population, and total population.


       Audience reach is estimated by multiplying foot traffic by the proportion of employed individuals in the
       total population, which provides an estimate of the effective reach of advertisements in that location.


       Args:
           foottraffic (int): The number of people passing through the location.
           employedpopulation (int): The number of employed individuals in the location.
           population (int): The total population of the location.


       Returns:
           int: The calculated audience reach for the location.


       Author: Prince Osei
       """
       return round(foottraffic * (employedpopulation / population))


   def cost_efficiency_score(self, audience_reach, ad_cost):
       """
       Calculates the cost efficiency score for a location by dividing audience reach by ad cost.


       The cost efficiency score is a metric that evaluates how well a location can reach its audience relative
       to the cost of the advertisement. A higher score indicates a more cost-effective location for ad placement.


       Args:
           audience_reach (int): The calculated audience reach for the location.
           ad_cost (float): The cost of running an ad in the location.


       Returns:
           float: The cost efficiency score for the location.


       Author: Prince Osei
       """
       if ad_cost == 0:
           return 0
       return audience_reach / ad_cost

   def rank_locations(self, top_num=24):
       """
        Ranks the locations based on their cost efficiency scores and returns the top top_num locations.


       Locations are sorted in descending order of their cost efficiency scores, with the most cost-effective
       locations appearing first. This allows businesses to allocate their advertising budget to the locations
       that will generate the highest audience reach per dollar spent.


       Args:
           top_num (int): The number of top locations to return based on cost efficiency scores. Default is 24.


       Returns:
           list: A list of dictionaries representing the top-ranked locations based on their cost efficiency scores.


       Author: Prince Osei
      
       Techniques:
           - use of a key function (lambda, sorted)
           - optional parameters/keyword arguments

       """
       return sorted(self.locations, key=lambda loc: loc["cost_efficiency_score"], reverse=True)[:top_num]



