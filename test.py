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
   
   def get_average(self, demographics, filtered_locations):
    """
    Calculates and returns the average values for age, income, and employed population 
    for a list of filtered locations.

    Args:
        demographics (dict): Demographic data for locations.
        filtered_locations (list): List of locations to analyze.

    Returns:
        dict: A dictionary containing the averages for age, income, and employedpercentage.
              Returns 0 for each if no filtered locations are provided.
              
    Author: Prince Osei
    """
    if not filtered_locations:
        print("No filtered locations provided.")
        return {"age": 0, "income": 0, "employedpercentage": 0}

    total_age = sum([demographics[loc]["age"] for loc in filtered_locations])
    total_income = sum([demographics[loc]["income"] for loc in filtered_locations])
    total_employed_percentage = sum([
        (demographics[loc]["employedpopulation"] / demographics[loc]["population"]) * 100
        for loc in filtered_locations
    ])

    count = len(filtered_locations)

    return {
        "age": total_age / count,
        "income": total_income / count,
        "employedpercentage": total_employed_percentage / count
    }